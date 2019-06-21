from random import randint

#Write your game of chance functions here

class Games:

    def __init__(self, name, rules, modifier, choices, action):
        self.name = name
        self.rules = rules
        self. modifier = modifier
        self.choices = choices # this is a list of things you can bet on
        self.action = action # this will be printed just to give a friendly ui

    def strfy_modifier(self):
        return "The win is {}x".format(self.modifier)

    def strfy_choices(self):
        return "You can choose {}".format(", ".join(self.choices))

    def has_won(self, bet, result):
        if bet == result:
            print("Congratulations, you won!")
            return True
        else:
            print("Oh no, you lost...")
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
    figures_values = [i for i in range(11, 15)]
    figures_to_value = {figure: value for figure, value in zip(figures, figures_values)}

    def __init__(self, name, rules, modifier):
        self.name = name
        self.rules = rules
        self.modifier = modifier
        

def greet(game_name):
    print("You chose to play {}!".format(game_name))
  
def get_money_bet():
    print("You have {} coins".format(money))
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

def game_routine(game):
    greet(game.name)
    print(game.rules)
    print(game.strfy_modifier())
    print(game.strfy_choices())

    bet = get_bet(game.choices)
    money_bet = get_money_bet()
    stakes = money_bet * game.modifier
    
    print(game.action)
    result = game.get_result()

    global money
    if game.has_won(bet, result):
        print("You win {} coins".format(stakes))
        money += stakes
    else:
        print("You lose {} coins".format(stakes))
        money -= stakes

def battle_routine():
    pass

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
    "You'll draw a random card from a deck and so I will. You win if your card is higher than mine",
    1
)

money = 100
#game_routine(cho_han)
#print(money)

