# Decodok-Q: Quantum Error Correction Games

An interactive platform for learning quantum error correction through games and visualizations. Built around the Steane code, Hamming codes, and other QEC constructions.

**Inspired by and building upon** the pioneering [Decodoku](docs/design/ORIGINAL-DECODOKU-GAME.md) game by Dr. James Wootton. This project extends the concept of quantum gaming education to additional quantum codes with rich geometric structure.

## Features

- **Interactive Visualizations**: Explore the Fano plane geometry underlying the Steane [[7,1,3]] code
- **Educational Games**: Learn syndrome decoding through hands-on puzzles
- **Modular QEC Framework**: Extensible Python backend for multiple code families
- **Visual Learning**: Understand stabilizer codes through geometric representations

## Project Structure

```
decodokq-syndrome-solver/
├── docs/                   # Documentation
│   ├── design/            # Roadmaps and UI design decisions
│   ├── theory/            # QEC theory and mathematical concepts
│   ├── games/             # Game-specific documentation
│   └── api/               # API documentation (future)
│
├── frontend/              # Frontend HTML/CSS/JS
│   ├── games/            # Individual game implementations
│   ├── shared/           # Shared components and utilities
│   ├── assets/           # Static assets
│   └── index.html        # Landing page
│
├── src/                   # Backend Python code
│   ├── core/             # Core QEC framework
│   ├── codes/            # Specific code implementations
│   ├── games/            # Game logic
│   ├── visualizers/      # Visualization backend
│   ├── api/              # API layer (future)
│   └── utils/            # Utility functions
│
├── tests/                 # Test suite
├── examples/              # Example scripts and notebooks
└── scripts/               # Build and utility scripts
```

## Current Games

### Fano Plane Syndrome Visualizer
Explore the dual Fano plane geometry that underlies the Steane [[7,1,3]] quantum error correction code. Select 3-qubit Hamming checks to see their 4-qubit stabilizer complements.

**Play now**: [frontend/games/fano-plane-syndrome-visualizer.html](frontend/games/fano-plane-syndrome-visualizer.html)

### Hamming Game (In Development)
Practice syndrome decoding with the classical Hamming (7,4) code.

## Getting Started

### Prerequisites
- Python 3.8+
- Modern web browser (for HTML visualizations)
- NumPy (installed automatically)

### Quick Setup

**Linux/macOS:**

```bash
# Clone the repository
git clone https://github.com/yourusername/decodokq-syndrome-solver.git
cd decodokq-syndrome-solver

# Run the setup script (creates venv and installs dependencies)
./setup.sh

# Activate the virtual environment
source venv/bin/activate
```

**Windows:**

```cmd
# Clone the repository
git clone https://github.com/yourusername/decodokq-syndrome-solver.git
cd decodokq-syndrome-solver

# Run the setup script (creates venv and installs dependencies)
setup.bat

# Activate the virtual environment
venv\Scripts\activate.bat
```

**Manual Installation:**

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

### Running Games

Open any HTML file in the `frontend/games/` directory directly in your browser:

```bash
open frontend/games/fano-plane-syndrome-visualizer.html
```

Or serve via a local server:

```bash
python -m http.server 8000
# Navigate to http://localhost:8000/frontend/
```

## Development

### Backend Development

The Python backend provides the QEC framework:

```python
from src.core.code_abstractions import CodeDefinition
from src.core.qec_framework import QubitRegister

# Use the core framework for your QEC experiments
```

### Adding New Games

1. Implement game logic in `src/games/`
2. Create visualization in `frontend/games/`
3. Add documentation in `docs/games/`

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/test_core/
```

## Key Concepts

### Steane Code
The [[7,1,3]] Steane code is a quantum error correction code that can:
- Encode 1 logical qubit into 7 physical qubits
- Detect and correct any single-qubit error
- Uses stabilizer formalism with 6 stabilizer generators

### Fano Plane Geometry
The Fano plane is a finite projective plane with 7 points and 7 lines. In the Steane code:
- Each point represents a physical qubit
- 7 lines represent Hamming (7,4) parity checks
- Complementary 4-qubit sets form the 6 stabilizers

## Documentation

### Games

- [Quick Start Guide](docs/games/QUICK-START-GUIDE.md) - Start here!
- [Steane Code Game](docs/games/steane-code-game.md)
- [Reed-Muller Code Game](docs/games/reed-muller-code-game.md)
- [Original Decodoku Game](docs/design/ORIGINAL-DECODOKU-GAME.md) - The inspiration

### Theory

- [Fano Plane Exploration](docs/theory/FANO-PLANE-EXPLORATION-AND-CODING-PLAN.md)
- [Steane Code Puzzle Design](docs/games/DECODOKQ-STEANE-CODE-PUZZLE.md)

### Design

- [Technical Roadmap](docs/design/ENHANCING-DECODOKU-TECHNICAL-ROADMAP.md)
- [UI Language Guide](docs/design/LANGUAGE-FOR-GAME-UI.md)

## Roadmap

- [ ] Complete Hamming game implementation
- [ ] Add multiplayer syndrome decoding challenges
- [ ] Implement Surface code visualizations
- [ ] Build REST API for game state management
- [ ] Add Color code support
- [ ] Create educational tutorial mode

## Contributing

Contributions welcome! Please read the documentation in `docs/` to understand the theoretical foundation.

## License

[Add your license here]

## Acknowledgments

This project builds upon the pioneering work of **Dr. James Wootton** and his original [Decodoku](https://github.com/quantumjim/decodoku) game, which demonstrated that quantum error correction research could be both accessible and fun through gaming.

**Special thanks to:**

- **Dr. James Wootton** - For creating the original Decodoku and sharing the code that inspired this project
- **The Decodoku community** - For showing that the public can contribute meaningfully to quantum research
- **NCCR QSIT** - For supporting the original Decodoku research

We stand on the shoulders of giants who showed us that quantum computing education should be playful, accessible, and engaging.

**Learn more**: Read about [the original Decodoku game](docs/design/ORIGINAL-DECODOKU-GAME.md) and James Wootton's philosophy on quantum gaming education.
