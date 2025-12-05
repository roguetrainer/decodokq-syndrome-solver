#!/bin/bash

# Setup script for Codo-Q: Quantum Error Correction Games
# This script creates a virtual environment and installs all dependencies

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored message
print_message() {
    color=$1
    message=$2
    echo -e "${color}${message}${NC}"
}

print_message "$BLUE" "╔════════════════════════════════════════════════════════════════╗"
print_message "$BLUE" "║       Codo-Q: Quantum Error Correction Games Setup            ║"
print_message "$BLUE" "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python 3 is installed
print_message "$YELLOW" "→ Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    print_message "$RED" "✗ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d ' ' -f 2)
print_message "$GREEN" "✓ Found Python $PYTHON_VERSION"
echo ""

# Check Python version is >= 3.8
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    print_message "$RED" "✗ Python 3.8 or higher is required. You have $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment
print_message "$YELLOW" "→ Creating virtual environment..."
if [ -d "venv" ]; then
    print_message "$YELLOW" "  Virtual environment already exists. Removing old one..."
    rm -rf venv
fi

python3 -m venv venv
print_message "$GREEN" "✓ Virtual environment created"
echo ""

# Activate virtual environment
print_message "$YELLOW" "→ Activating virtual environment..."
source venv/bin/activate
print_message "$GREEN" "✓ Virtual environment activated"
echo ""

# Upgrade pip
print_message "$YELLOW" "→ Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
print_message "$GREEN" "✓ pip upgraded"
echo ""

# Install requirements
print_message "$YELLOW" "→ Installing dependencies from requirements.txt..."
if [ ! -f "requirements.txt" ]; then
    print_message "$RED" "✗ requirements.txt not found!"
    exit 1
fi

pip install -r requirements.txt
print_message "$GREEN" "✓ Dependencies installed"
echo ""

# Verify installations
print_message "$YELLOW" "→ Verifying installations..."

# Check NumPy
if python -c "import numpy" 2>/dev/null; then
    NUMPY_VERSION=$(python -c "import numpy; print(numpy.__version__)")
    print_message "$GREEN" "  ✓ NumPy $NUMPY_VERSION"
else
    print_message "$RED" "  ✗ NumPy not installed correctly"
fi

# Check pytest
if python -c "import pytest" 2>/dev/null; then
    PYTEST_VERSION=$(python -c "import pytest; print(pytest.__version__)")
    print_message "$GREEN" "  ✓ pytest $PYTEST_VERSION"
else
    print_message "$YELLOW" "  ⚠ pytest not found (optional)"
fi

# Check Jupyter
if command -v jupyter &> /dev/null; then
    JUPYTER_VERSION=$(jupyter --version | grep "jupyter core" | cut -d: -f2 | xargs)
    print_message "$GREEN" "  ✓ Jupyter $JUPYTER_VERSION"
else
    print_message "$YELLOW" "  ⚠ Jupyter not found (recommended for interactive notebooks)"
fi

echo ""

# Test imports
print_message "$YELLOW" "→ Testing game imports..."
if python -c "from src.codes import SteaneCode, SteaneGame, ReedMullerCode, ReedMullerGame" 2>/dev/null; then
    print_message "$GREEN" "✓ Game modules imported successfully"
else
    print_message "$RED" "✗ Failed to import game modules"
    print_message "$YELLOW" "  This might be okay if you're setting up for the first time"
fi

echo ""

# Create activation helper script
print_message "$YELLOW" "→ Creating activation helper script..."
cat > activate_env.sh << 'EOF'
#!/bin/bash
# Quick activation script for the virtual environment
source venv/bin/activate
echo "Virtual environment activated!"
echo "To deactivate, run: deactivate"
EOF
chmod +x activate_env.sh
print_message "$GREEN" "✓ Created activate_env.sh"
echo ""

# Summary
print_message "$GREEN" "╔════════════════════════════════════════════════════════════════╗"
print_message "$GREEN" "║                  Setup Complete! 🎉                            ║"
print_message "$GREEN" "╚════════════════════════════════════════════════════════════════╝"
echo ""

print_message "$BLUE" "Next steps:"
echo ""
print_message "$YELLOW" "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo "   (or use: source activate_env.sh)"
echo ""

print_message "$YELLOW" "2. Try a quick demo:"
echo "   python examples/simple_steane_demo.py"
echo ""

print_message "$YELLOW" "3. Or start Jupyter for interactive learning:"
echo "   jupyter notebook examples/steane_game_demo.ipynb"
echo ""

print_message "$YELLOW" "4. Read the documentation:"
echo "   • GAMES-README.md (start here)"
echo "   • docs/games/QUICK-START-GUIDE.md"
echo ""

print_message "$BLUE" "Troubleshooting:"
echo "• If imports fail, make sure you're in the project root directory"
echo "• For Jupyter issues: pip install jupyter"
echo "• To deactivate the environment: deactivate"
echo ""

print_message "$GREEN" "Happy quantum error correcting! ⚛️"
