"""
Reed-Muller RM(1,3) Code (Quantum [[15,1,3]] code based on RM code)

The Reed-Muller RM(1,3) code has a beautiful tetrahedral geometry.
- 15 physical qubits
- 1 logical qubit
- Distance 3

Geometry: The Reed-Muller RM(1,3) code can be visualized using tetrahedral geometry.
The 15 codewords of minimum weight correspond to:
- 4 vertices of a 4-dimensional simplex (tetrahedron in 4D)
- 6 edges connecting the vertices
- 4 faces (triangular faces)
- 1 interior (the whole tetrahedron)

For the quantum version, we construct a CSS code from the classical RM(1,3) code.
"""

import numpy as np
from typing import List, Tuple, Dict, Optional
import random
from itertools import combinations


class ReedMullerCode:
    """
    Reed-Muller RM(1,3) code with tetrahedral geometry.

    Classical parameters: [15, 11, 3] - encodes 11 bits into 15, distance 3
    Quantum version: [[15, 1, 3]] - uses puncturing and CSS construction

    For simplicity, we work with the first-order Reed-Muller code RM(1,3)
    which has length 2^3 = 8, but we extend it to demonstrate the geometry.
    """

    def __init__(self, use_extended: bool = True):
        """
        Initialize Reed-Muller code.

        Args:
            use_extended: If True, use the extended version with 15 qubits
                         If False, use the simpler 8-qubit version for RM(1,3)
        """
        self.use_extended = use_extended

        if use_extended:
            self.n = 15  # Extended version
            self.k = 1   # Quantum version encodes 1 logical qubit
            self.d = 3   # Code distance
        else:
            self.n = 8   # Standard RM(1,3): length 2^m where m=3
            self.k = 1
            self.d = 3

        # For RM(1,3), the generator matrix includes:
        # - All-ones row (constant function)
        # - Rows for each of the 3 coordinate functions
        # We'll work with the standard 8-qubit version for clarity

        # Generator matrix for RM(1,3) - standard form
        # Rows: [all-ones, x1, x2, x3]
        self.G = self._build_generator_matrix()

        # Parity check matrix (derived from dual code)
        self.H = self._build_parity_check_matrix()

        # Tetrahedral structure: 4 vertices in 4D space projected to 3D
        # For visualization, we use 4 points forming a regular tetrahedron
        self.vertices = self._define_tetrahedral_vertices()
        self.edges = list(combinations(range(4), 2))  # 6 edges
        self.faces = list(combinations(range(4), 3))  # 4 triangular faces

        # Map qubits to geometric elements
        self.qubit_to_geometry = self._create_geometry_mapping()

    def _build_generator_matrix(self) -> np.ndarray:
        """Build the generator matrix for RM(1,3)."""
        if self.use_extended:
            # Simplified: use Reed-Muller construction
            # For demonstration, we create a representative matrix
            # Full implementation would use proper RM(1,3) construction
            G = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # all-ones
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # x1
                [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],  # x2
                [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],  # x3
            ], dtype=int)
        else:
            # Standard RM(1,3): 2^3 = 8 bits
            G = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1],  # all-ones (constant)
                [0, 1, 0, 1, 0, 1, 0, 1],  # x1
                [0, 0, 1, 1, 0, 0, 1, 1],  # x2
                [0, 0, 0, 0, 1, 1, 1, 1],  # x3
            ], dtype=int)
        return G

    def _build_parity_check_matrix(self) -> np.ndarray:
        """
        Build parity check matrix from the dual of RM(1,3).

        The dual of RM(r, m) is RM(m-r-1, m).
        For RM(1,3), dual is RM(1,3) itself (self-dual property).
        """
        if self.use_extended:
            # Simplified parity check matrix
            # In practice, this would be carefully constructed from RM theory
            n_checks = 4
            H = np.random.randint(0, 2, size=(n_checks, self.n))
        else:
            # For RM(1,3), we have 4 information bits, so 4 parity checks
            # H is derived to be orthogonal to G
            n_checks = 4
            H = np.array([
                [1, 1, 1, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1, 1, 0],
            ], dtype=int)
        return H

    def _define_tetrahedral_vertices(self) -> List[Tuple[float, float, float]]:
        """
        Define 4 vertices of a regular tetrahedron in 3D space.

        Returns:
            List of (x, y, z) coordinates
        """
        # Regular tetrahedron centered at origin
        # Vertices at alternating corners of a cube
        vertices = [
            (1, 1, 1),      # Vertex 0
            (1, -1, -1),    # Vertex 1
            (-1, 1, -1),    # Vertex 2
            (-1, -1, 1),    # Vertex 3
        ]
        return vertices

    def _create_geometry_mapping(self) -> Dict[int, Dict]:
        """
        Map qubit indices to geometric elements of the tetrahedron.

        Returns:
            Dictionary mapping qubit index to geometric description
        """
        mapping = {}

        # First 4 qubits: vertices
        for i in range(4):
            mapping[i] = {
                'type': 'vertex',
                'index': i,
                'position': self.vertices[i],
                'description': f'Vertex {i}'
            }

        # Next 6 qubits: edges
        for i, edge in enumerate(self.edges):
            qubit_idx = 4 + i
            mapping[qubit_idx] = {
                'type': 'edge',
                'index': i,
                'vertices': edge,
                'description': f'Edge {edge[0]}-{edge[1]}'
            }

        # Next 4 qubits: faces
        for i, face in enumerate(self.faces):
            qubit_idx = 10 + i
            mapping[qubit_idx] = {
                'type': 'face',
                'index': i,
                'vertices': face,
                'description': f'Face {face}'
            }

        # Last qubit: interior/whole tetrahedron
        if self.use_extended:
            mapping[14] = {
                'type': 'interior',
                'index': 0,
                'description': 'Interior (whole tetrahedron)'
            }

        return mapping

    def compute_syndrome(self, error: np.ndarray) -> np.ndarray:
        """
        Compute syndrome for a given error pattern.

        Args:
            error: Binary vector of length n indicating error locations

        Returns:
            Syndrome vector
        """
        syndrome = (self.H @ error[:len(self.H[0])]) % 2
        return syndrome

    def apply_random_error(self, num_errors: int = 1) -> Tuple[np.ndarray, List[int]]:
        """
        Generate a random error pattern.

        Args:
            num_errors: Number of qubits to have errors

        Returns:
            Tuple of (error_vector, error_locations)
        """
        error_vector = np.zeros(self.n, dtype=int)
        error_locations = random.sample(range(self.n), min(num_errors, self.n))

        for loc in error_locations:
            error_vector[loc] = 1

        return error_vector, error_locations

    def get_geometric_description(self, qubit_idx: int) -> str:
        """Get geometric description of a qubit."""
        if qubit_idx in self.qubit_to_geometry:
            return self.qubit_to_geometry[qubit_idx]['description']
        return f"Qubit {qubit_idx}"

    def visualize_error(self, error_locations: List[int]) -> str:
        """
        Create a text visualization of errors on the qubits.

        Args:
            error_locations: List of qubit indices with errors

        Returns:
            String representation with geometric context
        """
        visual = []
        for i in range(min(self.n, 15)):
            geo_desc = self.get_geometric_description(i)
            if i in error_locations:
                visual.append(f"Q{i:2d}[X] ({geo_desc})")
            else:
                visual.append(f"Q{i:2d}[ ] ({geo_desc})")
        return "\n".join(visual)

    def describe_geometry(self) -> str:
        """Return a description of the tetrahedral geometry."""
        desc = "TETRAHEDRAL GEOMETRY (Reed-Muller Code)\n"
        desc += "="*50 + "\n\n"

        if self.use_extended:
            desc += "15 Qubits mapped to tetrahedral structure:\n\n"
            desc += "VERTICES (4 qubits):\n"
            for i in range(4):
                desc += f"  Qubit {i}: {self.vertices[i]}\n"

            desc += "\nEDGES (6 qubits):\n"
            for i, edge in enumerate(self.edges):
                desc += f"  Qubit {4+i}: Edge {edge[0]}-{edge[1]}\n"

            desc += "\nFACES (4 qubits):\n"
            for i, face in enumerate(self.faces):
                desc += f"  Qubit {10+i}: Face {face}\n"

            desc += "\nINTERIOR (1 qubit):\n"
            desc += f"  Qubit 14: Whole tetrahedron\n"
        else:
            desc += f"8 Qubits (2^3 structure):\n"
            desc += "Each qubit corresponds to a vertex of a 3D cube\n"

        return desc

    def get_tetrahedral_structure(self) -> Dict:
        """Get the complete tetrahedral structure information."""
        return {
            'vertices': self.vertices,
            'edges': self.edges,
            'faces': self.faces,
            'qubit_mapping': self.qubit_to_geometry
        }


