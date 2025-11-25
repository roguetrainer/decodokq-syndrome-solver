import numpy as np
from abc import ABC, abstractmethod
import random
from typing import List, Dict, Tuple

# Constants for QEC Operations (reused)
PAULI_I = np.array([[1, 0], [0, 1]], dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
# ... other PAULI constants ...

# --- QubitRegister Class (Updated with location and probing state) ---
class QubitRegister:
    """Represents a single physical qubit in the game."""
    def __init__(self, index: int, location: Tuple[int, int] = (0, 0)):
        self.index = index
        self.location = location # (x, y) coordinates for potential Surface Code use
        self.current_error_pauli = 'I'
        self.is_highlighted = False      # For showing error/correction targets
        self.is_probed = False           # NEW: For highlighting during stabilizer probing
    
    def apply_pauli(self, pauli_op: str):
        """Applies a Pauli operator to this qubit's internal error state."""
        current = self.current_error_pauli
        
        # ... (Pauli multiplication logic remains the same) ...
        
        if pauli_op == 'I': return
        if pauli_op == current: self.current_error_pauli = 'I'
        elif current == 'I': self.current_error_pauli = pauli_op
        elif (current == 'X' and pauli_op == 'Z') or (current == 'Z' and pauli_op == 'X'): self.current_error_pauli = 'Y'
        elif (current == 'X' and pauli_op == 'Y') or (current == 'Y' and pauli_op == 'X'): self.current_error_pauli = 'Z'
        elif (current == 'Z' and pauli_op == 'Y') or (current == 'Y' and pauli_op == 'Z'): self.current_error_pauli = 'X'
        else: self.current_error_pauli = pauli_op # Fallback for complex ops

    def get_pauli_representation(self) -> str:
        return self.current_error_pauli
            
# --- Stabilizer Class (Reusable, includes definition and type) ---
class Stabilizer:
    """Represents a single stabilizer operator."""
    def __init__(self, definition_string: str, stype: str, index: int):
        self.definition_string = definition_string
        self.stype = stype 
        self.index = index
        self.measured_value = +1 # +1 (satisfied) or -1 (violated/syndrome)

    def measure(self, qubits: List[QubitRegister]) -> int:
        """Measures this stabilizer against the current error state."""
        anti_commutations = 0
        for i, (stabilizer_pauli, qubit) in enumerate(zip(self.definition_string, qubits)):
            error_pauli = qubit.get_pauli_representation()
            
            if stabilizer_pauli == 'I': continue
            
            # Simple anti-commutation check: Z stab detects X/Y errors; X stab detects Z/Y errors.
            if self.stype == 'Z' and (error_pauli == 'X' or error_pauli == 'Y'):
                anti_commutations += 1
            elif self.stype == 'X' and (error_pauli == 'Z' or error_pauli == 'Y'):
                anti_commutations += 1
        
        self.measured_value = -1 if anti_commutations % 2 != 0 else +1
        return self.measured_value
        
    def get_qubit_indices(self) -> List[int]:
        """Returns the indices of qubits involved in this stabilizer's check."""
        return [i for i, pauli in enumerate(self.definition_string) if pauli != 'I']

# --- QuantumCode Abstraction (Remains the same) ---
class QuantumCode(ABC):
    # ... (properties N, K, stabilizer_definitions, encode remain) ...
    @property
    @abstractmethod
    def N(self) -> int: pass
    @property
    @abstractmethod
    def K(self) -> int: pass
    @property
    @abstractmethod
    def stabilizer_definitions(self) -> List[Tuple[str, str]]: pass
    @abstractmethod
    def encode(self, logical_state: np.ndarray) -> np.ndarray: pass
    
# --- QECGameEngine (Updated with probe logic) ---
class QECGameEngine:
    """The main reusable engine providing core functionality."""
    def __init__(self, code: QuantumCode):
        self.code = code
        # Initialize qubits with placeholder locations
        self.qubits: List[QubitRegister] = [QubitRegister(i, location=(i % 4, i // 4)) for i in range(code.N)]
        
        # Initialize Stabilizer objects
        self.stabilizers: List[Stabilizer] = []
        for i, (def_str, stype) in enumerate(code.stabilizer_definitions):
            self.stabilizers.append(Stabilizer(def_str, stype, i))
        
        self.probed_stabilizer_index = -1 # Tracks which stabilizer is currently being probed

    def introduce_error(self) -> str:
        # Clears previous error, applies new single Pauli error, and updates qubit object.
        for q in self.qubits: q.current_error_pauli = 'I'
        qubit_index = random.randint(0, self.code.N - 1)
        error_type = random.choice(['X', 'Y', 'Z'])
        self.qubits[qubit_index].apply_pauli(error_type)
        return self.get_qubit_error_string()

    def get_current_syndrome_string(self) -> str:
        # Measures all stabilizers and returns their values as a single syndrome string.
        syndrome_values = []
        for stab in self.stabilizers:
            stab.measure(self.qubits)
            syndrome_values.append('0' if stab.measured_value == +1 else '1')
        return "".join(syndrome_values)

    def apply_correction(self, correction_string: str):
        # Applies a correction string to the qubits.
        for i, pauli_op in enumerate(correction_string):
            if pauli_op != 'I':
                self.qubits[i].apply_pauli(pauli_op)

    def get_qubit_error_string(self) -> str:
        """Returns the current accumulated error on the physical register as a string."""
        return "".join([q.get_pauli_representation() for q in self.qubits])
        
    def probe_stabilizer(self, stab_index: int):
        """
        NEW: Sets the visual state for stabilizer probing (the 'joystick' action).
        This method dictates what the UI should highlight.
        """
        if not (0 <= stab_index < len(self.stabilizers)):
            print(f"Error: Stabilizer index {stab_index} is out of bounds.")
            self.probed_stabilizer_index = -1
            for q in self.qubits: q.is_probed = False
            return
            
        self.probed_stabilizer_index = stab_index
        probed_stab = self.stabilizers[stab_index]
        qubits_involved = probed_stab.get_qubit_indices()

        print(f"--- Probing Stabilizer S{stab_index} ({probed_stab.stype} type) ---")
        print(f"Qubits involved (indices): {qubits_involved}")
        print(f"Current measurement value: {'+1 (Satisfied)' if probed_stab.measured_value == 1 else '-1 (Violated)'}")
        
        # Update the is_probed flag for visualization
        for i, q in enumerate(self.qubits):
            q.is_probed = i in qubits_involved


# --- Steane Code Implementation (Code Reuse/Extension) ---
class SteaneCode(QuantumCode):
    @property
    def N(self): return 7
    @property
    def K(self): return 1
    
    @property
    def stabilizer_definitions(self) -> List[Tuple[str, str]]:
        # Note: The indices (0-6) of the string map to QubitRegister indices.
        # This list of 6 stabilizers defines the code's geometry/Fano Plane checks.
        Z_stabs = ["ZIZIZII", "IZZIIZI", "IIZZZII"]
        X_stabs = ["XIXIXII", "IXXIIXI", "IIXXZIX"]
        return [(s, "Z") for s in Z_stabs] + [(s, "X") for s in X_stabs]
        
    def encode(self, logical_state: np.ndarray) -> np.ndarray:
        return np.zeros(2**7)

# --- Example Game Play ---
def run_steane_game_example_with_classes():
    print("--- QEC Engine: Steane Code Demonstration (Probing) ---")
    
    engine = QECGameEngine(SteaneCode())
    
    # 1. Setup an error
    engine.introduce_error()
    engine.get_current_syndrome_string() # Calculate syndrome, updates stab.measured_value
    
    print(f"Current Error State: {engine.get_qubit_error_string()}")
    print(f"Full Syndrome: {engine.get_current_syndrome_string()}")
    
    # 2. Player uses the "joystick" to probe S_Z2 (index 1)
    engine.probe_stabilizer(stab_index=1)
    
    # The game visualization would now:
    # - Highlight stabilizer index 1.
    # - Highlight qubits 0, 2, 4, 6 (based on its definition 'ZIZIZII').
    print("\nVisual Hint: Qubits with 'is_probed = True' should be highlighted now.")
    print([q.index for q in engine.qubits if q.is_probed])

    # 3. Player probes S_X3 (index 5)
    engine.probe_stabilizer(stab_index=5)
    print("\nVisual Hint: Now probing S_X3.")
    print([q.index for q in engine.qubits if q.is_probed])

if __name__ == "__main__":
    run_steane_game_example_with_classes()