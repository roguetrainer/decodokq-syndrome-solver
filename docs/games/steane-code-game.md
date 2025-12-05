# Steane Code Syndrome Decoding Game

## Overview

The Steane Code Game teaches quantum error correction through interactive syndrome decoding using the Steane [[7,1,3]] quantum code. Players learn to identify error locations by interpreting syndrome measurements from stabilizer checks.

## The Steane [[7,1,3]] Code

### Code Parameters
- **Physical qubits (n)**: 7
- **Logical qubits (k)**: 1
- **Distance (d)**: 3
- **Error correction**: Can correct any single-qubit error (X, Y, or Z)

### Background

The Steane code is a CSS (Calderbank-Shor-Steane) code built from the classical Hamming (7,4) code. It was one of the first quantum error correction codes discovered and remains important for:
- Fault-tolerant quantum computing
- Transversal gate implementation
- Educational demonstrations of quantum error correction

## Fano Plane Geometry

The Steane code is based on the **Fano plane** (also written as PG(2,2)), the smallest finite projective geometry.

### Structure
- **7 points**: Representing the 7 physical qubits
- **7 lines**: Each containing exactly 3 points
- **Incidence**: Every pair of points lies on exactly one line; every pair of lines intersects at exactly one point

### Binary Representation

The 7 points correspond to the 7 non-zero binary vectors of length 3:

| Qubit | Binary | Decimal |
|-------|--------|---------|
| 0     | 001    | 1       |
| 1     | 010    | 2       |
| 2     | 011    | 3       |
| 3     | 100    | 4       |
| 4     | 101    | 5       |
| 5     | 110    | 6       |
| 6     | 111    | 7       |

### The 7 Fano Lines

Each line is a set of 3 qubits whose binary representations XOR to zero:

1. **Line 0**: {0, 2, 4} - (001, 011, 101)
2. **Line 1**: {1, 2, 6} - (010, 011, 111)
3. **Line 2**: {0, 1, 3} - (001, 010, 100)
4. **Line 3**: {4, 5, 6} - (101, 110, 111)
5. **Line 4**: {2, 3, 5} - (011, 100, 110)
6. **Line 5**: {0, 5, 6} - (001, 110, 111)
7. **Line 6**: {1, 3, 4} - (010, 100, 101)

## Stabilizers

The Steane code uses **6 stabilizer generators** to detect errors:

### Parity Check Matrix (H)

The Hamming (7,4) parity check matrix:

```
H = [0 0 0 1 1 1 1]    Check 1: Qubits {3, 4, 5, 6}
    [0 1 1 0 0 1 1]    Check 2: Qubits {1, 2, 5, 6}
    [1 0 1 0 1 0 1]    Check 3: Qubits {0, 2, 4, 6}
```

### X-type and Z-type Stabilizers

- **3 X-type stabilizers**: Detect Z (phase-flip) errors
- **3 Z-type stabilizers**: Detect X (bit-flip) errors

Each stabilizer is a 4-qubit Pauli operator formed from the rows of H.

## Syndrome Decoding

### How It Works

1. **Error occurs**: A single qubit experiences an X, Y, or Z error
2. **Measure stabilizers**: All 6 stabilizers are measured
3. **Compute syndrome**: The 3 X-type measurements give a 3-bit syndrome
4. **Decode**: The syndrome directly indicates the error location

### The Magic of Hamming Codes

For the Steane/Hamming code, **the syndrome IS the error location**!

- Syndrome = `[0,0,0]` → No error
- Syndrome = `[1,0,0]` → Error on qubit 0 (binary 001 = 1)
- Syndrome = `[0,1,0]` → Error on qubit 1 (binary 010 = 2)
- Syndrome = `[1,1,0]` → Error on qubit 2 (binary 011 = 3)
- ...and so on

The syndrome value (read as binary) equals the qubit index + 1.

## Game Mechanics

### Objective
Learn to identify error locations from syndrome measurements.

### How to Play

1. **Round starts**: A random single-qubit error is introduced
2. **Observe syndrome**: You see the 3-bit syndrome from stabilizer measurements
3. **Decode**: Determine which qubit (0-6) has the error
4. **Submit answer**: Check if you correctly identified the error location
5. **Feedback**: See if you were correct and understand why