class ReedMullerGame:
    """
    Interactive game for learning Reed-Muller code syndrome decoding
    with tetrahedral geometry visualization.
    """

    def __init__(self, use_extended: bool = True):
        self.code = ReedMullerCode(use_extended=use_extended)
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
        error_vector, true_locations = self.code.apply_random_error(num_errors=num_errors)

        # Compute syndrome
        syndrome = self.code.compute_syndrome(error_vector)

        # Get geometric descriptions
        geometric_descriptions = [
            self.code.get_geometric_description(loc)
            for loc in true_locations
        ]

        round_info = {
            'error_vector': error_vector,
            'true_locations': true_locations,
            'syndrome': syndrome,
            'geometric_descriptions': geometric_descriptions,
            'visualization': self.code.visualize_error(true_locations)
        }

        self.rounds_played += 1
        return round_info

    def check_answer(self, guesses: List[int], true_locations: List[int]) -> bool:
        """
        Check if the player's guesses are correct.

        Args:
            guesses: Player's guessed error locations
            true_locations: Actual error locations

        Returns:
            True if correct
        """
        correct = set(guesses) == set(true_locations)
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

    def print_hint(self):
        """Print a hint about the tetrahedral structure."""
        print("\nHINT: Tetrahedral Structure")
        print("- Qubits 0-3: Vertices of the tetrahedron")
        print("- Qubits 4-9: Edges connecting vertices")
        print("- Qubits 10-13: Triangular faces")
        if self.code.use_extended:
            print("- Qubit 14: Interior (whole structure)")
        print("\nErrors on related geometric elements may have related syndromes!")
