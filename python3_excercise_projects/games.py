from random import randint, shuffle, randrange

#Write your game of chance functions here

class Games:

    def __init__(self, name, rules, modifier, choices, action):
        self.name = name
        self.rules = rules
        self. modifier = modifier
        self.choices = choices # this is a list of things you can bet on
        self.action = action # this will be printed just to give a friendly ui

    def strfy_modifier(self):
        return "The win is {}x.".format(self.modifier)

    def strfy_choices(self):
        return "You can choose {}.".format(", ".join(self.choices))

    def has_won(self, bet, result):
        if bet == result:
            print("Chanté, you win!")
            return True    
        print("Sashé, you lose...")
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

    def __init__(self, name, rules, modifier, action):
        self.name = name
        self.rules = rules
        self.modifier = modifier
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

class Roulotte:

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

# choices is a list type object
def get_bet(choices):
    while True:
        bet = input("What will you bet on? ").strip().lower()
        if bet in choices:
            return bet

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
    print(game.strfy_modifier())
    print(game.strfy_choices())

    while True:
        bet = get_bet(game.choices)
        money_bet = get_money_bet()
        stakes = money_bet * game.modifier
        
        print(game.action)
        result = game.get_result()

        global money
        if game.has_won(bet, result):
            print("You win {} coins.".format(stakes))
            money += stakes
        else:
            print("You lose {} coins.".format(stakes))
            money -= stakes

        if not want_continue():
            break

# battle is an instance of Battle
def battle_routine(battle):
    greet(battle.name)
    print(battle.rules)
    print(battle.strfy_modifier())

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




flip_coin = FlipCoin(
    "Flip Coin",
    "You win if you guess which side the coin will land on.",
    1,
    ['head', 'tail'],
    "\nCoin tossed!\n...\n..."
)

cho_han = ChoHan(
    "Cho-Han",
    "You win if you guess whether the sum of two rolled dice is even or odd.",
    1,
    ['even', 'odd'],
    "\nrolling dice!\n...\n..."
)

battle = Battle('Battle',
    "You'll draw a random card from a deck and so I will. You win if your card is higher than mine.",
    1,
    "\nDrawing cards...\n...\n..."
)
