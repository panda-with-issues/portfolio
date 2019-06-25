from random import randint, shuffle, randrange

#Write your game of chance functions here

class Games:

    def __init__(self, name, rules, choices, action):
        self.name = name
        self.rules = rules
        self.choices = choices # this is a list of things you can bet on
        self.action = action # this will be printed just to give a friendly ui

    def strfy_modifier(self):
        print("The win is 1x.")

    def strfy_choices(self):
        print("You can choose {}.".format("or ".join(self.choices)))

    def has_won(self, bet, result):
        if bet == result:
            print("Chanté, you win!")
            return True    
        print("Sashé, you lose...")
        return False
    
    def is_sure(self, bet):
        check_out = input("Are you really sure you want to bet on {}? [y/n] ".format(bet)).strip().lower()
        if check_out == 'y':
            return True
        return False       

class FlipCoin(Games):

    def get_result(self):
        percentage = randint(0,100)
        if percentage <= 50:
            print("...it's head!\n")
            result = 'head'
        else:
            print("...it's tail!\n")
            result = 'tail'
        return result


class ChoHan(Games):

    def get_result(self):
        dice_1 = randint(1,6)
        dice_2 = randint(1,6)
        print("...it's {} and {}!".format(dice_1, dice_2))
        if (dice_1 + dice_2) % 2 == 0:
            print("The sum is even!\n")
            result = 'even'
        else:
            print("The sum is odd!\n")
            result = 'odd'
        return result


class Battle(Games):

    deck = [i for i in range(1,11)]
    figures = ['J', 'Q', 'K', 'A']
    deck.extend(figures)
    game_deck = []
    for i in range(4):
        game_deck.extend(deck)
    figures_values = [i for i in range(11, 15)]
    figures_to_value = {figure: value for figure, value in zip(figures, figures_values)}

    def __init__(self, name, rules, action):
        self.name = name
        self.rules = rules
        self.action = action

    def draw(self, deck=game_deck):
        deck_copy = deck.copy()
        shuffle(deck_copy)
        print(self.action)
        your_card = deck_copy.pop(randrange(0, len(deck_copy)))
        my_card = deck_copy.pop(randrange(0, len(deck_copy)))
        print("You drew {}.".format(your_card))
        print("I drew {}.\n".format(my_card))
        return your_card, my_card

    def has_won(self, your_card, my_card, figures_to_value=figures_to_value):
        if type(your_card) is str:
            your_card = figures_to_value[your_card]
        if type(my_card) is str:
            my_card = figures_to_value[my_card]
        if your_card > my_card:
            return True
        elif your_card == my_card:
            return
        else:
            return False     


