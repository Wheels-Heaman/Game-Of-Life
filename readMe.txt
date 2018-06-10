A Simulation Of John Conway's Game of Life that is Boundless.

The Rules:
1. Any live cell with fewer than two live neighbors dies, as if by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Press "R" to generate and random board state.
Press "SPACE" at any time to stop or start the simulation. (This will also print out the board state in a format that can be pasted directly into the code) (I plan to remove this print function and replace it with a read and write function)
Use left mouse click to draw living cells into the board and use right click to kill cells.
Both of these function can be performed while the simulation is running, though most drawn cells tend to die on the next frame.
The number keys have allocated preset board states to demonstrate the sort of simulations that can be created. 

I am working on an "Infinite" version of the program that runs simulations non stop.
It will start a new random board when the previous one gets stuck in a loop.
The longest "Surviving" simulations are saved and can be run again to attempt to find the pattern or long surviving simulations.  