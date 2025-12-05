# Reed-Muller Code Syndrome Decoding Game

## Overview

The Reed-Muller Code Game teaches quantum error correction through 3D tetrahedral geometry. Players learn to visualize quantum codes in three dimensions and understand the relationship between geometric structure and error correction capabilities.

## The Reed-Muller Code

### Code Parameters

**Standard RM(1,3):**
- **Physical qubits (n)**: 8
- **Information bits (k)**: 4
- **Distance (d)**: 4

**Extended/Quantum version [[15,1,3]]:**
- **Physical qubits (n)**: 15
- **Logical qubits (k)**: 1
- **Distance (d)**: 3
- **Error correction**: Can correct any single-qubit error

### Background

Reed-Muller codes are a family of classical error-correcting codes discovered by Irving S. Reed and D. E. Muller in 1954. They have beautiful geometric structure and important properties:

- **Recursive construction**: Built from smaller Reed-Muller codes
- **Boolean function representation**: Codewords correspond to Boolean functions
- **Geometric interpretation**: Points and hyperplanes in affine/projective space
- **NASA heritage**: Used in Mariner 9 spacecraft (1971)

The quantum version uses the CSS construction to create a quantum error-correcting code.

## Tetrahedral Geometry

### The 4-Dimensional Simplex

A **simplex** is the simplest polytope in any dimension:
- 1D: Line segment (2 vertices)
- 2D: Triangle (3 vertices)
- 3D: Tetrahedron (4 vertices)
- 4D: 4-simplex (5 vertices)

For the Reed-Muller code, we work with a **regular tetrahedron** structure.

### Structure of the 15-Qubit Code

The 15 qubits map to geometric elements:

#### 4 Vertices (Qubits 0-3)

The fundamental points of the tetrahedron in 3D space:

| Qubit | Position (x, y, z) | Description |
|-------|-------------------|-------------|
| 0     | (1, 1, 1)         | Vertex 0    |
| 1     | (1, -1, -1)       | Vertex 1    |
| 2     | (-1, 1, -1)       | Vertex 2    |
| 3     | (-1, -1, 1)       | Vertex 3    |

These vertices form a regular tetrahedron centered at the origin.

#### 6 Edges (Qubits 4-9)

Edges connect pairs of vertices. There are C(4,2) = 6 edges:

| Qubit | Edge | Connects Vertices |
|-------|------|-------------------|
| 4     | 0-1  | Vertex 0 ↔ Vertex 1 |
| 5     | 0-2  | Vertex 0 ↔ Vertex 2 |
| 6     | 0-3  | Vertex 0 ↔ Vertex 3 |
| 7     | 1-2  | Vertex 1 ↔ Vertex 2 |
| 8     | 1-3  | Vertex 1 ↔ Vertex 3 |
| 9     | 2-3  | Vertex 2 ↔ Vertex 3 |

#### 4 Faces (Qubits 10-13)

Triangular faces formed by triples of vertices. There are C(4,3) = 4 faces:

| Qubit | Face | Vertices |
|-------|------|----------|
| 10    | Face 0 | {0, 1, 2} |
| 11    | Face 1 | {0, 1, 3} |
| 12    | Face 2 | {0, 2, 3} |
| 13    | Face 3 | {1, 2, 3} |

#### 1 Interior (Qubit 14)

The **whole tetrahedron** - representing the interior or volume.

### Combinatorial Summary

- **0-dimensional elements**: 4 vertices
- **1-dimensional elements**: 6 edges
- **2-dimensional elements**: 4 faces
- **3-dimensional element**: 1 interior
- **Total**: 4 + 6 + 4 + 1 = **15 qubits**

This is the **face lattice** of a tetrahedron!

## Reed-Muller Construction

### Generator Matrix

The generator matrix for RM(1,3) has rows corresponding to:

