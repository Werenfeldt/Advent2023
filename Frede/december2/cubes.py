RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14
game_id_sum = 0

def transform_grabs(string_list):
    grabs_list = []
    for grab in string_list:
        items = grab.split(",")

        grabs_tuple = ()
        for g in items:
            number, color = g.split()
            grabs_tuple = (color, int(number))
            grabs_list.append(grabs_tuple)
    return grabs_list

def check_game(grabs_list):
    for color, number in grabs_list:
        if color == "red" and number > RED_LIMIT:
            return False
        elif color == "green" and number > GREEN_LIMIT:
            return False
        elif color == "blue" and number > BLUE_LIMIT:
            return False
    return True

with open('input.txt') as s:
    for line in s:
        game, rounds = line.split(":")
        game_id = int(game.split()[1])
        grabs = rounds.strip().split(";")

        grablist = transform_grabs(grabs)
        
        if check_game(grablist):
            game_id_sum += game_id

print("Sum of game_ids: ", game_id_sum)
