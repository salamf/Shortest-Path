# Shortest-Path

A city is modeled as a two dimensional table. This program gets the minimum
number of moves to get from cell A to cell B on the table using a graph data structure. In each move, we can either go
right, go left, go up, or go down one cell in the table. We cannot make a diagonal move. Also,
we can only move to a cell if the cell is not blocked, and if we do not leave the table.

## Input Format
The first line of the input contains a positive integer 𝑛. In the next lines, the city is described as
an 𝑛 × 𝑛 table. There are 𝑛 lines where each line has 𝑛 characters. Each character is one of the
following:
1) A '.' cell represents an intersection that is in good shape and can be used for the commute.
2) A '#' cell represents a blocked intersection that cannot be used.
3) An 'A' shows the starting point.
4) A 'B' shows the destination.

## Constraints

1) 1 < 𝑛 ≤ 1000
2) There is exactly one 'A' cell and one 'B' cell in the input.
Output Format
If it is possible to reach from cell 'A' to cell 'B', print the minimum number of moves required to
do so. If not, print the word "IMPOSSIBLE".