### Difficulty Levels

#### Beginner
- Single X errors only
- Full syndrome shown
- Hints available

#### Intermediate
- X and Z errors
- Must distinguish error type from stabilizer measurements

#### Advanced
- Y errors (both X and Z components)
- Multiple rounds with scoring
- Time limits

## Learning Objectives

After playing this game, you should understand:

1. **Fano plane geometry** and its connection to the Hamming code
2. **Stabilizer measurements** and syndrome calculation
3. **Error syndrome relationship** - how syndromes point to error locations
4. **CSS codes** - using classical codes to build quantum codes
5. **Perfect codes** - minimal redundancy for error correction

## Code Implementation

### Running the Game

```python
from src.codes.steane import SteaneCode, SteaneGame

# Initialize
game = SteaneGame()

# Play a round
round_info = game.play_round(num_errors=1)
print(f"Syndrome: {round_info['syndrome']}")

# Make a guess
guess = 5  # Your guess
correct = game.check_answer(guess, round_info['true_locations'][0])

# Check statistics
stats = game.get_stats()
print(f"Score: {stats['score']}/{stats['rounds_played']}")
```

### Jupyter Notebook

For an interactive experience, use the provided Jupyter notebook:

```bash
jupyter notebook examples/steane_game_demo.ipynb
```

## Mathematical Details

### Syndrome Calculation

Given an error vector **e** (7-bit binary vector with 1 at error location):

**Syndrome s = H · e (mod 2)**

Where H is the 3×7 parity check matrix.

### Example

Error on qubit 5:
- Error vector: `e = [0,0,0,0,0,1,0]`
- Syndrome calculation:
  ```
  s₁ = 0⊕0⊕0⊕1⊕1⊕1⊕0 = 1
  s₂ = 0⊕1⊕1⊕0⊕0⊕1⊕0 = 1
  s₃ = 1⊕0⊕1⊕0⊕1⊕0⊕0 = 1
  ```
- Syndrome: `s = [1,1,1]` = binary 111 = decimal 7
- But we use 0-indexing, so error is on qubit 5 (111 - 1 = 6, but column 6 in 0-indexed H)

Actually, column 5 of H (0-indexed) is `[1,1,1]ᵀ`, confirming the error location.

## Tips and Strategies

### Quick Syndrome Decoding

1. **Convert to decimal**: Read syndrome as 3-bit binary number
2. **Subtract 1**: Get 0-indexed qubit number
3. **Verify**: Check against the parity check matrix columns

### Pattern Recognition

Learn to recognize common syndromes:
- `[1,0,0]` → Qubit 0
- `[0,1,0]` → Qubit 1
- `[1,1,0]` → Qubit 2
- `[0,0,1]` → Qubit 3
- etc.

### Understanding Stabilizers

Remember that each stabilizer checks 4 qubits. If a stabilizer "fires" (measures -1), the error is on one of those 4 qubits. The combination of all 3 stabilizer measurements narrows it down to exactly 1 qubit.

## Extensions and Variants

### Multi-error Detection

While the Steane code can only *correct* single errors, it can *detect* some two-error patterns. Try introducing two errors and see what syndromes appear!

### Logical Operations

Explore how logical X, Y, Z operations on the encoded logical qubit correspond to operations on the physical qubits.

### Circuit Implementation

Study the quantum circuit for encoding, error correction, and decoding in the Steane code.

## References

1. Steane, A. M. (1996). "Error Correcting Codes in Quantum Theory". Physical Review Letters.
2. Nielsen & Chuang. "Quantum Computation and Quantum Information". Chapter 10.
3. Gottesman, D. "Stabilizer Codes and Quantum Error Correction" (PhD thesis).

## Related Games

- [Reed-Muller Game](reed-muller-code-game.md) - 3D tetrahedral geometry
- Hamming (7,4) Classical Code - The classical foundation
- Surface Code Game - 2D lattice topology

## Next Steps

1. Complete the Steane game tutorial
2. Try the Reed-Muller game for 3D geometry
3. Study the full stabilizer formalism
4. Explore fault-tolerant gate implementations
