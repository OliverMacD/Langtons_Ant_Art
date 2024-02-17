# Langtons_Ant_Art
The purpose of this project is to use the Langton's Art Turing Machine to create art using a physical display

## What is Langton's Ant
From wikipedia, "Langton's ant is a two-dimensional universal Turing machine with a very simple set of rules but complex emergent behavior. It was invented by Chris Langton in 1986 and runs on a square lattice of black and white cells.[1] The universality of Langton's ant was proven in 2000.[2] The idea has been generalized in several different ways, such as turmites which add more colors and more states." (A)

### Langton's Ant  Standard Rules
- If the ant is on a White Square, turn 90 degrees CW, flip the color of the square, and move forward one space
- If the ant is on a Black Square, turn 90 degrees CCW, flip the color of the square, and move forward one space

## Plans for Adapting the Rules
Similar to traditional extensions to multiple colors, this program will utilize multiple colors to show the ant's path. The difference here is that instead of creating a new RL sequence, the original rule will be kept but the effects of the rule will change as described below.

### New Rules
- If the ant is on a Colored Square, turn 90 degrees CW, multiply the value of the square by -1, and move forward one space
- If the ant is on a Black Square, turn 90 degrees CCW, multiply the value of the square by -1 and add 1 to the value of the square, and move forward one space
- If the ant tries to move into a wall, it will turn 180 degrees before moving again

### Value Visualization
- All tiles with a value > 0 will be displayed with a color that is tied to the given number
- All tiles with a value < 0 will be displayed by a black square
- All tiles revert to 0 when they hit a max of N

# Current Progress
The project is currently in its early stages, a table of the progress on the individual milestones can be found below. Futher information on the different milestones can be found under the respective section including smaller more detailed milestones.

| Milestones       | Python Simulation | Arduino Bit Matrix | Large Scale Art Piece  |
|------------------|-------------------|--------------------|------------------------|
| Current Progress | Not Started       | Not Started        | Not Started            |   
| Last Update      | 02.16.2024        | 02.16.2024         | 02.16.2024             |

## Python Simulation
**Goal:** Create a python version of the display to show what the ant's path might look like and get a good understanding of the projects direction.

**Progress:** Not Started

The simulation is run on a jupyter notebook in python 3.12.0. To run the simulation, the following packages are needed on top of a default conda environment:
- notebook
- matplotlib

## Arduino Bit Matrix
**Goal:** Create a small scale version of the project using an arduino and basic off the shelf components.

**Progress:** Not Started

## Large Scale Art Piece
**Goal:** Create the full large scale art piece.

**Progress:** Not Started

# Sources
(A) https://en.wikipedia.org/wiki/Langton%27s_ant
