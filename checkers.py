# Simulating a game of checkers
# Read and parse moves from input file
file1 = open("game1.txt", "r")
file2 = open("game2.txt", "r")
input_f1 = file1.readlines()
input_f2 = file2.readlines()

list_f1 = []
list_f2 = []

for line in input_f1:  # remove white space, split on spaces
    move = line.strip().split(" ")
    list_f1.append((move[0], move[1]))

for line in input_f2:  # remove white space, split on spaces
    move = line.strip().split(" ")
    list_f2.append((move[0], move[1]))

red = list_f2[0::2]     # change from list_f1 to list_f2 to switch between the games
black = list_f2[1::2]   # change from list_f1 to list_f2 to switch between the games
nest_list1 = [red, black]

# Initialize variables and set totals to zero
red_total = 0
black_total = 0
total_moves = 0
red_captures = 0
red_2jumps = 0
black_captures = 0
black_2jumps = 0

# Iterate over all moves in the game
for i in range(len(red)):
    a = abs(int(nest_list1[0][i][0][0]) - int(nest_list1[0][i][1][0]))   # subtracting individual values for a move
    b = abs(int(nest_list1[0][i][0][2]) - int(nest_list1[0][i][1][2]))
    c = int(str(a) + str(b))
    if c == 11:     # if/elif/else statement used to update totals based on the move
        total_moves += 1
    elif c == 22:
        red_total += 1
        red_captures += 1
        total_moves += 1
        print("Red jumped a black piece!")
    else:
        red_total += 2
        red_2jumps += 1
        total_moves += 1
        red_captures += 2
        print("Red double-jumped two black pieces!")
    if red_total >= 12:    # check if red has won
        Winner = "Red"
        break
    x = abs(int(nest_list1[1][i][0][0]) - int(nest_list1[1][i][1][0]))    # subtracting individual values for a move
    y = abs(int(nest_list1[1][i][0][2]) - int(nest_list1[1][i][1][2]))
    z = int(str(x) + str(y))
    if z == 11:    # if/elif/else statement used to update totals based on the move
        total_moves += 1
    elif z == 22:
        black_total += 1
        black_captures += 1
        total_moves += 1
        print("Black jumped a red piece!")
    else:
        black_total += 2
        black_2jumps += 1
        total_moves += 1
        black_captures += 2
        print("Black double-jumped two red pieces!")
    if black_total >= 12:    # check if black has won
        Winner = "Black"
        break

# Output the results
print(f'\n-----Game Stats-----\nWinner: {Winner}\nTotal Moves: {total_moves}\nRed Captures: {red_captures}\n'
      f'Red Double-jumps: {red_2jumps}\nBlack Captures: {black_captures}\nBlack Double-jumps: {black_2jumps}')
