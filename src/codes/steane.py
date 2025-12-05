"""
Steane [[7,1,3]] Quantum Error Correction Code

The Steane code is a CSS code based on the classical Hamming (7,4) code.
It encodes 1 logical qubit into 7 physical qubits and can correct any single-qubit error.

Geometry: The Steane code is built on Fano plane geometry (PG(2,2) over F_2).
The 7 physical qubits correspond to the 7 points of the Fano plane.
"""

import numpy as np
from typing import List, Tuple, Dict, Optional
import random


class SteaneCode:
    """
    Steane [[7,1,3]] quantum error correction code based on Fano plane geometry.

    The code uses 6 stabilizer generators (3 X-type and 3 Z-type) derived from
    the Hamming (7,4) parity check matrix.
    """

    def __init__(self):
        self.n = 7  # Number of physical qubits
        self.k = 1  # Number of logical qubits
        self.d = 3  # Code distance

        # Fano plane structure: 7 points, 7 lines
        # Points labeled 1-7 (binary: 001, 010, 011, 100, 101, 110, 111)
        self.points = list(range(7))

        # Hamming (7,4) parity check matrix H
        # Columns are binary representations 1-7
        self.H = np.array([
            [0, 0, 0, 1, 1, 1, 1],  # Check 1: positions 4,5,6,7 (indices 3,4,5,6)
            [0, 1, 1, 0, 0, 1, 1],  # Check 2: positions 2,3,6,7 (indices 1,2,5,6)
            [1, 0, 1, 0, 1, 0, 1]   # Check 3: positions 1,3,5,7 (indices 0,2,4,6)
        ], dtype=int)

        # The 7 lines of the Fano plane (each line contains 3 points)
        # These are the 3-qubit subsets where XOR = 0
        self.fano_lines = [
            [0, 2, 4],  # Line through points 1,3,5 (001, 011, 101)
            [1, 2, 6],  # Line through points 2,3,7 (010, 011, 111)
            [0, 1, 3],  # Line through points 1,2,4 (001, 010, 100)
            [4, 5, 6],  # Line through points 5,6,7 (101, 110, 111)
            [2, 3, 5],  # Line through points 3,4,6 (011, 100, 110)
            [0, 5, 6],  # Line through points 1,6,7 (001, 110, 111)
            [1, 3, 4],  # Line through points 2,4,5 (010, 100, 101)
        ]

        # For Steane code: stabilizers are complements of Fano lines (4-qubit checks)
        # X-type stabilizers (bit-flip detection)
        self.stabilizers_X = self._compute_stabilizers()
        # Z-type stabilizers (phase-flip detection) - same structure
        self.stabilizers_Z = self._compute_stabilizers()

        # Pauli operators
        self.pauli_types = ['I', 'X', 'Y', 'Z']

    def _compute_stabilizers(self) -> List[List[int]]:
        """
        Compute 6 stabilizer generators from the Hamming parity check matrix.

        For the Steane code, we use 3 stabilizers from H (X-type) and
        3 stabilizers from H (Z-type). Each row of H gives a 4-qubit stabilizer.

        Returns:
            List of stabilizer qubit indices
        """
        stabilizers = []
        for row in self.H:
            # Find indices where row has 1's (these are the qubits in the stabilizer)
            stabilizer_qubits = [i for i, val in enumerate(row) if val == 1]
            stabilizers.append(stabilizer_qubits)
        return stabilizers

    def get_all_stabilizers(self) -> Dict[str, List[List[int]]]:
        """Get all stabilizer generators with their types."""
        return {
            'X': self.stabilizers_X,
            'Z': self.stabilizers_Z
        }

    def compute_syndrome(self, error: np.ndarray, error_type: str = 'X') -> np.ndarray:
        """
        Compute the syndrome for a given error pattern.

        Args:
            error: Binary vector of length 7 indicating error locations
            error_type: 'X' for bit-flip or 'Z' for phase-flip

        Returns:
            Syndrome vector (length 3)
        """
        # Syndrome is H @ error (mod 2)
        syndrome = (self.H @ error) % 2
        return syndrome

    def syndrome_to_error_location(self, syndrome: np.ndarray) -> Optional[int]:
        """
        Decode syndrome to find error location.

        The syndrome is the binary representation of the error position (1-7).
        Syndrome = 0 means no error.

        Args:
            syndrome: 3-bit syndrome vector

        Returns:
            Error location (0-6) or None if no error
        """
        # Convert syndrome to decimal
        syndrome_value = syndrome[0] + 2*syndrome[1] + 4*syndrome[2]

        if syndrome_value == 0:
            return None

        # Syndrome points directly to error location (1-indexed)
        # We return 0-indexed
        return syndrome_value - 1

    def apply_random_error(self, error_type: str = 'X',
                          num_errors: int = 1) -> Tuple[np.ndarray, List[int]]:
        """
        Generate a random error pattern.

        Args:
            error_type: 'X', 'Z', or 'Y'
            num_errors: Number of qubits to have errors (1-7)

        Returns:
            Tuple of (error_vector, error_locations)
        """
        error_vector = np.zeros(7, dtype=int)
        error_locations = random.sample(range(7), num_errors)

        for loc in error_locations:
            error_vector[loc] = 1

        return error_vector, error_locations

    def get_fano_line_complement(self, line_idx: int) -> List[int]:
        """
        Get the complement of a Fano line (forms a 4-qubit stabilizer).

        Args:
            line_idx: Index of the Fano line (0-6)

        Returns:
            List of qubit indices in the complement
        """
        line = self.fano_lines[line_idx]
        complement = [i for i in range(7) if i not in line]
        return complement

    def visualize_error(self, error_locations: List[int]) -> str:
        """
        Create a text visualization of errors on the 7 qubits.

        Args:
            error_locations: List of qubit indices with errors

        Returns:
            String representation
        """
        visual = []
        for i in range(7):
            if i in error_locations:
                visual.append(f"Q{i}[X]")
            else:
                visual.append(f"Q{i}[ ]")
        return " ".join(visual)

    def get_stabilizer_measurement(self, error: np.ndarray,
                                   stabilizer_type: str = 'X') -> List[int]:
        """
        Measure all stabilizers and return their outcomes.

        Args:
            error: Error vector
            stabilizer_type: 'X' or 'Z'

        Returns:
            List of stabilizer measurement outcomes (0 or 1 for each stabilizer)
        """
        stabilizers = self.stabilizers_X if stabilizer_type == 'X' else self.stabilizers_Z
        measurements = []

        for stabilizer_qubits in stabilizers:
            # Measure parity of error on stabilizer qubits
            parity = sum(error[q] for q in stabilizer_qubits) % 2
            measurements.append(parity)

        return measurements

    def describe_geometry(self) -> str:
        """Return a description of the Fano plane geometry."""
        desc = "FANO PLANE GEOMETRY (Steane Code)\n"
        desc += "="*50 + "\n\n"
        desc += "7 Points (Qubits): 0, 1, 2, 3, 4, 5, 6\n"
        desc += "Corresponding to binary: 001, 010, 011, 100, 101, 110, 111\n\n"
        desc += "7 Lines (3-qubit subsets where XOR = 0):\n"
        for i, line in enumerate(self.fano_lines):
            desc += f"  Line {i}: {line}\n"
        desc += "\n"
        desc += "6 Stabilizers (4-qubit checks, complements of certain lines):\n"
        for i, stab in enumerate(self.stabilizers_X):
            desc += f"  X-Stabilizer {i}: {stab}\n"
        return desc