class Roulette(Games):

    table = [
        [0, 0, 0],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18],
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27],
        [28, 29, 30],
        [31, 32, 33],
        [34, 35, 36]
    ]

    # this dict maps every possible roulette's bet with its rules and modifier
    bet_types_details = {
        "Plein": ["You can choose only one number!", 35],
        "Cheval": ["You can choose two adjacent numbers on the table, vertically or horizontally.", 17],
        "Transversale Plein": ["You can choose a row on the table, or 0 and 2 with either 1 or 3.", 11],
        "Carré": ["You choose four numbers that share a corner.", 8],
        "Transversale Simple": ["You bet on two adjacent rows.", 5],
        "Colonne": ["You choose all numbers in a column.", 2],
        "Douzaine": ["You can choose all numbers in the first 4 rows, or from the 5th to the 8th, or in the last 4 rows.", 2],
        "Rouge": ["You choose all red numbers.", 1],
        "Noir": ["You choose all black numbers.", 1],
        "Manque": ["You choose all numbers between 1-18.", 1],
        "Passe": ["You choose all numbers between 19-36.", 1],
        "Pair": ["You choose all even numbers.", 1],
        "Impair": ["You choose all odd numbers.", 1]
    }

    natural_from_1 = [n for n in range(1, len(bet_types_details)+1)]

    # this dict maps a natural number with a type of bet
    bets_input_for_user = {n:bet for n, bet in zip(natural_from_1, bet_types_details.keys())}

    def __init__(self, name, rules, action):
        self.name = name
        self.rules = rules
        self.action = action

    def print_table(self):
        separator = ['-' for i in range(16)]
        str_separator = "".join(separator)
        str_table = ['', str_separator]
        for row in self.table:
            str_row = []
            if self.table.index(row) == 0:
                str_row.append('|      0       |')
            else:
                for n in row:
                    if row.index(n) == 0:
                        str_row.append('|')
                    if n < 10:
                        str_row.append(str(n) + '  |')
                    else:
                        str_row.append(str(n) + ' |')
            strfd_row = " ".join(str_row)
            str_table.append(strfd_row)
            str_table.append(str_separator)
        strfd_table = '\n'.join(str_table)
        print(strfd_table)
    
    def strfy_modifier(self, bet_type, bet_types_details=bet_types_details):
        print("The win is {}x.".format(bet_types_details[bet_type][1]))

    def bet_is_valid(self, bet):
        try:
            bet = int(bet)    
        except ValueError:
            print("Please insert a number written in digits.")
            return False
        if int(bet) not in range(37):
            print("Please choose a number on the roulette's table")
            return False
        else:
            return True

    # Items are too few to justify a binary search algorithm, and I have to return the row index instead of the number index. In this case there's no valid reason
    # to worry about a N runtime (N=13), so the search algorithm will be linear.
    def get_row_idx(self, number):
        for row in self.table:
            if number in row:
                return self.table.index(row)

    def get_bet_type_and_modifier(self, input_lst=bets_input_for_user, bet_details=bet_types_details, valid_input=natural_from_1):
        print("Which type of bet do you want to do?\n")
        for key, value in input_lst.items():
            print("{}: {}".format(key, value))
        while True:
            n_chosen = input("\nEnter the number of the bet you want to do. Type h for help: ").strip().lower()
            if n_chosen == 'h':
                for key, details in bet_details.items():
                    print("\n{}: {}". format(key, details[0]))
                    self.strfy_modifier(key)
                    continue
            else:
                try:
                    n_chosen = int(n_chosen)
                except ValueError:
                    print("Please enter a number.")
                    continue
                if n_chosen not in valid_input:
                    print("Please enter a number associated with a bet.")
                    continue
                else:
                    chosen_bet = input_lst[n_chosen]
                    rules, modifier = bet_details[chosen_bet]
                    print("\nYou chose a {} bet.".format(chosen_bet))
                    print(rules)
                    self.strfy_modifier(chosen_bet)
                    validation = input("Is this right? [y/n] ").strip().lower()
                    if validation == 'y':
                        return chosen_bet, modifier
        
    def get_bet(self, bet_type):       
        self.print_table()

        if bet_type == "Plein":
            while True:
                bet = input("\nChoose which number you want to bet on: ")
                if self.bet_is_valid(bet):
                    if self.is_sure(bet):
                        return bet

        if bet_type == 'Cheval':
            while True:
                first_number = input("\nChoose the first number you want to bet on: ")
                if self.bet_is_valid(first_number):
                    first_number = int(first_number)
                    bet_row_idx = self.get_row_idx(first_number)
                    bet_row = self.table[bet_row_idx]
                    first_number_idx = bet_row.index(first_number)
                    choices = []

                    # add horizontal adjacents
                    if first_number == 0:
                        choices.extend(self.table[1])
                    else:
                        if first_number_idx - 1 >= 0: 
                            choices.append(bet_row[first_number_idx-1])
                        if first_number_idx + 1 < 3:
                            choices.append(bet_row[first_number_idx+1])

                    # add vertical adjacents
                    if first_number != 0: # this to prevent a double 1 in choices
                        if bet_row_idx > 0:
                            precedent_row = self.table[bet_row_idx - 1]
                            choices.append(precedent_row[first_number_idx])
                        if bet_row_idx < len(self.table)-1:
                            succesive_row = self.table[bet_row_idx + 1]
                            choices.append(succesive_row[first_number_idx])
                    
                    choices.sort()
                    print(choices)
