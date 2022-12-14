# advent-of-code-2022
Advent of Code 2022. Written in python3.

## Testing
You can test the outputs in the following ways. To see all days completd, scroll down to the bottom.

#### ./aoc/main.py
You can execute `./aoc/main.py` python3 exectuable. Which will give you output to each Day i've completed and each part (each day has two parts). If something fails the basic `assert` statments will fail the program.

```
(.venv) dave@Davids-MBP advent-of-code-2022 % ./aoc/main.py
--- Day 1: Calorie Counting ---
--- PASS. Day 1. Part 1 Answer: 70613 ---
--- PASS. Day 1. Part 2 Answer: 205805 ---

--- Day 2: Rock Paper Scissors ---
--- PASS. Day 2. Part 1 Answer: 14163 ---
--- PASS. Day 2. Part 2 Answer: 12091 ---

--- Day 3: Rucksack Reorganization ---
--- PASS. Day 3. Part 1 Answer: 8515 ---
--- PASS. Day 3. Part 2 Answer: 2434 ---
```

#### ./test/test_aoc.py
You can run the PyTest `python3 -m pytest test/test_aoc.py` found in this file `./test/test_aoc.py` to get a more comprehensive output. But, for advent of code, this is overkill, as it runs a basic test on the given file. I wrote these to learn some more.

```
(.venv) dave@Davids-MBP advent-of-code-2022 % python3 -m pytest test/
============================= test session starts ==============================
platform darwin -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/dave/workspace/github/personal/advent-of-code-2022
collected 10 items                                                             

test/test_calorie_counting.py ...                                        [ 30%]
test/test_rock_paper_scissors.py ...                                     [ 60%]
test/test_rucksack.py ....                                               [100%]

============================== 10 passed in 0.01s ==============================
```

## Completed Days
The following Days have been completed.

- [x] [--- Day 1: Calorie Counting ---](https://adventofcode.com/2022/day/1)
- [x] [--- Day 2: Rock Paper Scissors ---](https://adventofcode.com/2022/day/2)
- [x] [--- Day 3: Rucksack Reorganization ---](https://adventofcode.com/2022/day/3)
- [ ] [--- Day 4: Camp Cleanup ---](https://adventofcode.com/2022/day/4)

***Number of Stars - 6***
