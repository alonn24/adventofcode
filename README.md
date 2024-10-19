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
Make sure you are running python version 3.11 or higher.
Run `pytest` to run all the tests, choose a file to run the tests for a specific day or choose a test case.
```
>
> python -m pytest
> python -m pytest -k test_day17_part1_realcase
> python -m day-xx.py
```

To generate a requirements.txt file, run the following command
```
> pip install pipreqs
> pipreqs . --force
```