"""
        "Cheval": ["You can choose two adjacent numbers on the table, vertically or horizontally.", 17],
        "Transversale Plein": ["You can choose a row on the table, or 0 and 2 with either 1 or 3.", 11],
        "Carré": ["You choose four numbers that share a corner.", 8],
        "Transversale Simple": ["You bet on two adjacent rows.", 5],
        "Colonne": ["You choose all numbers in a column.", 2],
        "Douzaine": ["You can choose all numbers in the first 4 rows, or from the 5th to the 8th, or in the last 4 rows.", 2],
        "Rouge": ["You choose all red numbers.", 1],
        "Noir": ["You choose all black numbers.", 1],
        "Manque": ["You choose all numbers between 1-18.", 1],
        "Passe": ["You choose all numbers between 19-36.", 1],
        "Pair": ["You choose all even numbers.", 1],
        "Impair": ["You choose all odd numbers.", 1]
"""

            

def greet(game_name):
    print("You chose to play {}!".format(game_name))
  
def get_money_bet():
    print("You have {} coins.".format(money))
    while True:
        money_bet = input("How many moneys do you want to bet? ").strip()
        try:
            money_bet = int(money_bet)
        except ValueError:
            print("Write in digint the amount of money you want to bet\n")
            continue
        if money_bet <= 0:
            print("You must bet at least 1 coin!\n")
            continue
        if money_bet > money:
            print("You don't have enough money!\n")
            continue
        else:
            return money_bet

########################
# THIS MUST BE DEBUGGED
####################### 
# game is a subGames object
def get_bet(game):
    while True:
        bet = input("What will you bet on? ").strip().lower()
        if bet in game.choices:
            if game.is_sure(bet):
                return bet
        else:
            print("Please enter a valid bet")

def want_continue():
    valid_input = ['y', 'n']
    while True:
        choice = input("Do you want to give it another try? [y/n] ").strip().lower()
        if choice not in valid_input:
            print("Please digit 'y' for yes or 'n' for no.")
            continue
        if choice == 'y':
            return True
        if choice == 'n':
            return False

# game is a subGames object
def game_routine(game):
    greet(game.name)
    print(game.rules)
    game.strfy_modifier()
    game.strfy_choices()

    while True:
        bet = get_bet(game.choices)
        money_bet = get_money_bet()
        
        print(game.action)
        result = game.get_result()

        global money
        if game.has_won(bet, result):
            print("You win {} coins.".format(money_bet))
            money += money_bet
        else:
            print("You lose {} coins.".format(money_bet))
            money -= money_bet

        if not want_continue():
            break

# battle is an instance of Battle
def battle_routine(battle):
    greet(battle.name)
    print(battle.rules)
    battle.strfy_modifier()

    while True:
        money_bet = get_money_bet()

        your_card, my_card = battle.draw()

        global money
        if battle.has_won(your_card, my_card):
            print("Chanté, you win!")
            print("You win {} coins.".format(money_bet))
            money += money_bet
        elif battle.has_won(your_card, my_card) is None:
            print("Oh my, it's a tie!")
            print("No coins won nor lost.")
        else:
            print("Sashé, you lose...")
            print("You lose {} coins.".format(money_bet))
            money -= money_bet

        if not want_continue():
            break

# roulette is an instance of Roulette
def roulette_routine(roulette):
    greet(roulette.name)
    print(roulette.rules)
    bet_type, modifier = roulette.get_bet_type_and_modifier()

flip_coin = FlipCoin(
    "Flip Coin",
    "You win if you guess which side the coin will land on.",
    ['head', 'tail'],
    "\nCoin tossed!\n...\n..."
)

cho_han = ChoHan(
    "Cho-Han",
    "You win if you guess whether the sum of two rolled dice is even or odd.",
    ['even', 'odd'],
    "\nrolling dice!\n...\n..."
)

battle = Battle('Battle',
    "You'll draw a random card from a deck and so I will. You win if your card is higher than mine.",
    "\nDrawing cards...\n...\n..."
)

roulette = Roulette(
    "Roulotte",
    "You win if the ball stops on one of the numbers you bet on.",
    "\nRien ne va plus! Ball is spinning...\n...\n..."
)

bet_type, modifier = roulette.get_bet_type_and_modifier()
bet = roulette.get_bet(bet_type)