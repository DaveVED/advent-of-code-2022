# advent-of-code-2022
Advent of Code 2022. Written in python3.

## Testing
You can test the outputs in the following ways.

##### ./aoc/main.py
You can execute `./aoc/main.py` python3 exectuable. Which will give you output to each Day i've completed and each part (each day has two parts). If something fails the basic `assert` statments will fail the program.

```
(.venv) dave@Davids-MBP advent-of-code-2022 % ./aoc/main.py   
--- Day 1: Calorie Counting ---
--- PASS. Day 1. Part 1 Answer: 70613 ---
--- PASS. Day 1. Part 2 Answer: 205805 ---

--- Day 2: Rock Paper Scissors ---
--- PASS. Day 2. Part 1 Answer: 14163 ---
--- PASS. Day 2. Part 2 Answer: 12091 ---
```

##### ./test/test_aoc.py
You can run the PyTest `python3 -m pytest test/test_aoc.py` found in this file `./test/test_aoc.py` to get a more comprehensive output. But, for advent of code, this is overkill, as it runs a basic test on the given file. I wrote these to learn some more.

```
(.venv) dave@Davids-MBP advent-of-code-2022 % python3 -m pytest test/test_aoc.py
============================= test session starts ==============================
platform darwin -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/dave/workspace/github/personal/advent-of-code-2022
collected 1 item                                                               

test/test_aoc.py .                                                       [100%]

============================== 1 passed in 0.00s ===============================

```

## Completed Days
The following Days have been completed.

- [ x ] [--- Day 1: Calorie Counting ---](https://adventofcode.com/2022/day/1)
- [ x ] [--- Day 2: Rock Paper Scissors ---](https://adventofcode.com/2022/day/2)
- [  ] [--- Day 3: Rucksack Reorganization ---](https://adventofcode.com/2022/day/3)

***Number of Stars - 4***
