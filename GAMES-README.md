# Quantum Error Correction Games

## Overview

This repository contains two interactive games for learning quantum error correction codes through geometric visualization and syndrome decoding practice.

**Inspired by [Decodoku](docs/design/ORIGINAL-DECODOKU-GAME.md)**: This project builds upon Dr. James Wootton's pioneering work in quantum gaming education, extending the concept to qubit stabilizer codes with rich geometric structure (Steane and Reed-Muller codes).

---
![CodoQ](./img/CodoQ.png)
---

## Games Implemented

### 1. Steane Code Game - 2D Fano Plane Geometry

**Code**: Steane [[7,1,3]] quantum error correction code

**Geometry**: Fano plane (PG(2,2))
- 7 qubits = 7 points
- 7 lines (3 points each)
- 2D projective geometry

**Files**:
- Implementation: [src/codes/steane.py](src/codes/steane.py)
- Jupyter Notebook: [examples/steane_game_demo.ipynb](examples/steane_game_demo.ipynb)
- Documentation: [docs/games/steane-code-game.md](docs/games/steane-code-game.md)

**Key Features**:
- Perfect syndrome decoding (syndrome = error location)
- Based on classical Hamming (7,4) code
- 6 stabilizer generators (3 X-type, 3 Z-type)
- Ideal for beginners learning QEC

### 2. Reed-Muller Code Game - 3D Tetrahedral Geometry

**Code**: Reed-Muller [[15,1,3]] quantum code (extended version)

**Geometry**: Tetrahedral simplex
- 15 qubits = 4 vertices + 6 edges + 4 faces + 1 interior
- 3D geometric structure
- Face lattice of a tetrahedron

**Files**:
- Implementation: [src/codes/reed_muller.py](src/codes/reed_muller.py)
- Jupyter Notebook: [examples/reed_muller_game_demo.ipynb](examples/reed_muller_game_demo.ipynb)
- Documentation: [docs/games/reed-muller-code-game.md](docs/games/reed-muller-code-game.md)

**Key Features**:
- 3D geometric visualization
- Qubit-to-geometry mapping
- Boolean function representation
- More complex than Steane code

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Running the Games

#### Option 1: Jupyter Notebooks (Recommended)

Open in Jupyter:
- `examples/steane_game_demo.ipynb` - Start here!
- `examples/reed_muller_game_demo.ipynb` - Try after Steane

#### Option 2: Python Scripts

**Steane Game:**
```python
from src.codes import SteaneGame

game = SteaneGame()
round_info = game.play_round(num_errors=1)

print(f"Syndrome: {round_info['syndrome']}")
print(f"Error at: Qubit {round_info['true_locations'][0]}")
```

**Reed-Muller Game:**
```python
from src.codes import ReedMullerGame

game = ReedMullerGame(use_extended=True)
round_info = game.play_round(num_errors=1)

print(f"Error on: {round_info['geometric_descriptions'][0]}")
print(round_info['visualization'])
```

## Documentation

### Game Guides
- 📘 [Quick Start Guide](docs/games/QUICK-START-GUIDE.md) - **START HERE**
- 📗 [Steane Code Game Guide](docs/games/steane-code-game.md)
- 📙 [Reed-Muller Code Game Guide](docs/games/reed-muller-code-game.md)

### Theory Documentation
Located in [docs/theory/](docs/theory/):
- Fano plane exploration
- Hamming checks and Fano plane rules
- Stabilizer theory
- Self-duality properties
- Logical qubit concepts

### Design Documentation
Located in [docs/design/](docs/design/):
- Extension roadmap
- Technical roadmap
- UI language guide

## Game Comparison

| Feature | Steane [[7,1,3]] | Reed-Muller [[15,1,3]] |
|---------|------------------|------------------------|
| **Qubits** | 7 | 15 |
| **Geometry** | 2D Fano Plane | 3D Tetrahedron |
| **Elements** | 7 points, 7 lines | 4 vertices, 6 edges, 4 faces, 1 interior |
| **Distance** | 3 | 3 |
| **Difficulty** | Beginner | Intermediate |
| **Syndrome Decoding** | Direct (Hamming) | Pattern-based |
| **Best For** | Learning QEC basics | Understanding geometry |

## What You'll Learn

### Core Concepts
1. **Quantum Error Correction** fundamentals
2. **Stabilizer codes** and syndrome decoding
3. **CSS codes** (Calderbank-Shor-Steane)
4. **Geometric representations** of quantum codes

### Steane Code Specifics
- Fano plane geometry
- Perfect codes
- Hamming code connection
- Direct syndrome decoding

### Reed-Muller Code Specifics
- 3D geometric visualization
- Boolean function representation
- Hierarchical structure
- Reed-Muller code family

## Code Structure

