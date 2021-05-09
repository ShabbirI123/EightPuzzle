# 8-Puzzle
Python script is for solving the"8-puzzle" game.

This is a python script we developed for solving the tile sliding [8-puzzle game](https://en.wikipedia.org/wiki/15_puzzle).

## Input format
Input files are plain text, written as six lines: the start state and goal state.
States are space-delineated. One must include the numbers 0-8, where `0` represents the empty space, and `1`-`8` the 8 
tiles of the puzzle.
Here is an example of a properly formatted state: 

```
1 2 0
3 4 6
5 7 8
```

## How to run

`8-Puzzle.py` reads from standard input. Use an IDE and just push the run button or your integrated 
CLI and go to the directory and type:`python.exe 8-Puzzle.py`. 

## Example 
Here is an example:

### Input 

```
Enter the start state matrix 
1 2 0
3 4 5
6 7 8

Enter the goal state matrix 
1 2 3
4 5 6
7 8 0
```

### Command line

```
python.exe 8-Puzzle.py
```

### Output

```
1 2 3
4 5 6
7 8 0

Steps: < number of needed steps> 
```

OR IF THE CURRENT STATE AND GOAL STATE IS UNREACHABLE

```
Your Goal state is unreachable
```