class SteaneGame:
    """
    Interactive game for learning Steane code syndrome decoding.

    Players must identify error locations based on syndrome measurements.
    """

    def __init__(self):
        self.code = SteaneCode()
        self.score = 0
        self.rounds_played = 0

    def play_round(self, num_errors: int = 1) -> Dict:
        """
        Play one round of the syndrome decoding game.

        Args:
            num_errors: Number of errors to introduce

        Returns:
            Dictionary with round information
        """
        # Generate random error
        error_vector, true_locations = self.code.apply_random_error(
            error_type='X',
            num_errors=num_errors
        )

        # Compute syndrome
        syndrome = self.code.compute_syndrome(error_vector)

        # Get stabilizer measurements
        stabilizer_measurements = self.code.get_stabilizer_measurement(error_vector)

        round_info = {
            'error_vector': error_vector,
            'true_locations': true_locations,
            'syndrome': syndrome,
            'syndrome_decimal': syndrome[0] + 2*syndrome[1] + 4*syndrome[2],
            'stabilizer_measurements': stabilizer_measurements,
            'visualization': self.code.visualize_error(true_locations)
        }

        self.rounds_played += 1
        return round_info

    def check_answer(self, guess: int, true_location: int) -> bool:
        """
        Check if the player's guess is correct.

        Args:
            guess: Player's guessed error location
            true_location: Actual error location

        Returns:
            True if correct
        """
        correct = (guess == true_location)
        if correct:
            self.score += 1
        return correct

    def get_stats(self) -> Dict:
        """Get game statistics."""
        return {
            'score': self.score,
            'rounds_played': self.rounds_played,
            'accuracy': self.score / self.rounds_played if self.rounds_played > 0 else 0
        }

    def print_hint(self, syndrome: np.ndarray):
        """Print a hint about syndrome decoding."""
        syndrome_value = syndrome[0] + 2*syndrome[1] + 4*syndrome[2]
        print(f"\nHINT: The syndrome {syndrome} in binary equals {syndrome_value} in decimal.")
        print(f"For the Steane/Hamming code, the syndrome directly points to the error location.")
        print(f"Syndrome value {syndrome_value} means the error is at qubit {syndrome_value-1} (0-indexed).")