```
G = [1 1 1 1 1 1 1 1]    Row 0: Constant function (all 1s)
    [0 1 0 1 0 1 0 1]    Row 1: x₁ (first coordinate)
    [0 0 1 1 0 0 1 1]    Row 2: x₂ (second coordinate)
    [0 0 0 0 1 1 1 1]    Row 3: x₃ (third coordinate)
```

Each row represents a Boolean function:
- **Row 0**: f(x₁,x₂,x₃) = 1 (constant)
- **Row 1**: f(x₁,x₂,x₃) = x₁
- **Row 2**: f(x₁,x₂,x₃) = x₂
- **Row 3**: f(x₁,x₂,x₃) = x₃

### Codewords

Linear combinations of these rows (over GF(2)) give 2⁴ = 16 codewords.

### Duality

Reed-Muller codes have interesting duality properties:
- RM(r, m) is dual to RM(m-r-1, m)
- RM(1, m) is self-dual when properly extended

## Syndrome Decoding

### Error Patterns

In the quantum version, errors can occur on any of the 15 qubits:

1. **Vertex errors** (Qubits 0-3): Fundamental point errors
2. **Edge errors** (Qubits 4-9): Errors on connections
3. **Face errors** (Qubits 10-13): Errors on 2D surfaces
4. **Interior error** (Qubit 14): Error on the whole structure

### Geometric Intuition

The geometric structure helps us understand error patterns:

- **Adjacent elements**: Vertices connected by an edge, or edges bounding a face
- **Incidence**: Which elements contain or are contained in others
- **Symmetry**: The tetrahedron has high symmetry (Td point group)

### Syndrome Structure

The syndrome is computed using the parity check matrix H. For the quantum code, we use stabilizer generators derived from the classical Reed-Muller code structure.

## Game Mechanics

### Objective

Learn to decode syndromes and identify error locations using 3D geometric intuition.

### How to Play

1. **Visualize the structure**: Understand the tetrahedral geometry
2. **Error introduced**: A random error occurs on one (or more) qubits
3. **Observe syndrome**: See the stabilizer measurement results
4. **Identify location**: Determine which qubit(s) have errors
5. **Geometric reasoning**: Use the 3D structure to understand error patterns
6. **Submit answer**: Check your understanding

### Difficulty Levels

#### Beginner
- Single errors on vertices only
- Full geometric descriptions provided
- Focus on learning the structure

#### Intermediate
- Errors on any geometric element (vertices, edges, faces)
- Syndrome provided
- Must map syndrome to geometric location

#### Advanced
- Multiple errors
- Identify error patterns
- Understand uncorrectable errors

## Learning Objectives

1. **3D geometric visualization** of quantum codes
2. **Hierarchical structure** - vertices → edges → faces → interior
3. **Boolean function representation** of codewords
4. **Reed-Muller code family** and their properties
5. **Geometric vs. algebraic** perspectives on error correction

## Code Implementation

### Running the Game

```python
from src.codes.reed_muller import ReedMullerCode, ReedMullerGame

# Initialize 15-qubit version
game = ReedMullerGame(use_extended=True)

# Play a round
round_info = game.play_round(num_errors=1)

# See the geometric description
print(round_info['geometric_descriptions'])
print(round_info['visualization'])

# Check statistics
stats = game.get_stats()
```

### Jupyter Notebook

For interactive 3D exploration:

```bash
jupyter notebook examples/reed_muller_game_demo.ipynb
```

## Visualization Strategies

### Text-Based (Current Implementation)

The current game uses text to describe geometric elements:
- Qubit index
- Element type (vertex/edge/face/interior)
- Which vertices are involved
- 3D coordinates (for vertices)

### Future: 3D Graphics

Potential enhancements:
- Interactive 3D rotation of the tetrahedron
- Highlight error locations in red
- Animate syndrome propagation
- Show stabilizer support regions

## Mathematical Details

### Affine Space Representation

The 8 positions in RM(1,3) correspond to points in 3D affine space:

