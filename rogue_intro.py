import os
from msvcrt import getch
import time
import random


def player_health():     #   Figure out how to color variables, otherwise trailing color will effect other functions
    health = 33
    if health >= 50:
        print('\n\n\033[1;32mPlayer HP: ', health)
    elif health <= 49:
        print('\n\n\033[1;32mPlayer HP: \033[1;31m', health)
    if health < 1:
        game_over()


def save_high_score():
    high_score = open('high_score.txt', 'w')
    name = input('Great job! Enter your name to add your score to scoreboard: ')
    f = open('scoreboard.txt', 'w')
    f.write(high_score)
    f.close()


obstacles2 = {'obstacle_list':  '#', 'obs3':'/', 'obs4':'|','obs5':'-', 'obs6':'\\', 'obs7':'0'
           }


def create_level2(filename='level_2.txt'):
    with open(filename, 'r') as f:
        level2 = []
        for i in f:
            level2.append(list(i))
        player_position(level2, 3, 3)
        return level2


def print_level2(level2):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in level2:
        for i in row:
            print(i, end='')


def player_position(level2, player_position_y, player_position_x):
    level2[player_position_y][player_position_x] = '@'


def player_movement(level2, player_position_y, player_position_x):
    while True:
        key_press = ord(getch())
        if key_press == 115:
            level2[player_position_y][player_position_x] = "@"
            player_position_y += 1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_y += -1
                    level2[player_position_y][player_position_x] = "@"
                    player_health()
        elif key_press == 119:
            level2[player_position_y][player_position_x] = "@"
            player_position_y += -1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_y += 1
                    level2[player_position_y][player_position_x] = "@"
                    player_health()
        elif key_press == 97:
            level2[player_position_y][player_position_x] = "@"
            player_position_x += -1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_x += 1
                    level2[player_position_y][player_position_x] = "@"
                    player_health()
        elif key_press == 100:
            level2[player_position_y][player_position_x] = "@"
            player_position_x += 1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_x += -1
                    level2[player_position_y][player_position_x] = "@"
                    player_health()
        print_level2(level2)


def check_player_obstacles2(level2, player_position_y, player_position_x):
    for key, value in obstacles2.items():
        if level2[player_position_y +1][player_position_x] == obstacles2.get(key) and level2[player_position_y -1][player_position_x]  == obstacles2.get(key) and level2[player_position_y][player_position_x+1]  == obstacles2.get(key) and level2[player_position_y][player_position_x-1]  == obstacles2.get(key):
            level2[player_position_y][player_position_x] = '@'
    pass


def add_element_to_level2(level2, player_position_y, player_position_x, char):
    level2[player_position_y][player_position_x] = char


def main2():
    level2 = create_level2()
    player_movement(level2, 3, 3)

#def spike_damage():          ////       # this function gives UnBoundLocal Error because
    #player_health -= 20      ////       # it cannot call player_health before assignment
    #return health            ////       # To Improve : parameters / calling other functions


def create_board():         # customizable board specifications
    board = []
    column = [" "] * 30
    for i in range(1,10):
        board.append(list(column))
    return board


def print_board(board):      # displays the actual board (level)
    for x in range(0, len(board)):
        print("".join(board[x]))


def movement(board = [], player_x=0, player_y=0, current_place=""):  #movement for first level
    if board == []:
        board = create_board()
    obstacles = ["0", "|", "#"]
    damage_objects = [">", "<", "^"]
    next_level = ['%']
    board[3][3] = "0"
    board[2][2] = "0"
    board[10][10] = "#"
    board[5][5] = "<"
    if current_place == "":
        current_place = board[player_y][player_x]
    board[player_y][player_x] = "\033[1;33m@\033[0m"
    #if current_place in damage_objects:                  \\\ THESE 4 LINES ARE WHERE 
        #current_place = board[player_y][player_x]        \\\ DAMAGE WOULD BE CALLED
    #board[player_y][player_x] = "\033[1;33m@\033[0m"     \\\ IF YOU TOUCHED A
    #spike_damage()                                       \\\ DAMAGE_OBJECT
    #if current_place in next_level:                         ///// 
    #    current_place = board[player_y][player_x]           /////    these 5 lines
    #board[player_y][player_x] = "\033[1;33m@\033[0m"        /////    are for calling
    #clear_terminal()                                        /////    the second level
    #main2()                                                 /////    
    for line in board:
        print("".join(line))
    move = input()
    player_health()
    if move == "w":
        if board[player_y - 1][player_x] in obstacles:
            print("Something is in the way")
            movement(board, player_x, player_y, current_place)
        board[player_y][player_x] = current_place
        player_y -= 1
        movement(board, player_x, player_y)
        player_health()
    if move == "s":
        if board[player_y + 1][player_x] in obstacles:
            print("Something is in the way")
            movement(board, player_x, player_y, current_place)
        board[player_y][player_x] = current_place
        player_y += 1
        movement(board, player_x, player_y)
        player_health()
    if move == "a":
        if board[player_y][player_x - 1] in obstacles:
            print("Something is in the way")
            movement(board, player_x, player_y, current_place)
        board[player_y][player_x] = current_place
        player_x -= 1
        movement(board, player_x, player_y)
        player_health()
    if move == "d":
        if board[player_y][player_x + 1] in obstacles:
            print("Something is in the way")
            movement(board, player_x, player_y, current_place)
        board[player_y][player_x] = current_place
        player_x += 1
        movement(board, player_x, player_y)
        player_health()
    else:
        print("Wrong key. You can use only W/S/A/D")
        player_health()


