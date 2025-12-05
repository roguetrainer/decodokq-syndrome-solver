#!/usr/bin/env python3
"""
Simple standalone demo of the Reed-Muller Code game.
Run this script to explore the tetrahedral geometry.

Usage:
    python simple_reed_muller_demo.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.codes.reed_muller import ReedMullerCode, ReedMullerGame
import numpy as np


def print_separator():
    print("=" * 70)


def demo_geometry():
    """Demonstrate the tetrahedral geometry."""
    print_separator()
    print("REED-MULLER CODE GEOMETRY DEMO")
    print_separator()

    code = ReedMullerCode(use_extended=True)
    print(code.describe_geometry())
    print()


def demo_qubit_mapping():
    """Show the detailed qubit-to-geometry mapping."""
    print_separator()
    print("QUBIT-TO-GEOMETRY MAPPING")
    print_separator()
    print()

    code = ReedMullerCode(use_extended=True)

    print("VERTICES (4 qubits):")
    for i in range(4):
        desc = code.get_geometric_description(i)
        mapping = code.qubit_to_geometry[i]
        pos = mapping['position']
        print(f"  Qubit {i:2d}: {desc:20s} Position: ({pos[0]:+2.0f}, {pos[1]:+2.0f}, {pos[2]:+2.0f})")

    print("\nEDGES (6 qubits):")
    for i in range(4, 10):
        desc = code.get_geometric_description(i)
        print(f"  Qubit {i:2d}: {desc}")

    print("\nFACES (4 qubits):")
    for i in range(10, 14):
        desc = code.get_geometric_description(i)
        print(f"  Qubit {i:2d}: {desc}")

    print("\nINTERIOR (1 qubit):")
    desc = code.get_geometric_description(14)
    print(f"  Qubit 14: {desc}")
    print()


def demo_error_on_different_elements():
    """Show how errors on different geometric elements appear."""
    print_separator()
    print("ERRORS ON DIFFERENT GEOMETRIC ELEMENTS")
    print_separator()
    print()

    code = ReedMullerCode(use_extended=True)

    test_qubits = [
        (1, "Vertex 1"),
        (5, "Edge 0-2"),
        (11, "Face (0,1,3)"),
        (14, "Interior")
    ]

    for qubit, description in test_qubits:
        error_vector = np.zeros(15, dtype=int)
        error_vector[qubit] = 1

        syndrome = code.compute_syndrome(error_vector)

        print(f"Error on Qubit {qubit:2d} ({description}):")
        print(f"  Syndrome: {syndrome}")
        print(f"  Geometric: {code.get_geometric_description(qubit)}")
        print()


def demo_tetrahedral_structure():
    """Show the complete tetrahedral structure."""
    print_separator()
    print("TETRAHEDRAL STRUCTURE DETAILS")
    print_separator()
    print()

    code = ReedMullerCode(use_extended=True)
    structure = code.get_tetrahedral_structure()

    print("VERTICES:")
    for i, vertex in enumerate(structure['vertices']):
        print(f"  Vertex {i}: {vertex}")

    print(f"\nEDGES (total: {len(structure['edges'])}):")
    for i, edge in enumerate(structure['edges']):
        print(f"  Edge {i} (Qubit {4+i}): Connects vertices {edge}")

    print(f"\nFACES (total: {len(structure['faces'])}):")
    for i, face in enumerate(structure['faces']):
        print(f"  Face {i} (Qubit {10+i}): Vertices {face}")

    print()


def play_interactive_rounds(num_rounds=3):
    """Play several rounds of the game."""
    print_separator()
    print(f"PLAYING {num_rounds} ROUNDS")
    print_separator()
    print()

    game = ReedMullerGame(use_extended=True)

    for i in range(num_rounds):
        print(f"\n--- ROUND {i+1} ---")

        # Generate error
        round_info = game.play_round(num_errors=1)

        print(f"Syndrome: {round_info['syndrome']}")
        print()
        print("Error location:")
        print(f"  Qubit: {round_info['true_locations'][0]}")
        print(f"  Geometric element: {round_info['geometric_descriptions'][0]}")
        print()
        print("Visualization:")
        print(round_info['visualization'])

    print()
    print_separator()
    print(f"Completed {num_rounds} rounds")
    print_separator()
    print()


def compare_8_and_15_qubit_versions():
    """Compare the standard 8-qubit and extended 15-qubit versions."""
    print_separator()
    print("COMPARING 8-QUBIT vs 15-QUBIT VERSIONS")
    print_separator()
    print()

    # 8-qubit version
    code_8 = ReedMullerCode(use_extended=False)
    print("8-QUBIT VERSION (Standard RM(1,3)):")
    print(f"  Number of qubits: {code_8.n}")
    print(f"  Generator matrix shape: {code_8.G.shape}")
    print(f"  Represents 2^3 = 8 points in 3D space (cube vertices)")
    print()

    # 15-qubit version
    code_15 = ReedMullerCode(use_extended=True)
    print("15-QUBIT VERSION (Extended/Quantum):")
    print(f"  Number of qubits: {code_15.n}")
    print(f"  Generator matrix shape: {code_15.G.shape}")
    print(f"  Geometric elements: 4 vertices + 6 edges + 4 faces + 1 interior = 15")
    print()


def main():
    """Run all demonstrations."""
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 17 + "REED-MULLER CODE DEMO" + " " * 30 + "║")
    print("║" + " " * 18 + "Tetrahedral Geometry" + " " * 31 + "║")
    print("╚" + "═" * 68 + "╝")
    print()

    # Run demonstrations
    demo_geometry()
    input("Press Enter to continue...")

    demo_qubit_mapping()
    input("Press Enter to continue...")

    demo_tetrahedral_structure()
    input("Press Enter to continue...")

    demo_error_on_different_elements()
    input("Press Enter to continue...")

    compare_8_and_15_qubit_versions()
    input("Press Enter to continue...")

    play_interactive_rounds(num_rounds=3)

    print()
    print("Demo complete! Try the Jupyter notebook for more interactivity:")
    print("  jupyter notebook examples/reed_muller_game_demo.ipynb")
    print()


if __name__ == "__main__":
    main()
