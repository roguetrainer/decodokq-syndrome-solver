# Quick Start Guide - Quantum Error Correction Games

## Overview

This guide helps you get started with the two main quantum error correction games in this repository.

**About This Project**: Inspired by [Dr. James Wootton's Decodoku](../design/ORIGINAL-DECODOKU-GAME.md), these games make quantum error correction accessible through geometric visualization and interactive gameplay.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codoq-quantum-game.git
cd codoq-quantum-game

# Install dependencies
pip install -r requirements.txt
```

## Two Games Available

### 1. Steane Code Game (2D - Fano Plane)
- **7 qubits** in 2D geometry
- **Fano plane** structure
- Perfect for beginners
- **Start here** if new to QEC

### 2. Reed-Muller Code Game (3D - Tetrahedron)
- **15 qubits** in 3D geometry
- **Tetrahedral** structure
- More complex visualization
- **Try after** mastering Steane

## Running the Games

### Option 1: Jupyter Notebooks (Recommended)

```bash
# Start Jupyter
jupyter notebook

# Open either:
# - examples/steane_game_demo.ipynb
# - examples/reed_muller_game_demo.ipynb
```

### Option 2: Python Script

#### Steane Code Example

```python
from src.codes import SteaneCode, SteaneGame

# Create game
game = SteaneGame()

# Play one round
round_info = game.play_round(num_errors=1)

# Show syndrome
print(f"Syndrome: {round_info['syndrome']}")
print(f"Which qubit has the error? (0-6)")

# Reveal answer
print(f"Answer: Qubit {round_info['true_locations'][0]}")

# Check if you were right
guess = int(input("Your guess: "))
correct = game.check_answer(guess, round_info['true_locations'][0])
print("Correct!" if correct else "Wrong!")
```

#### Reed-Muller Code Example

```python
from src.codes import ReedMullerCode, ReedMullerGame

# Create game with 15-qubit version
game = ReedMullerGame(use_extended=True)

# Play one round
round_info = game.play_round(num_errors=1)

# Show information
print(f"Syndrome: {round_info['syndrome']}")
print(f"Error is on: {round_info['geometric_descriptions'][0]}")
print(round_info['visualization'])
```

## Game Modes

### Practice Mode
Learn at your own pace with hints and full information:
```python
game = SteaneGame()
round_info = game.play_round()

# Get a hint
game.print_hint(round_info['syndrome'])
```

### Challenge Mode
Test your skills across multiple rounds:
```python
game = SteaneGame()

for i in range(10):
    round_info = game.play_round()
    # Solve without hints!
    guess = your_decoding_algorithm(round_info['syndrome'])
    game.check_answer(guess, round_info['true_locations'][0])

# Check your score
stats = game.get_stats()
print(f"Score: {stats['score']}/10")
```

## Understanding the Output

### Steane Code Output

```
Syndrome: [1 0 1]
Syndrome (decimal): 5
```

**How to decode:**
1. Convert syndrome to decimal: 1 + 0×2 + 1×4 = 5
2. The error is on qubit 4 (since we use 0-indexing, decimal 5 → qubit 4)

### Reed-Muller Code Output

```
Error on: Edge 1-2 (Qubit 7)

Visualization:
Q 0[ ] (Vertex 0)
Q 1[ ] (Vertex 1)
...
Q 7[X] (Edge 1-2)
```

**How to interpret:**
- `[ ]` = No error
- `[X]` = Error present
- Geometric description tells you the 3D structure

## Learning Path

### Week 1: Steane Code Basics
1. ✅ Understand Fano plane geometry
2. ✅ Learn syndrome-to-error mapping
3. ✅ Play 20 rounds with 100% accuracy

### Week 2: Steane Code Mastery
1. ✅ Understand stabilizer measurements
2. ✅ Explore multi-qubit errors
3. ✅ Study the parity check matrix

### Week 3: Reed-Muller Introduction
1. ✅ Visualize tetrahedral geometry
2. ✅ Map qubits to geometric elements
3. ✅ Play 10 rounds with hints

### Week 4: Reed-Muller Mastery
1. ✅ Decode without geometric descriptions
2. ✅ Understand Boolean function representation
3. ✅ Compare with Steane code

## Common Pitfalls

### Steane Code

❌ **Mistake**: Forgetting that syndrome is 1-indexed in decimal
```python
syndrome = [0, 1, 0]  # Binary: 010 = decimal 2
error_location = 2     # WRONG!
error_location = 1     # CORRECT (qubit index 1)
```

✅ **Solution**: Column of H at index `i` equals binary representation of `i+1`

### Reed-Muller Code

❌ **Mistake**: Confusing vertex indices with qubit indices
```python
error_on_vertex_2 = qubit_2  # WRONG! Vertex 2 is qubit 2
error_on_edge_0_1 = qubit_1  # WRONG! Edge 0-1 is qubit 4
```

✅ **Solution**: Use the `qubit_to_geometry` mapping

## Code Structure Reference

```
src/codes/
├── steane.py              # Steane [[7,1,3]] code
│   ├── SteaneCode         # Code implementation
│   └── SteaneGame         # Game logic
│
└── reed_muller.py         # Reed-Muller code
    ├── ReedMullerCode     # Code implementation (8 or 15 qubits)
    └── ReedMullerGame     # Game logic
```

## API Quick Reference

### Common Methods

Both `SteaneGame` and `ReedMullerGame` share these methods:

```python
# Play one round
round_info = game.play_round(num_errors=1)
# Returns: dict with 'syndrome', 'true_locations', 'visualization'

# Check answer
is_correct = game.check_answer(guess, true_location)
# Returns: bool

# Get statistics
stats = game.get_stats()
# Returns: dict with 'score', 'rounds_played', 'accuracy'
```

### Code-Specific Methods

**Steane:**
```python
code = SteaneCode()
syndrome = code.compute_syndrome(error_vector)
location = code.syndrome_to_error_location(syndrome)
geometry = code.describe_geometry()
```

**Reed-Muller:**
```python
code = ReedMullerCode(use_extended=True)
syndrome = code.compute_syndrome(error_vector)
geo_desc = code.get_geometric_description(qubit_idx)
structure = code.get_tetrahedral_structure()
```

## Next Steps

1. **Complete the notebooks**: Work through all cells in both demos
2. **Read the documentation**:
   - [Steane Code Game](steane-code-game.md)
   - [Reed-Muller Code Game](reed-muller-code-game.md)
3. **Explore the theory**: Check the `docs/theory/` folder
4. **Build your own game**: Use the code framework to create new challenges

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError`:
```bash
# Make sure you're in the project root
cd /path/to/codoq-quantum-game

# Add to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or in Python:
import sys
sys.path.append('..')  # When in examples/
```

### NumPy Errors

```bash
pip install --upgrade numpy
```

### Jupyter Not Starting

```bash
pip install jupyter
jupyter notebook
```

## Getting Help

- **Issues**: Open an issue on GitHub
- **Documentation**: Check `docs/` folder
- **Theory Questions**: Read the theory docs in `docs/theory/`

## Have Fun!

Quantum error correction is fascinating. Take your time, experiment, and enjoy learning! 🎮⚛️
