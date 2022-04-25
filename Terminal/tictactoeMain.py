from os import system   # System cls clears the terminal (Windows)
from re import match    # Allows to filter for one specific
import jstyleson        # Jsonc is used to indicate what can be done

# Same as with open for json, but allows comments to be used too
with open(r"terminal\config.jsonc") as jsoncfile:
    config: dict = jstyleson.load(jsoncfile)

SYMBOLS = config["symbols"]         # Gets the dict entries
ROW_LENGTH = config["row-length"]   # If you change the json keys, change this
CLEAR = lambda: system("cls")       # Clear terminal on windows

turn = False    # Player 0 or player 1
played = 0      # How long the game should go on
max_turns = ROW_LENGTH * ROW_LENGTH # Since its a perfect square...
# J = 0, starts at 1, goes to 2. J = 1, starts at 3, ends at 6...
# Depends on row length. The lambda function keeps everything under 80 chars
grid_func = lambda add: [f"{i + add}" for i in range(ROW_LENGTH)]
grid = [grid_func(ROW_LENGTH * j) for j in range(ROW_LENGTH)]

def print_grid() -> None:
    """Iters through the global grid and prints each line, seperated by " | ".
    If the current line isnt the last one, print ______ as it looks nicer,
    otherwise dont
    """
    for line in grid:
        output = " | ".join(line)
        print(output)
        if line != grid[-1]:
            print("-" * len(output))

# The reason a for loop isnt used is because if the input is invalid,
# The round doesnt count
while played < max_turns:
    print_grid()                # Prints the grid
    usr_inp = input("Input a number on the grid: ")
    find = match("\d", usr_inp) # re.match any number
    CLEAR()                     # Clears output
    if find == None:            # If there was no number input
        print("Please input a valid number")
        continue                # Dont make the round count and continue
    find = int(find.group())    # Get the integer from the input
    row = find // ROW_LENGTH    # 4: Thats 1 row down and 1 in (len = 3)
    column = find % ROW_LENGTH  # The remainder of rows bc rows are subtracted
    current_player = SYMBOLS[turn]      # It works with a bool and len = 2 [01]
    if grid[row][column] in SYMBOLS:    # If that current spot is already taken
        print("That spot is taken")     # Continue, dont make the round count
        continue                # This is the reason why a for loop isnt used
    played += 1                 # Only if nothing fails make it count
    grid[row][column] = current_player  # Set the selected position to the val
    turn = not turn             # Make it the other players turn
else:                           # If the game is over
    print_grid()                # Print the grid one last time
    print("Thank you for playing")      # And thank the players
    #~ Add win system
    #~ Dump Winner