```
Position    (x₁, x₂, x₃)
   0         (0, 0, 0)
   1         (1, 0, 0)
   2         (0, 1, 0)
   3         (1, 1, 0)
   4         (0, 0, 1)
   5         (1, 0, 1)
   6         (0, 1, 1)
   7         (1, 1, 1)
```

These are the 8 vertices of a 3D unit cube.

### Reed-Muller Decoding

Classical Reed-Muller decoding uses **majority logic** or **recursive decoding**. The algorithm exploits the code's structure to efficiently correct errors.

For the quantum version, we use stabilizer measurements and syndrome lookup.

## Comparison with Other Codes

### Steane vs. Reed-Muller

| Property | Steane [[7,1,3]] | Reed-Muller [[15,1,3]] |
|----------|------------------|------------------------|
| Qubits | 7 | 15 |
| Dimension | 2D (Fano plane) | 3D (Tetrahedron) |
| Geometric Elements | Points + Lines | Vertices + Edges + Faces |
| Symmetry Group | PGL(3,2) ≈ PSL(2,7) | Tetrahedral group Td |
| Code Family | Hamming/CSS | Reed-Muller/CSS |
| Efficiency | More efficient | More geometric structure |

### Surface Code vs. Reed-Muller

Surface codes use 2D lattices, while Reed-Muller uses 3D polytope structure. Both are topological in nature.

## Advanced Topics

### Higher-Order Reed-Muller Codes

The family RM(r, m) includes:
- **RM(0, m)**: Repetition code
- **RM(1, m)**: First-order (used here)
- **RM(2, m)**: Second-order (includes products like x₁x₂)
- **RM(m, m)**: Full space (no error correction)

### Recursive Construction

Reed-Muller codes can be built recursively:
```
RM(r, m) = {(u, u+v) | u ∈ RM(r, m-1), v ∈ RM(r-1, m-1)}
```

This is called the **Plotkin construction** or **|u|u+v| construction**.

### Applications

Reed-Muller codes are used in:
- Spacecraft communication (Mariner, Pioneer)
- 5G polar codes (are related to RM codes)
- Quantum computing (CSS code construction)
- Cryptography (bent functions)

## Tips and Strategies

### Geometric Thinking

1. **Start with vertices**: The 4 fundamental points
2. **Build edges**: Connect vertex pairs
3. **Form faces**: Triangular regions
4. **Complete structure**: The whole tetrahedron

### Syndrome Patterns

Different geometric elements may produce recognizable syndrome patterns. With practice, you'll learn to associate syndromes with geometric locations.

### Symmetry Exploitation

The tetrahedron has 24 symmetries (rotations and reflections). Understanding these symmetries can help recognize equivalent error patterns.

## Extensions and Variants

### Multi-Error Patterns

Introduce errors on multiple qubits and study:
- Which patterns are correctable
- Which patterns are detectable but not correctable
- Which patterns are indistinguishable from no error

### Higher Dimensions

Explore 4D and 5D simplices for larger codes.

### Color Code Connection

The tetrahedral structure is related to 3D color codes, another family of topological quantum codes.

## References

1. Reed, I. S. (1954). "A class of multiple-error-correcting codes and the decoding scheme"
2. Muller, D. E. (1954). "Application of Boolean algebra to switching circuit design"
3. MacWilliams & Sloane. "The Theory of Error-Correcting Codes". Chapter 13.
4. Nielsen & Chuang. "Quantum Computation and Quantum Information". Chapter 10.

## Related Games

- [Steane Code Game](steane-code-game.md) - 2D Fano plane geometry
- Surface Code Game - 2D lattice topology
- Color Code Game - 3D face-centered cubic lattice

## Next Steps

1. Complete the Reed-Muller game tutorial
2. Compare with the 2D Steane code
3. Study the Boolean function representation
4. Explore higher-order Reed-Muller codes
5. Investigate connections to polar codes