def game_over():    
    clear_terminal()
    play_again = input('You lost, would you like to play again? (yes / no): ')
    if play_again == 'yes':
        start_game_or_boss()
    elif play_again == 'no':
        exit()
    else:
        print("I do not understand, please type yes or no", game_over())


#def map():          \\\\ OLD VERSION OF MAP CREATION, KEEPING IT AROUND JUST INCASE.
    #width = 90
    #height = 30
    #create_board(width, height)


def home_screen(): #Main Title Page with all the starting routes
    start_answer = input('\033[1;33mWould you like to play a game? (yes or no) : ')
    if start_answer == 'yes':
        clear_terminal()
        start_game_or_boss()
    elif start_answer == 'no':
        exit()
    else:
        print("I do not understand, please type yes or no")
        home_screen()


def start_game_or_boss(): # Another pop-up that allows me to navigate through quick testing of certain levels
    next_window = input('\033[1;37mType yes for level 1, skip for level 2, or no for final boss (yes / no / skip): ')
    if next_window == 'yes':
        clear_terminal()
        movement()
        player_health()
    elif next_window == 'no':
        display_final_boss()
        player_health()
    elif next_window == 'skip':
        main2()
    else:
        print ("I do not understand, please type yes or no", start_game_or_boss())


def clear_terminal():
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def boss(digit_list):
    player_lives = 0
    while True:
        mode = input("Select difficulty (easy/medium/hard)")
        if mode == "easy":
            player_lives = 15
            break
        elif mode == "medium":
            player_lives = 10
            break
        elif mode == "hard":
            player_lives = 5
            break      
    while player_lives > 0:
        start_time = time.time()
        time.time()
        while True:
            guess_number = input("choose a 3 digit number")
            if len(guess_number) != 3:
                print("Number has to have exactly 3 digits!")
            else:
                break
        guess_number_list = list(guess_number)
        print(guess_number_list)
        score = 0
        if int(guess_number_list[0]) in digit_list:
            if int(guess_number_list[0]) == digit_list[0]:
                print("hot")
                score += 1
            else:
                print("warm")
        else:
            print("cold")
        if int(guess_number_list[1]) in digit_list:
            if int(guess_number_list[1]) == digit_list[1]:
                print("hot")
                score += 1
            else:
                print("warm")
        else:
            print("cold")
        if int(guess_number_list[2]) in digit_list:
            if int(guess_number_list[2]) == digit_list[2]:
                print("hot")
                score += 1
            else:
                print("warm")
        else:
            print("cold")
        if score == 3:
            end_time = time.time() - start_time
            print("You won! Your time was", (round(end_time, 2)))
            (save_high_score)
            break
        player_lives -= 1
        print("chances left: ", player_lives)
    if score < 3:
        end_time = time.time() - start_time
        print("You lose! Your time was", (round(end_time, 2)))


def reset():
    digit_list = []
    a = random.randint(5,9)
    digit_list.append(a)
    b = random.randint(5,9)
    while b in digit_list:
        b = random.randint(5,9)
    digit_list.append(b)
    c = random.randint(5,9)
    while c in digit_list:
        c = random.randint(5,9)
    digit_list.append(c)
    #print(digit_list)
    boss(digit_list)
    play_again()


def play_again():
    play_again = input("Do you want to play again? (yes/no)")
    if play_again == "yes":
        reset()
    elif play_again == "no":
        exit("Goodbye!")


def display_final_boss(file_name='grim_reaper.txt'):
    # Read ascii art for final boss from file
    f = open(file_name, 'r')
    for line in f:
        print(repr(line.rstrip("\n")))
    reset()


