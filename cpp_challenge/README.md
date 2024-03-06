
# cpp challenge

This C++ program is a maze solver. It reads a maze from the standard input, finds the shortest path from the top to the bottom, and prints the path on the standard output.

## How it works

The program uses depth-first search (DFS) to find a path from the top to the bottom of the maze. The DFS starts from every cell in the top row and stops when it reaches the bottom row. The shortest path is then selected from all the paths found.

The maze is represented as a 2D grid of characters, where '.' represents an open cell and '#' represents a wall. The path is marked with numbers starting from '0'.

## Input

The input is a sequence of lines, each containing a string of '.' and '#' characters. Each line represents a row in the maze. The input ends with a line that does not start with '.' or '#'.

## Output

The output is the length of the longest path and the maze with the path marked. If no path is found, the program prints '-1'.


## Demo
https://www.youtube.com/watch?v=GZVqlbaSdTo

