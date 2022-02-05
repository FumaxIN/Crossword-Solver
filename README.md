# Crossword Solver

Solves a sqare(nxn) crossword puzzle.

## Running

#### Requirements

* [Python](https://www.python.org/downloads/)
* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/install/)

#### Steps
Download the file

```shell
https://github.com/FumaxIN/Crossword-Solver.git
```
Switch to the directory
```shell
cd Crossword-Solver
```
Run the command
```shell
python crossword.py
```

## How it works

* Enter the order of crossword(n).
    
* Enter each character individualy
    
* Crossword table ccreated
    
* All the words are now listed
    
* Example:

![crossword format](https://user-images.githubusercontent.com/40835240/152645725-85978db8-a2a1-487b-9f9e-169eb6f7fc16.png)


boy
boyo
bat
tree
ree
cat
aba
ton
tin
rat
rato
oxo
atop
top
oozy
fiz

# Note:
As this is just a side project to practice pandas and numpy, this may not be very efficient and comes with some constraints:
* Diagonally it can only find one word.
* Diagonal search is limited to Left to Right diagonal only.
* In any direction, search will happen in a straight line, i.e. no reverse search

Well, I really wanted to overcome these constraints, but with colleges reopening and my other priorities I am currently unable to. Might do in future.

