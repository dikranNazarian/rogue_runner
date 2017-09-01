from msvcrt import getch
import os

obstacles2 = {'obstacle_list':  '#', 'obs3':'/', 'obs4':'|','obs5':'-', 'obs6':'\\', 'obs7':'0' }



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
        elif key_press == 119:
            level2[player_position_y][player_position_x] = "@"
            player_position_y += -1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_y += 1
                    level2[player_position_y][player_position_x] = "@"
        elif key_press == 97:
            level2[player_position_y][player_position_x] = "@"
            player_position_x += -1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_x += 1
                    level2[player_position_y][player_position_x] = "@"
        elif key_press == 100:
            level2[player_position_y][player_position_x] = "@"
            player_position_x += 1
            for value in obstacles2.values():
                if level2[player_position_y][player_position_x] == value:
                    player_position_x += -1
                    level2[player_position_y][player_position_x] = "@"
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

main2()

# SOME USEFUL CODE I MAY NEED TO USE LATER FOR WRITING OUT HIGH SCORES
'''def logprint(string_to_log):
  new_file = open('log_file.txt', 'a')
  new_file.write(string_to_log)
  new_file.write('\n')
  new_file.close()'''