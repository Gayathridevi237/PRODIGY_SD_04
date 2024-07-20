PRODIGY_SD_04

SUDOKO SOLVER:

CONCEPT IN THIS TASK 4 :

1.We  Create a program that solves Sudoku puzzles automatically. The program  take an input grid representing an unsolved Sudoku puzzle and 
use an algorithm to fill in the missing numbers.

2.This program creates a graphical user interface (GUI) for solving Sudoku puzzles using the PyQt5 library. The interface allows users to input a Sudoku puzzle, 
solve it with a single button click, or clear the grid to input a new puzzle. The program uses a backtracking algorithm to solve the puzzle.

REQUIREMENTS for the PyQt5 Sudoku Solver Program:


Software Requirements:

Python:
        Ensure that Python is installed on your system. Python 3.x is recommended


 PyQt5:

Install the PyQt5 library for creating the graphical user interface.

Functional Requirements:

Sudoku Puzzle Input:
        Users must be able to input a Sudoku puzzle into a 9x9 grid.
        Each cell in the grid should accept a single digit (1-9) or be left blank for empty cells
        
IDEOLOGY of the PyQt5 Sudoku Solver Program:

1. User-Centric Design

The primary goal is to create a tool that is easy for users to interact with, allowing them to input, solve, and clear Sudoku puzzles with minimal effort.


2. Algorithmic Problem Solving

The program leverages algorithmic techniques to efficiently solve Sudoku puzzles.

Backtracking Algorithm: The core of the Sudoku solver is the backtracking algorithm, a recursive approach that explores all possible configurations until it finds a valid solution or determines that none exists.
Constraint Satisfaction: The algorithm ensures that the Sudoku rules are followed by checking constraints (no repeated numbers in rows, columns, or 3x3 subgrids) before placing a number in a cell.
Recursive Problem Solving: Learning how to implement recursive functions to explore all possible solutions efficiently.

3.Software Development Practices:

Debugging: Learning how to debug a GUI application and handle common issues that arise in interactive programs.
Testing: Understanding the importance of testing the application with various input scenarios to ensure reliability and correctness.
