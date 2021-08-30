# Tic Tac Toe using Python and Pygame

## Pygame Overview- 
Pygame is a cross-platform set of Python modules which is used to create video games. It consists of computer graphics and sound libraries designed to be used with the Python programming language. pygame is a Python wrapper for the SDL library, which stands for Simple DirectMedia Layer.

## Implementation steps-
1. Create a display board using pygame.display and a console board using numpy.
### Basic Functions for game-
2. draw_board()- Drawing lines on display board( pygame.draw.line )
3. mark_square()- Mark square on console board for a player
4. available_square()- Checks the availability of square
5. is_board_full()- Checks whether the board is full
6. draw_figures()- Draw Circle if player 1 plays and Cross if player 2 plays on display board
7. check_win()- There are 4 ways for a player to win the game- horizontal, vertical, ascending diagonal and descending diagonal. SO, we check for all possibilities if there is a win situation.
8. vertical_line(), horizontal_line(), asc_diagonal_line(), des_diagonal_line()- To make a winning line on display board
9. restart()- Initialize the board and restart the game.
### Game Execution
10. Link the console board to display board.
11. Map the mouse click on display board(as player clicks in a box) to the console board as display board is of image_size * image_size and console board is 3*3.
12. Note that x-coordinate and y-coordinate are in opposite direction for display board and console board.
13. Fill board with alternative player- mark the square, draw figure and check for win everytime. 
14. Switch the player for next move.
15. Adding F5 key to restart the game.

![alt text](https://user-images.githubusercontent.com/67466457/131387172-c2e30287-e23f-4ae9-9973-370e76d0babd.png)
![alt text](https://user-images.githubusercontent.com/67466457/131387182-ac5f7aa9-4e05-4159-a084-8c0201aa8942.png)               
![Screenshot (81)](https://user-images.githubusercontent.com/67466457/131387470-10d39932-3e76-4608-b7e1-74e9b5f4060d.png)
