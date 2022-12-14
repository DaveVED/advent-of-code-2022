# advent-of-code-2022
[![Actions Status](https://github.com/DaveVED/advent-of-code-2022/workflows/Tests/badge.svg)](https://github.com/DaveVED/<advent-of-code-2022/actions)

All challenges written in `python3`. You can find all days (challenges) completed below under the ***Completed Days*** section. And how to test that, they acutally pass by executing the steps in teh ***Usage*** section.

## Usage
Every challenge has supporting `pytest` ensuring that the following is meet for *both parts* of every question.

- [x] Easy input data provided on Advent of code passes.
- [x] Input data provided on Advent of coded passes.

You can execute all the tests by running `python3 -m pytest test/ `.

```
(.venv) dave@Davids-MBP advent-of-code-2022 % python3 -m pytest test/          
============================= test session starts ==============================
platform darwin -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/dave/workspace/github/personal/advent-of-code-2022
collected 20 items                                                             

test/test_calorie_counting.py ..                                         [ 10%]
test/test_camp_cleanup.py .                                              [ 15%]
test/test_no_space_left_on_device.py ......                              [ 45%]
test/test_rock_paper_scissors.py ...                                     [ 60%]
test/test_rucksack.py ....                                               [ 80%]
test/test_supply_stacks.py ..                                            [ 90%]
test/test_treetop_tree_house.py .                                        [ 95%]
test/test_turning_trouble.py .                                           [100%]

============================== 20 passed in 0.05s ==============================
```

or a specific tests by targeting that test file `python3 -m pytest test/:file_name`.

```
(.venv) dave@Davids-MBP advent-of-code-2022 % python3 -m pytest test/test_supply_stacks.py -s
============================= test session starts ==============================
platform darwin -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/dave/workspace/github/personal/advent-of-code-2022
collected 2 items                                                              

test/test_supply_stacks.py ..

============================== 2 passed in 0.00s ===============================
```

## Completed Days
The following Days have been completed.

- [x] [--- Day 1: Calorie Counting ---](https://adventofcode.com/2022/day/1)
- [x] [--- Day 2: Rock Paper Scissors ---](https://adventofcode.com/2022/day/2)
- [x] [--- Day 3: Rucksack Reorganization ---](https://adventofcode.com/2022/day/3)
- [x] [--- Day 4: Camp Cleanup ---](https://adventofcode.com/2022/day/4)
- [x] [--- Day 5: Supply Stacks ---](https://adventofcode.com/2022/day/5)
- [x] [--- Day 6: Tuning Trouble ---](https://adventofcode.com/2022/day/6)
- [x] [--- Day 7: No Space Left On Device ---](https://adventofcode.com/2022/day/7)
- [x] [--- Day 8: Treetop Tree House ---](https://adventofcode.com/2022/day/8)
- [ ] [--- Day 9: Rope Bridge ---](https://adventofcode.com/2022/day/9)

A full list of challenges can be found [here](https://adventofcode.com/).

***Number of Stars - 16***
