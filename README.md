[Advent Of Code](https://adventofcode.com) solutions

## Testing
### javascript / python / go / other script languages
```
> node */js/day-xx.js
> python */python/day-xx.py
> go run */go/day-xx.go
```

### scala
```
> sbt
> compile
> run
> chooose day-XX to run
```

### cpp
```
> cmake CMakeLists.txt
> make
> */cpp/run-
day-xx
```

### Python

Python solutions are organized in the `python/` directory. See [python/README.md](python/README.md) for detailed setup and workflow.

**Quick Start:**
```bash
# Install package
pip install -e .

# Run all tests
pytest

# Run specific year
pytest python/year2024

# Run specific day
pytest python/year2024/day_1_test.py
```

**Getting Input Files:**
Input files are not included in the repository (they are personal to each user). Get your inputs from:
- [Advent of Code 2024](https://adventofcode.com/2024) - Save to `inputs/2024/day_X.txt`
- [Advent of Code 2023](https://adventofcode.com/2023) - Save to `inputs/2023/day_X.txt`
- [Advent of Code 2022](https://adventofcode.com/2022) - Save to `inputs/2022/day_X.txt`

Input files are gitignored to respect Advent of Code's request not to share personal puzzle inputs.