def print_table(inventory):
    start = 0
    column_width = 13
    column2_width = 6
    column3_width = 10
    additional_space = 2
    for element in inventory:
        if len(element) + additional_space > column_width:
            column_width = len(element) + additional_space
        else:
            continue
    sum = 0
    weight = {"Gold": 1, "Healthy pie": 5, "Armor": 15}
    print(inventory)
    print("Inventory:\n")
    print("count".rjust(column2_width), "item name".rjust(column_width), "weight".rjust(column3_width))
    print(("-") * (column_width + column2_width + column3_width + 2))
    for element in inventory:
        print(str(inventory[element]).rjust(column2_width), element.rjust(column_width), str(weight[element]).rjust(column3_width))
        sum = inventory[element] + sum
    print(("-") * (column_width + column2_width + column3_width + 2))
    print("Total number of items: ", sum)
    return inventory


def add_to_inventory(inventory, added_items):
    for element in added_items:
        if element in inventory:
            inventory[element] = inventory[element] + 1
        else:
            inventory[element] = 1
        return inventory


def import_invetory(inventory, filename="Inventory.txt"):
    file = open(filename, 'r')
    import_items = file.read().split(",")
    file.close()
    for element in import_items:
        if element in inventory:
            inventory[element] = inventory[element] + 1
        else:
            inventory[element] = 1
    return inventory


def test():
    inventory = {}
    inventory = import_invetory(inventory)
    print_table(inventory)


def screen_hall_of_fame(filename='scores.txt'):
    f = open(filename, 'r')
    for line in f:
        print(repr(line.rstrip("\n")))
        #f.close()
    print('Highscores : \n Dikran | 1:55 \n Gabriela | 1:54')
    #with open(filename, 'r') as f:            \\\\  I have multiple ways of reading files, this current one
        #clear_terminal()                      \\\\  is not working, but keeping this here to fix later
    #for row in filename:
        #for i in row:
            #print(i, end='')
    

#def print_scores(scores):     Had code here, not in use but may be needed later to get a better score screen
    

def screen_credits(file_name='credits.txt'):
    # Read ascii art for credits from file
    f = open(file_name, 'r')
    for line in f:
        print(repr(line.rstrip("\n")))
    print('\033[1;37min association with Code Cool 2017')
    go_home = input('\033[1;34mPress h to return home')
    if go_home == 'h':
        menu()

        

#def player_money():


def main():
    home_screen()

def menu():     # would have loved for the entire menu (where run starts globally) to work inside function, no luck.
    print(''' \n
\033[1;36m _______  _______  _______           _______  \033[1;31m  _______           _        _        _______  _______ \033[0m
\033[1;36m(  ____ )(  ___  )(  ____ \|\     /|(  ____ \ \033[1;31m (  ____ )|\     /|( (    /|( (    /|(  ____ \(  ____ )\033[0m
\033[1;36m| (    )|| (   ) || (    \/| )   ( || (    \/ \033[1;31m | (    )|| )   ( ||  \  ( ||  \  ( || (    \/| (    )|\033[0m
\033[1;36m| (____)|| |   | || |      | |   | || (__     \033[1;31m | (____)|| |   | ||   \ | ||   \ | || (__    | (____)|\033[0m
\033[1;36m|     __)| |   | || | ____ | |   | ||  __)    \033[1;31m |     __)| |   | || (\ \) || (\ \) ||  __)   |     __)\033[0m
\033[1;36m| (\ (   | |   | || | \_  )| |   | || (       \033[1;31m | (\ (   | |   | || | \   || | \   || (      | (\ (   \033[0m
\033[1;36m| ) \ \__| (___) || (___) || (___) || (____/\ \033[1;31m | ) \ \__| (___) || )  \  || )  \  || (____/\| ) \ \__\033[0m
\033[1;36m|/   \__/(_______)(_______)(_______)(_______/ \033[1;31m |/   \__/(_______)|/    )_)|/    )_)(_______/|/   \__/\033[0m
    ''')
    print('Press 1: To start the game')
    print('Press 2: To view the credits')
    print('Press 3: To view the highscores')
    print('Press 4: To view the game story and how to play')
    print('Press q: to quit')
    return input('What do you want to do? ')
run = menu()
while True:
    if run == '1':
        main()
        break
    elif run == '2':
        screen_credits()
        break
    elif run == '3':
        screen_hall_of_fame()
    elif run == '4':
        print("Welcome to the ROUGE RUNNER game.\nYou went for the evening jogging, but it was dark, foggy and you lost in the woods.\nThere was no one around but the abandoned building. As you decided to cross the non existing doors,\nyou realised that this place is haunted and possesed by weird creatures.\nThe doors you once crossed became a wall. You realised that you are in a labyrinth.\nTo return safely you must find a way out that is located on the opposite part of the building.\nOn your journey you have to concur some random creatures and win the final battle with a boss.\nCollect items that might be useful during the final battle, and collect money. The more you collect, the easier final battle will be.")
        print("\nUse w,s,a,d to move. To collect the item or drink a health potion, press the space bar.")
        break    # break needed otherwise text keeps on duplicating
    elif run == 'q':
        print('Come back soon :)')
        break











