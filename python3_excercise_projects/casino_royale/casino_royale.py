from casino_classes import FlipCoin, ChoHan, Battle, Roulette
from highscores import generate_highscore_csv
import csv
  
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
    print("\n\nYou chose to play {}!".format(game.name))
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
        
        if money == 0:
            break            

        if not want_continue():
            break

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

games = [flip_coin, cho_han, battle, roulette]
nums_to_game = {num:game for num, game in zip(range(1, len(games) + 1), games)}

def get_game(input_dict=nums_to_game):
    print("\nThese are the game currently available:")
    for num, game in nums_to_game.items():
        print("{}: {}".format(num, game.name))
    while True:
        num = input("\nPlease enter the number of the game you want to play: [1-{}] ".format(len(games))).strip()
        try:
            num = int(num)
        except ValueError:
            print("Please enter a number written in digits.")
            continue
        if num in input_dict:
            return input_dict[num]
        print("Please choose a number associated with a bet.")

money = 100
loser_string = """\n\nOh no, you have no more coins!\n
Seems like today isn't your day at all...
Don't worry, next time will be better!
Come by soon and thank you for having played with Casinò Royale!"""

# play the game
print("\n\nWelcome to the Casinò Royale!")
name = input("Uh-oh, what's your name again? " ).strip().title()
if len(name) > 8:
    name = name[:8]

#print(f"""Oh my, sure! Here you go, {name}: 100 shiny coins you can use to play all the games you want.
#Be careful though: if you finish them, it's game over.
#Best of luck and have a good time!"""
#    )

while money > 0:
    game = get_game()
    game_routine(game)
    if money == 0:
        print(loser_string)
        break
    want_play_again = input("\nDo you want to play another game? [y/n] ").strip().lower()
    if want_play_again != 'y':
        check_out = input("\nAre you really sure you want to quit the game? [y/n] ").strip().lower()
        if check_out == 'y':
            print("\nThank you for having played with Casino Royale. Come by soon!")
            break

# highscores creation and visualization
generate_highscore_csv(name, money)

with open('.highscores.csv') as f:
    #print header
    separator = ''.join(['=' for i in range(24)])
    blank_line = '|' + ''.join([' ' for i in range(22)]) + '|'
    thin_separator = ''.join(['-' for i in range(24)])
    print('\n\n')
    print(separator)
    print(blank_line)
    print("| BEST  PLAYERS  BOARD |")
    print(blank_line)
    print(separator)
    
    highscores = csv.DictReader(f)
    for line in highscores:
        print(blank_line)
        current_and_position = f"| {line['current'] if line['current'] else ' '}  {line['position']} "
        name = f" {line['name']} "
        while len(name) < 10:
            name += ' '
        coins = f" {line['coins']}"
        while len(coins) < 6:
            coins += ' '
        coins += '|'
        score_line = current_and_position + name + coins
        print(score_line)
    print(separator)