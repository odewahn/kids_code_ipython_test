from random import randint

SCORE_TYPES = ("pair", "two pair", "3 of a kind", "4 of a kind", "full house", 
    "small straight", "large straight", "chance", "generala",
    "ones", "twos", "threes", "fours", "fives", "sixes")

def score_dice(dice, scores, score):
    pass

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

    add_score(dice, scores, choice)

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
    get_score_choice(dice, scores)

if __name__ == '__main__':
    main()