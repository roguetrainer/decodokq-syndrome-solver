#!/usr/bin/env python3
"""
Simple standalone demo of the Steane Code game.
Run this script to play a few rounds of syndrome decoding.

Usage:
    python simple_steane_demo.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.codes.steane import SteaneCode, SteaneGame
import numpy as np


def print_separator():
    print("=" * 70)


def demo_geometry():
    """Demonstrate the Fano plane geometry."""
    print_separator()
    print("STEANE CODE GEOMETRY DEMO")
    print_separator()

    code = SteaneCode()
    print(code.describe_geometry())
    print()


def demo_syndrome_decoding():
    """Demonstrate syndrome decoding with a specific error."""
    print_separator()
    print("SYNDROME DECODING EXAMPLE")
    print_separator()
    print()

    code = SteaneCode()

    # Create error on qubit 3
    error_vector = np.zeros(7, dtype=int)
    error_location = 3
    error_vector[error_location] = 1

    print(f"Introducing error on qubit {error_location}")
    print(f"Error vector: {error_vector}")
    print()

    # Compute syndrome
    syndrome = code.compute_syndrome(error_vector)
    syndrome_decimal = syndrome[0] + 2*syndrome[1] + 4*syndrome[2]

    print(f"Syndrome (binary): {syndrome}")
    print(f"Syndrome (decimal): {syndrome_decimal}")
    print()

    # Decode
    detected_location = code.syndrome_to_error_location(syndrome)
    print(f"Decoded error location: Qubit {detected_location}")
    print(f"Actual error location: Qubit {error_location}")
    print(f"Result: {'✓ CORRECT' if detected_location == error_location else '✗ WRONG'}")
    print()


def play_interactive_rounds(num_rounds=3):
    """Play several rounds of the game."""
    print_separator()
    print(f"PLAYING {num_rounds} ROUNDS")
    print_separator()
    print()

    game = SteaneGame()

    for i in range(num_rounds):
        print(f"\n--- ROUND {i+1} ---")

        # Generate error and compute syndrome
        round_info = game.play_round(num_errors=1)

        print(f"Syndrome (binary): {round_info['syndrome']}")
        print(f"Syndrome (decimal): {round_info['syndrome_decimal']}")
        print()

        # For demonstration, automatically decode
        code = SteaneCode()
        guess = code.syndrome_to_error_location(round_info['syndrome'])

        print(f"Decoded guess: Qubit {guess}")
        print(f"Actual error:  Qubit {round_info['true_locations'][0]}")

        # Check answer
        correct = game.check_answer(guess, round_info['true_locations'][0])
        print(f"Result: {'✓ CORRECT!' if correct else '✗ WRONG'}")

    # Final statistics
    print()
    print_separator()
    print("FINAL STATISTICS")
    print_separator()
    stats = game.get_stats()
    print(f"Score: {stats['score']}/{stats['rounds_played']}")
    print(f"Accuracy: {stats['accuracy']*100:.1f}%")
    print()


def demonstrate_all_syndromes():
    """Show all possible single-qubit errors and their syndromes."""
    print_separator()
    print("ALL SINGLE-QUBIT ERROR SYNDROMES")
    print_separator()
    print()

    code = SteaneCode()

    print("Qubit | Binary  | Decimal | Syndrome")
    print("------|---------|---------|----------")

    for qubit in range(7):
        error_vector = np.zeros(7, dtype=int)
        error_vector[qubit] = 1

        syndrome = code.compute_syndrome(error_vector)
        syndrome_decimal = syndrome[0] + 2*syndrome[1] + 4*syndrome[2]

        # Binary representation of qubit+1
        binary = format(qubit + 1, '03b')

        print(f"  {qubit}   | {binary}     |    {qubit+1}    | {syndrome}")

    print()
    print("Note: The syndrome equals the binary representation of (qubit_index + 1)")
    print()


def main():
    """Run all demonstrations."""
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 20 + "STEANE CODE DEMO" + " " * 32 + "║")
    print("║" + " " * 15 + "Quantum Error Correction Game" + " " * 24 + "║")
    print("╚" + "═" * 68 + "╝")
    print()

    # Run demonstrations
    demo_geometry()
    input("Press Enter to continue...")

    demo_syndrome_decoding()
    input("Press Enter to continue...")

    demonstrate_all_syndromes()
    input("Press Enter to continue...")

    play_interactive_rounds(num_rounds=5)

    print()
    print("Demo complete! Try the Jupyter notebook for more interactivity:")
    print("  jupyter notebook examples/steane_game_demo.ipynb")
    print()


if __name__ == "__main__":
    main()
