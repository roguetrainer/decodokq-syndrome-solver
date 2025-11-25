import numpy as np
from abc import ABC, abstractmethod
from typing import List, Tuple

# --- Module 1: Code Abstraction (CodeDefinition Class) ---
# This abstract base class ensures all new codes (Qudit, Toric, Color, etc.)
# adhere to a standard interface for essential parameters.
class CodeDefinition(ABC):
    """
    Abstract Base Class for all Quantum Error Correction Codes (QECCs)
    to enforce modularity and standardized access to code parameters.
    """
    def __init__(self, d: int, L: int):
        """
        :param d: Dimension of the underlying quantum system (qudit dimension).
                  d=2 for qubits (Toric/Surface/Color Codes).
                  d>2 for qudits (Original Decodoku codes, e.g., d=10).
        :param L: Lattice size or code distance parameter.
        """
        self.d = d
        self.L = L

    @property
    @abstractmethod
    def n_physical(self) -> int:
        """Total number of physical qudits/qubits in the code."""
        pass

    @property
    @abstractmethod
    def k_logical(self) -> int:
        """Total number of encoded logical qubits."""
        pass

    @property
    @abstractmethod
    def distance(self) -> int:
        """The minimum distance of the code (d_min)."""
        pass

    @abstractmethod
    def get_stabilizer_matrix(self) -> np.ndarray:
        """
        Returns the generalized Parity Check Matrix (H) or Stabilizer Generator Matrix (S).
        The structure and arithmetic depend on 'd' (field dimension).
        """
        pass

    @abstractmethod
    def get_topology(self) -> str:
        """Describes the geometric support of the code (e.g., 'Planar', 'Toroidal')."""
        pass


# --- Example Implementation: The Original Qudit Surface Code (d > 2) ---
class QuditSurfaceCode(CodeDefinition):
    """
    Implementation of the original Decodoku-style Qudit Code (additive checks mod d).
    Placeholder implementation for demonstration.
    """
    def __init__(self, d=10, L=3):
        super().__init__(d, L)

    @property
    def n_physical(self) -> int:
        return 2 * self.L**2

    @property
    def k_logical(self) -> int:
        return 1

    @property
    def distance(self) -> int:
        return self.L

    def get_stabilizer_matrix(self) -> np.ndarray:
        # In the original Decodoku, this matrix represents the local qudit indices
        # involved in the modular sum check for each plaquette.
        # Placeholder: 8 checks acting on 18 qudits for L=3 surface code geometry.
        return np.random.randint(0, self.d, size=(8, self.n_physical))

    def get_topology(self) -> str:
        return "Planar Grid (Qudit)"


# --- Module 2: Generalized Stabilizer Check Logic ---
# This module handles the field-specific syndrome calculation.
def calculate_syndrome(code: CodeDefinition, error_vector: np.ndarray) -> np.ndarray:
    """
    Calculates the syndrome vector (s) based on the code's definition and an applied error vector (e).
    The operation is generalized to handle Z2 (qubit) or Zd (qudit) arithmetic.

    Syndrome s = H @ e (with appropriate modular arithmetic).

    :param code: An instance of a CodeDefinition subclass.
    :param error_vector: A 1D numpy array representing the error (e).
    :return: The syndrome vector (s).
    """
    H = code.get_stabilizer_matrix()

    # The core operation: Syndrome = H * Error (performed over the specific field F_d)
    syndrome = H @ error_vector

    # Apply modular arithmetic based on the code dimension 'd'
    if code.d == 2:
        # Z2 (binary) arithmetic for standard qubit CSS codes (Pauli commutation checks)
        # Note: For full QEC, the matrix H should be split into Hx and Hz.
        # Here we model the simplest linear code check (bit-flip component)
        return syndrome % 2
    
    elif code.d > 2:
        # Zd (modular) arithmetic for qudit codes (e.g., d=10 in Decodoku)
        # Check if the modular sum is zero (or non-zero, indicating a syndrome event)
        return syndrome % code.d
    
    else:
        raise ValueError("Code dimension 'd' must be >= 2.")


# --- Module 3: Toric Code (Qubit) Example Implementation ---
class ToricCode(CodeDefinition):
    """
    Implementation of the Toric Code (Z2 qubit stabilizer code) defined on a torus.
    This demonstrates the Z2 functionality required for expansion.
    """
    def __init__(self, L=3):
        # Toric Code uses qubits (d=2) and encodes k=2 logical qubits.
        super().__init__(d=2, L=L)
        # Note: A proper implementation would define Hx and Hz matrices.

    @property
    def n_physical(self) -> int:
        # L x L Toric code has 2L^2 qubits on the edges of the grid.[1]
        return 2 * self.L**2

    @property
    def k_logical(self) -> int:
        # Toric code encodes 2 logical qubits.[1]
        return 2

    @property
    def distance(self) -> int:
        # Distance is L.[1]
        return self.L

    def get_stabilizer_matrix(self) -> np.ndarray:
        # This function would construct the 2D lattice graph and generate the
        # stabilizer matrix (Hx and Hz combined) based on vertex and plaquette checks.[2]
        # Placeholder for demonstration of the required interface:
        n_checks = 2 * (self.L**2 - 1)  # Simplified: (L^2 X-checks + L^2 Z-checks) - 2
        return np.random.randint(0, 2, size=(n_checks, self.n_physical))

    def get_topology(self) -> str:
        return "Toroidal Grid (Qubit)"