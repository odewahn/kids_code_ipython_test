from random import randint

def get_turn_total(player):
    total = 0
    print "It's {}'s turn!".format(player)
    cont = True
    while cont:
        print "Total so far for this turn:", total
        roll = randint(1, 6)
        if roll == 1:
            print "Eek! A one!"
            return 0
        else:
            print "You rolled a", roll
            total += roll
        cont = get_continue("Roll? ")
    return total

def get_continue(prompt):
    while True:
        cont = raw_input(prompt)
        if cont == "":
            print "Sorry, you have to give me something!"
        elif cont[0].lower() == 'y':
            return True
        elif cont[0].lower() == 'n':
            return False
        else:
            print "Huh?"

def get_players():
    while True:
        num = raw_input("How many players? ")
        try:
            num = int(num)
            break
        except Exception, e:
            print "Sorry, that's not valid."

    players = {}
    for i in range(num):
        while True:
            name = raw_input("Player {} name: ".format(i))
            if not name in players:
                players[name] = 0
                break
            else:
                print "Sorry, that name is taken."
    return players

def print_rules():
    print "Each player takes turns rolling a single die."
    print "The player can choose to hold whenever they want,"
    print "but if they get a one, their total is set to zero"
    print "and their turn ends."
    print "\nThe first player to reach 100 wins."

def print_scores(players):
    for player in players:
        print "{} has {} points.".format(player, players[player])

def main():
    print_rules()
    running = True
    winner = None
    # This is the main program loop
    while running:
        players = get_players()
        while not winner:
            for player in players:
                total = get_turn_total(player)
                players[player] += total
                print_scores(players)
                if players[player] >= 100:
                    break
            for player in players:
                if players[player] >= 100:
                    winner = player
        print "The winner was {}!".format(winner)
        running = get_continue("Play again?")         


if __name__ == '__main__':
    main()