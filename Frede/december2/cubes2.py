powersum = 0

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
    redcount = 0
    greencount = 0
    bluecount = 0

    for color, number in grabs_list:
        if color == "red" and number > redcount:
            redcount = number
        elif color == "green" and number > greencount:
            greencount = number
        elif color == "blue" and number > bluecount:
            bluecount = number
        
    return redcount * greencount * bluecount

with open('input.txt') as s:
    for line in s:
        game, rounds = line.split(":")
        game_id = int(game.split()[1])
        grabs = rounds.strip().split(";")

        grablist = transform_grabs(grabs)
        
        power = check_game(grablist)
        powersum += power
    print("Final powersum:", powersum)
