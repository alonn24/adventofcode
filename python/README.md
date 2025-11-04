# Advent of Code - Python Solutions

This directory contains Python solutions for Advent of Code challenges, organized by year with shared utility functions.

## 🚀 Quick Start

### Installation

1. Install the package in development mode (from repository root):

```bash
# Basic installation
pip install -e .

# With dev tools (autopep8, flake8)
pip install -e ".[dev]"
```

2. Get your puzzle inputs from Advent of Code:

   - [2024 Puzzles](https://adventofcode.com/2024) - Save to `inputs/2024/day_X.txt`
   - [2023 Puzzles](https://adventofcode.com/2023) - Save to `inputs/2023/day_X.txt`
   - [2022 Puzzles](https://adventofcode.com/2022) - Save to `inputs/2022/day_X.txt`

   **Note:** Input files are personal to each user and are not included in the repository.

### Running Tests

```bash
# Run all tests
pytest

# Run specific year
pytest python/year2024

# Run specific day
pytest python/year2024/day_1_test.py

# Run specific test function
pytest python/year2024/day_1_test.py::test_day1_part1_test_case

# Run with verbose output
pytest python/year2024 -v

# Run tests matching a pattern
pytest python/year2024 -k "part1"
```

### Linting

The project uses flake8 for code quality checks:

```bash
# Check for critical errors (syntax errors, undefined names)
flake8 python/ --count --select=E9,F63,F7,F82 --show-source --statistics

# Check for all code quality issues
flake8 python/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Auto-fix formatting issues (install autopep8 first)
pip install autopep8
autopep8 --in-place --aggressive --aggressive python/**/*.py
```

**Common flake8 checks:**

- **E9**: Syntax errors
- **F63, F7, F82**: Import and naming errors
- **E302**: Missing blank lines between functions
- **W293, W391**: Whitespace issues
- **F401**: Unused imports
