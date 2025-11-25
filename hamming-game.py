import random
import numpy as np

# --- Configuration ---
# Hamming (7,4) Parity Check Matrix (H)
# H is constructed such that its columns are the binary representations of 1 through 7.
# H @ codeword.T = syndrome
H = np.array([
    [0, 0, 0, 1, 1, 1, 1],  # P1 checks bits 4, 5, 6, 7
    [0, 1, 1, 0, 0, 1, 1],  # P2 checks bits 2, 3, 6, 7
    [1, 0, 1, 0, 1, 0, 1]   # P4 checks bits 3, 5, 7
], dtype=np.int8)

# Map the 3-bit syndrome (p4, p2, p1) to the error position (1 to 7)
# Note: P4 is the most significant bit in the standard representation.
SYNDROME_TO_ERROR = {
    '001': 1, '010': 2, '011': 3, '100': 4,
    '101': 5, '110': 6, '111': 7
}

class HammingGame:
    """
    A conceptual class for a Decodoku-style game using Hamming(7,4) codes.
    The goal is to correct a single error based on the calculated syndrome.
    """

    def __init__(self):
        self.message = self._generate_random_message()
        self.codeword = self._encode(self.message)
        self.error_position = 0
        self.corrupted_codeword = []
        self._introduce_error()

    def _generate_random_message(self):
        """Generates a 4-bit message (m4, m3, m2, m1)."""
        return np.array([random.randint(0, 1) for _ in range(4)], dtype=np.int8)

    def _encode(self, message):
        """
        Encodes the 4-bit message into a 7-bit Hamming(7,4) codeword.
        Codeword structure: (p4, p2, m4, p1, m3, m2, m1) - using standard indices (7 to 1).
        In this 0-indexed array: (c6, c5, c4, c3, c2, c1, c0)
        Indices: 6 5 4 3 2 1 0
        Bits:    p4 p2 m4 p1 m3 m2 m1
        """
        m = message # [m4, m3, m2, m1]
        c = np.zeros(7, dtype=np.int8)

        # Map message bits to codeword positions (c[index] = message_bit)
        c[4], c[2], c[1], c[0] = m[0], m[1], m[2], m[3]

        # Calculate parity bits (XOR sums)
        # P1 (c3) checks c4, c2, c1, c0 -> (m4, m3, m2, m1) - NOT standard
        # Standard P1 (bit 1) checks bits 3, 5, 7. In array: 6, 4, 2, 0
        c[3] = (c[6] + c[4] + c[2] + c[0]) % 2 # Checks bits 1, 3, 5, 7

        # P2 (c5) checks bits 2, 3, 6, 7. In array: 5, 4, 1, 0
        c[5] = (c[6] + c[5] + c[3] + c[2]) % 2 # Checks bits 2, 3, 6, 7

        # P4 (c6) checks bits 4, 5, 6, 7. In array: 3, 2, 1, 0
        c[6] = (c[6] + c[5] + c[4] + c[3]) % 2 # Checks bits 4, 5, 6, 7

        # We'll stick to the simpler structure where H defines the rules.
        # Let's use the H matrix for the encoding, which is conceptually simpler for a puzzle.
        # (c0, c1, c2, c3, c4, c5, c6) -> [m1, m2, m3, m4, p1, p2, p3]
        # Since the puzzle is about decoding a *received* word, we only need the H matrix.
        # Let's create a random *valid* codeword and then corrupt it.
        # c = [m1, m2, m3, m4, p1, p2, p3]
        G = np.array([
            [1, 0, 0, 0, 1, 1, 0],  # m1 -> c0, c4, c5
            [0, 1, 0, 0, 1, 0, 1],  # m2 -> c1, c4, c6
            [0, 0, 1, 0, 0, 1, 1],  # m3 -> c2, c5, c6
            [0, 0, 0, 1, 1, 1, 1]   # m4 -> c3, c4, c5, c6
        ], dtype=np.int8)
        codeword = np.dot(message, G) % 2
        return codeword

    def _introduce_error(self):
        """Randomly flips exactly one bit in the codeword."""
        self.corrupted_codeword = self.codeword.copy()
        # Choose a random position (0 to 6) to flip
        self.error_position = random.randint(0, 6)
        # Flip the bit (XOR with 1)
        self.corrupted_codeword[self.error_position] ^= 1

    def calculate_syndrome(self, word):
        """
        Calculates the 3-bit syndrome for a 7-bit word (H @ word.T).
        The result is a column vector [s1, s2, s3] where the syndrome bits
        correspond to the rows of H.
        """
        syndrome_vec = np.dot(H, word) % 2
        # Convert to string (p4, p2, p1) for lookup, using the order of H rows.
        # H rows are [p1 check, p2 check, p4 check] (by standard definition of column weights)
        # The lookup table uses the syndrome value (p4, p2, p1) for error location.
        # Since H is [p1, p2, p4] in this array, we read it as [s1, s2, s3].
        # Let's adjust the H matrix definition to be [p4, p2, p1] for cleaner syndrome reading:
        H_puzzle = np.array([
            [1, 0, 1, 0, 1, 0, 1],  # Row 0: P4 (checks 3, 5, 7)
            [0, 1, 1, 0, 0, 1, 1],  # Row 1: P2 (checks 2, 3, 6, 7)
            [0, 0, 0, 1, 1, 1, 1]   # Row 2: P1 (checks 4, 5, 6, 7)
        ], dtype=np.int8)
        syndrome_vec = np.dot(H_puzzle, word) % 2
        
        # syndrome_vec is [s_p4, s_p2, s_p1]
        syndrome_str = "".join(map(str, syndrome_vec))
        return syndrome_str

    def start_game(self):
        """Runs a single round of the Hamming Decodoku puzzle."""
        print("--- Hamming(7,4) Decodoku: Bit-Flip Challenge ---")
        print("\nYour Goal: Find the single error and fix it.")
        print(f"H Matrix Rows: P4, P2, P1 checks (indices 0-6)")

        # 1. Show the corrupted codeword
        print("\n[RECEIVED CODEWORD (7 bits)]")
        print("Index: [0][1][2][3][4][5][6]")
        print(f"Value: {list(self.corrupted_codeword)}")

        # 2. Calculate and display the syndrome (the puzzle hint)
        syndrome = self.calculate_syndrome(self.corrupted_codeword)
        print(f"\n[CALCULATED SYNDROME (P4, P2, P1)]: {syndrome}")

        if syndrome == '000':
            print("Syndrome is 000. No error detected. (This shouldn't happen in the challenge mode!)")
            return

        # 3. Player's guess
        try:
            player_guess = int(input(
                "\nWhich index (0-6) do you think is the error location? "
            ))
            if 0 <= player_guess <= 6:
                # 4. Check the answer
                # The index is the position - 1. E.g., error at '101' means pos 5, index 4.
                # SYNDROME_TO_ERROR maps the syndrome string to the 1-based index (1 to 7).
                # We need to convert this 1-based index to the 0-based array index (0 to 6).
                error_pos_1based = SYNDROME_TO_ERROR.get(syndrome)
                correct_index = error_pos_1based - 1 if error_pos_1based else -1
                
                if player_guess == correct_index:
                    print("\n✅ CORRECT! You successfully identified and corrected the error.")
                    print(f"Syndrome {syndrome} correctly maps to error location (1-based) {error_pos_1based}.")
                else:
                    print(f"\n❌ INCORRECT. The syndrome {syndrome} means the error is at index {correct_index}.")
                    print(f"Your guess was index {player_guess}. Try again!")
                
                print(f"\n[ORIGINAL CODEWORD]: {list(self.codeword)}")
                
            else:
                print("Invalid input. Please enter an index between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# --- Execution ---
if __name__ == "__main__":
    # Ensure numpy is installed: pip install numpy
    game = HammingGame()
    game.start_game()