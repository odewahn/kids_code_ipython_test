from random import randint

SCORE_TYPES = ("pair", "two pair", "3 of a kind", "4 of a kind", "full house", 
    "small straight", "large straight", "chance", "generala",
    "ones", "twos", "threes", "fours", "fives", "sixes")

SUM_SCORES = ("pair", "two pair", "3 of a kind", "4 of a kind", "chance",
    "ones", "twos", "threes", "fours", "fives", "sixes")

STATIC_SCORES = {
    "full house": 20,
    "small straight": 25,
    "large straight": 30,
    "generala": 50 
}

def add_option_list(options, num, score_type):
    if options.has_key(score_type):
        options[score_type].append(num)
    else:
        otions[score_type] = [num]

def get_choice_options(dice):
    options = {}
    dice.sort()
    dice_str = ""
    for die in dice:
        dice_str = dice_str+str(die)
    if dice_str in ("12345", "23456"):
        options["large straight"] = None
    if dice_str in ("1234", "2345", "3456"):
        options["small straight"] = None
    for i in "123456":
        if dice_str.count(i) >= 2:
            
        if dice_str.count(i) >= 3:
            if options.has_key("3 of a kind"):
                options["three of a kind"].append(i)
            else:
                options["three of a kind"] = [i]


def get_dice_sum(dice, choice):
    return 0

def add_score(dice, scores, choice):
    if choice in SUM_SCORES:
        pass
    elif choice in STATIC_SCORES.keys():
        pass
    else:
        print "I'm not sure what I should do..."

def draw_dice(dice):
    # Draw the top line
    print "+---+---+---+---+---+"
    # Draw the innards
    print "|",
    for die in dice:
        print str(die) + " |",
    print
    # Draw the bottom line
    print "+---+---+---+---+---+"
    print "  1   2   3   4   5"

def roll_dice(num_dice=5):
    dice = []
    for i in range(num_dice):
        dice.append(randint(1, 6))
    return dice

def discard_dice(dice):
    die = 'x'
    while die[0].lower() != 'r':
        die = raw_input("Which number die would you like to discard (r to roll)? (1-6, r) ")
        if die.isdigit():
            if int(die) - 1 > 6:
                print "Sorry, I can't get rid of", die
                continue
            dice[int(die) - 1] = 0
        elif die[0].lower() != 'r':
            print "Huh?"

def get_new_dice(dice):
    for i in range(5):
        if dice[i] == 0:
            dice[i] = randint(1, 6)

def print_score_sheet(scores):
    print
    num = 1
    for score in SCORE_TYPES:
        if scores[score] == None:
            taken = "[ ]"
        else:
            taken = "[X]"
        print "{taken} {num}. {slot}".format(taken=taken, num=num, slot=score.title())
        num += 1

def add_score(dice, scores, choice):
    choice = SCORE_TYPES[choice]
    if choice == 

def get_score_choice(dice, scores):
    while True:
        choice = raw_input("Which score? ")
        try:
            choice = int(choice) - 1
            if choice > len(SCORE_TYPES):
                print "No good"
            elif scores[SCORE_TYPES[choice]] == None:
                print "Nope"
            else:
                break
        except:
            print "Sorry, that dosn't work"

    return choice

def main():
    scores = {}
    for score in SCORE_TYPES:
        scores[score] = None

    dice = roll_dice()
    draw_dice(dice)
    for i in range(3):
        discard = raw_input("Would you like to discard some of your dice? ")
        if discard[0].lower() == 'n':
            draw_dice(dice)
            break
        discard_dice(dice)
        get_new_dice(dice)
        draw_dice(dice)
    print_score_sheet(scores)
    choice = get_score_choice(dice, scores)
    add_score(dice, scores, choice)

if __name__ == '__main__':
    main()