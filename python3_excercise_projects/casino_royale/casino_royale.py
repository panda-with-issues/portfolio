from casino_classes import FlipCoin, ChoHan, Battle, Roulette
  
def get_money_bet():
    print("\nYou have {} coins.".format(money))
    while True:
        money_bet = input("How many coins do you want to bet? ").strip()
        try:
            money_bet = int(money_bet)
        except ValueError:
            print("Write in digit the amount of coins you want to bet\n")
            continue
        if money_bet <= 0:
            print("You must bet at least 1 coin!\n")
            continue
        if money_bet > money:
            print("You haven't got enough coins!\n")
            continue
        else:
            return money_bet

# game is a subGames object
def get_bet(game):
    while True:
        bet = input("\nWhat will you bet on? ").strip().lower()
        if bet in game.choices:
            if game.is_sure(bet):
                return bet
        else:
            print("Please enter a valid bet")

def want_continue():
    valid_input = ['y', 'n']
    while True:
        choice = input("\nDo you want to give it another try? [y/n] ").strip().lower()
        if choice not in valid_input:
            print("Please digit 'y' for yes or 'n' for no.")
            continue
        if choice == 'y':
            return True
        if choice == 'n':
            return False

# game is a subGames object
def game_routine(game):

    # welcome routine
    print("You chose to play {}!".format(game.name))
    print(game.rules)
    if type(game) != Roulette:
        game.strfy_modifier()
    if game.choices:
        game.strfy_choices()

    # game routine starts: first ask to bet on something
    while True:
        modifier = 1
        if game.choices:
            bet = get_bet(game)
        if type(game) == Roulette:
            bet_type, modifier = game.get_bet_type_and_modifier()
            bet = game.get_bet(bet_type)
            print(bet)
        
        #ask how many money user want to bet
        money_bet = get_money_bet()
        stakes = money_bet * modifier
        
        # process results of game
        print(game.action)
        if type(game) == Battle:
            your_card, my_card = game.draw()
            result = game.get_result(your_card, my_card)
        else:
            result = game.get_result()

        global money
        if type(game) != Battle:
            if game.has_won(bet, result):
                print("You win {} coins.".format(stakes))
                money += stakes
            else:
                print("You lose {} coins.".format(money_bet))
                money -= money_bet
        else:
            if result == "tie":
                print("No coins won nor lost.")
            elif result == "win":
                print("You win {} coins.".format(stakes))
                money += stakes
            else:
                print("You lose {} coins.".format(stakes))
                money -= money_bet            

        if not want_continue():
            break

"""# battle is an instance of Battle
def battle_routine(battle):
    greet(battle.name)
    print(battle.rules)
    battle.strfy_modifier()

    while True:
        money_bet = get_money_bet()

        your_card, my_card = battle.draw()

        global money
        if battle.has_won(your_card, my_card):
            print("You win {} coins.".format(money_bet))
            money += money_bet
        elif battle.has_won(your_card, my_card) is None:
            print("No coins won nor lost.")
        else:
            print("You lose {} coins.".format(money_bet))
            money -= money_bet

        if not want_continue():
            break

# roulette is an instance of Roulette
def roulette_routine(roulette):
    greet(roulette.name)
    print(roulette.rules)

    while True:
        bet_type, modifier = roulette.get_bet_type_and_modifier()"""

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

battle = Battle(
    'Battle',
    "You'll draw a random card from a deck and so I will. You win if your card is higher than mine.",
    None,
    "\nDrawing cards...\n...\n..."
)

roulette = Roulette(
    "Roulette",
    "You win if the ball stops on one of the numbers you bet on.",
    None,
    "\nRien ne va plus! Ball is spinning...\n...\n..."
)

money = 100
game_routine(battle)
