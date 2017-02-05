
# value = "Hi my name is Garrett! I don't like to fish, I like crafting. I do like eating fish though. Crafting is fun."
value = "Treehouse Rocks. rocks are cool. I like using Treehouse! What do you use?"

def word_count(value):
    word_count = {}
    sentence  = ""
    punctuation = ",.'!?"

    for letter in value:
        if letter not in punctuation:
            sentence += letter.lower()

    for word in sentence.split(' '):
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count

def combo(one, two):
    pairs = []
    for index, item in enumerate(one):
        pairs.append((one[index], two[index]))

    print(pairs)

# combo('hel', [2, 3, 5,])

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    for course, covers in COURSES.items():
        if covers & topics:
            print(course)

def covers_all(topics):
    matched_courses = []
    for course, covers in COURSES.items():
        if topics == topics & covers:
            matched_courses.append(course)
    print(matched_courses)

# covers_all({"input", "strings"})

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

# for tile in TILES:
#     if tile == '||':
#         print('\n')
#     else:
#         print(tile, end='')


BOARD_SIZE = 10
board_heading = [chr(letter) for letter in range(ord('A'), ord('A') + BOARD_SIZE)]

def print_board():
    board = [['0' for space in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]
    return board

def place_ship(location, length, orientation, board, ship):
    board = board

    alpha = ''.join([chr(letter) for letter in range(65,75)]).lower()
    column, row = location
    column = alpha.index(column)

    if orientation.lower() == 'h':
        if '-' in board[row][column:(column + length)]:
            print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship))
        else:
            for space in board[row][column:(column + length)]:
                board[row][column:(column + length)] = ['-' for num in range(length)]
    if orientation.lower() == 'v':
        for board_row in range(column,(column + length)):
            # if board[board_row][column] != '0':
            #     print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship))
            # else:
                board[board_row][column] = '|'

    game_board = board

game_board = print_board()

# should place ship
place_ship(('b',3), 5, 'h', game_board, 'Air Carrier')

# should get a warning and no ship placement
place_ship(('b',5), 5, 'h', game_board, 'Battleship')

# should place ship
place_ship(('a', 5), 3, 'h', game_board, 'Tugboat')
place_ship(('f', 7), 3, 'h', game_board, 'Assault Ship')

# should get a warning and no ship placement
place_ship(('f', 7), 3, 'v', game_board, 'Gun Ship')

print(board_heading)
for row in game_board:
    print(row)