```
codoq-quantum-game/
│
├── src/codes/                      # Code implementations
│   ├── steane.py                  # Steane [[7,1,3]]
│   │   ├── SteaneCode            # Code class
│   │   └── SteaneGame            # Game class
│   └── reed_muller.py            # Reed-Muller code
│       ├── ReedMullerCode        # Code class (8 or 15 qubits)
│       └── ReedMullerGame        # Game class
│
├── examples/                       # Jupyter notebooks
│   ├── steane_game_demo.ipynb
│   └── reed_muller_game_demo.ipynb
│
└── docs/games/                     # Documentation
    ├── QUICK-START-GUIDE.md       # Start here!
    ├── steane-code-game.md
    └── reed-muller-code-game.md
```

## Game Features

### Both Games Support

✅ Single-error syndrome decoding
✅ Random error generation
✅ Syndrome calculation
✅ Geometric visualization (text-based)
✅ Score tracking
✅ Practice and challenge modes
✅ Hints and explanations

### Future Enhancements

🔲 3D interactive graphics (for Reed-Muller)
🔲 Multi-error patterns
🔲 Time-based challenges
🔲 Leaderboards
🔲 Animation of error propagation
🔲 Sound effects

## Learning Path

### Recommended Progression

1. **Week 1: Steane Basics**
   - Complete `steane_game_demo.ipynb`
   - Read [steane-code-game.md](docs/games/steane-code-game.md)
   - Play 20 rounds with 100% accuracy

2. **Week 2: Steane Mastery**
   - Understand stabilizer formalism
   - Study the Fano plane structure
   - Explore multi-qubit errors

3. **Week 3: Reed-Muller Introduction**
   - Complete `reed_muller_game_demo.ipynb`
   - Visualize the tetrahedral geometry
   - Map qubits to geometric elements

4. **Week 4: Reed-Muller Mastery**
   - Decode without hints
   - Compare with Steane code
   - Understand Boolean functions

## Testing Your Understanding

After completing both games, you should be able to:

- [ ] Explain what a stabilizer is
- [ ] Calculate syndromes by hand (for Steane)
- [ ] Draw the Fano plane and label all 7 lines
- [ ] Describe the tetrahedral structure
- [ ] Map any qubit to its geometric element (Reed-Muller)
- [ ] Explain why these codes have distance 3
- [ ] Understand CSS code construction

## Examples

### Steane Code Example

```python
from src.codes import SteaneCode

code = SteaneCode()

# Create error on qubit 5
import numpy as np
error = np.zeros(7, dtype=int)
error[5] = 1

# Compute syndrome
syndrome = code.compute_syndrome(error)
print(f"Syndrome: {syndrome}")  # [0 1 1]

# Decode
location = code.syndrome_to_error_location(syndrome)
print(f"Error at qubit: {location}")  # 5
```

### Reed-Muller Code Example

```python
from src.codes import ReedMullerCode

code = ReedMullerCode(use_extended=True)

# Show geometry
print(code.describe_geometry())

# Get geometric element for qubit 7
print(code.get_geometric_description(7))  # "Edge 1-2"

# Show tetrahedral structure
structure = code.get_tetrahedral_structure()
print(f"Vertices: {structure['vertices']}")
print(f"Edges: {structure['edges']}")
```

## Contributing

Ideas for new games or improvements?

1. Fork the repository
2. Create a feature branch
3. Add your game in `src/codes/`
4. Create a Jupyter notebook in `examples/`
5. Write documentation in `docs/games/`
6. Submit a pull request

## References

### Papers
- Steane, A. M. (1996). "Error Correcting Codes in Quantum Theory"
- Reed, I. S. (1954). "A class of multiple-error-correcting codes"
- Muller, D. E. (1954). "Application of Boolean algebra to switching circuit design"

### Books
- Nielsen & Chuang. "Quantum Computation and Quantum Information"
- MacWilliams & Sloane. "The Theory of Error-Correcting Codes"

### Online Resources
- [Quantum Error Correction Zoo](https://errorcorrectionzoo.org/)
- [Original Decodoku game](https://github.com/quantumjim/decodoku) by Dr. James Wootton
- [The Original Decodoku - Full Story](docs/design/ORIGINAL-DECODOKU-GAME.md)

## License

[Your license here]

## Acknowledgments

This project builds upon **Dr. James Wootton's** pioneering [Decodoku](https://github.com/quantumjim/decodoku) game, which showed that quantum error correction could be made accessible and fun through gaming. We are grateful for his vision of quantum gaming education and the open-source code he shared.

**Special thanks to:**

- **Dr. James Wootton** - For creating the original Decodoku and inspiring this project
- **The Decodoku community** - For demonstrating that games can contribute to quantum research
- **Quantum error correction researchers** - For the theoretical foundations

Read more about [the original Decodoku game](docs/design/ORIGINAL-DECODOKU-GAME.md) and its impact on quantum gaming education.

---

**Ready to start?** Open [docs/games/QUICK-START-GUIDE.md](docs/games/QUICK-START-GUIDE.md) and begin your quantum error correction journey! 🚀⚛️
