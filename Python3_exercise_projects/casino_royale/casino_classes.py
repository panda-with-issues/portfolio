from random import randint, shuffle, randrange

class Games:

    def __init__(self, name, rules, choices, action):
        self.name = name
        self.rules = rules
        self.choices = choices # this is a list of things you can bet on
        self.action = action # this will be printed just to give a friendly ui

    def strfy_modifier(self):
        print("The win is 1x.")

    def strfy_choices(self):
        print("\nYou can choose {}.".format(" or ".join(self.choices)))

    def has_won(self, bet, result):
        if bet == result:
            print("Chanté, you win!")
            return True    
        print("Sashé, you lose...")
        return False
    
    def is_sure(self, bet):
        check_out = input("\nAre you really sure you want to bet on {}? [y/n] ".format(bet)).strip().lower()
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

    def draw(self, deck=game_deck):
        deck_copy = deck.copy()
        shuffle(deck_copy)
        your_card = deck_copy.pop(randrange(0, len(deck_copy)))
        my_card = deck_copy.pop(randrange(0, len(deck_copy)))
        print("You drew {}.".format(your_card))
        print("I drew {}.\n".format(my_card))
        return your_card, my_card

    def get_result(self, your_card, my_card, figures_to_value=figures_to_value):
        if type(your_card) is str:
            your_card = figures_to_value[your_card]
        if type(my_card) is str:
            my_card = figures_to_value[my_card]
        if your_card > my_card:
            print("Chanté, you win!")
            return "win"
        elif your_card == my_card:
            print("Oh my, it's a tie!")
            return "tie"
        else:
            print("Sashé, you lose...")            
            return "loss"     


class Roulette(Games):

    # build table layout as a matrix 3x13
    table = [[0, 0, 0]]
    table_row = []
    for num in range(1, 37):
        table_row.append(num)
        if len(table_row) == 3:
            table.append(table_row)
            table_row = []

    # build the list of red numbers: the first 5 odd numbers, then skip 2, then the next 4 even numbers and repeat
    red_nums = []
    i = 0
    for num in range(1, 37):
        if i < 5 and num % 2 == 1:
            red_nums.append(num)
            i += 1
        elif i == 5 and num == red_nums[-1] + 3:
            red_nums.append(num)
            i += 1
        elif 5 < i <= 9 and num % 2 == 0:
            red_nums.append(num)
            i += 1
        if i == 9:
            i = 0

    # build the list of black numbers. This can't be easily done with a comprehension with conditional filter ([num if num not in red_rums]) because of the wierd
    # scope of comprehension, which can't access external variables unless it is only one and is the outermost iterator.
    # Hence I will use a longer but plain loop to afford the same task (another work-around would be declaring the comprehension as instance variable in the constructor,
    # because doing this the comprehension will widen its scope to the __init__'s scope, that is the whole class)
    black_nums = []
    for num in range(1, 37):
        if num not in red_nums:
            black_nums.append(num)

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

    # map the name of every chance simple with its bet and word to be printed in formatted string
    chances_simples = {
        "Rouge": [red_nums, "red"],
        "Noir": [black_nums, "black"],
        "Manque": [[num for num in range(1, 19)], "low"],
        "Passe": [[num for num in range(19, 37)], "high"],
        "Pair": [[num for num in range(1, 37) if num % 2 == 0], "even"],
        "Impair": [[num for num in range(1, 37) if num % 2 == 1], "odd"]
    }

    natural_from_1 = [n for n in range(1, len(bet_types_details)+1)]
    # this dict maps a natural number with a type of bet
    bets_input_for_user = {n:bet for n, bet in zip(natural_from_1, bet_types_details.keys())}

    # Call with num_row, to get table printed with row counted. The first row counted will be [0].
    # Call no_zero to make the numeration start at the [1, 2, 3] row.
    # Calling the function with no_zero True but num_row False will not produce any rows numeration.
    # Call with num_col to have the columns numerated at the bottom of the table
    # Call with num_dozen to have dozens numerated
    def print_table(self, num_row=False, no_zero=False, num_col=False, num_dozen=False):
        separator = ['-' for i in range(16)]

        # make separator longer in case of rows numeration or dozen numeration, in order to line up with vertical bars
        if num_row or num_dozen:
            separator.append("    ")
            separator[-1], separator[0] = separator[0], separator[-1]
        
        # make a longer separator to limit dozens
        if num_dozen:
            dozens_separator = ['-' for i in range(20)]
            strfd_dozens_separator = "".join(dozens_separator)
            counters = ['3rd', '2nd', '1st']
        
        str_separator = "".join(separator)
        str_table = ['', str_separator] # '' is here to have a blank line before the table's beginning 
        for row in self.table:
            str_row = []

            # logic to have rows counted
            if num_row:
                if no_zero:
                    num = str(self.table.index(row))
                else:
                    num = str(self.table.index(row) + 1)
                if num == '0':
                    str_row.append("   ")
                elif len(num) < 2:
                    str_row.append(num + ": ")
                else:
                    str_row.append(num + ":")

            # logic to have dozen numbered
            if num_dozen:
                if (self.table.index(row) + 2) % 4 == 0: # print number at rows with indices 2, 6, 10
                    counter = counters.pop()
                    str_row.append(counter)
                else:
                    str_row.append("   ")

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
            
            # mark dozens limits
            if num_dozen and self.table.index(row) % 4 == 0:
                str_table.append(strfd_dozens_separator)
            else:

                str_table.append(str_separator)
        
        # logic to have columns counted
        if num_col:
            numeration_row = []
            for i in range(1, 4):
                numeration_row.append("  {}  ".format(i))
            strfd_numeration_row = "".join(numeration_row)
            str_table.append(strfd_numeration_row)

        strfd_table = '\n'.join(str_table)
        print(strfd_table)
    
    def strfy_modifier(self, bet_type, bet_types_details=bet_types_details):
        print("The win is {}x.".format(bet_types_details[bet_type][1]))

    def bet_is_valid(self, bet, table=False, choices=False, carré=False):
        try:
            bet = int(bet)    
        except ValueError:
            print("Please insert a number written in digits.")
            return False
        if table:
            if bet not in range(37):
                print("Please choose a number on the roulette's table.")
                return False
            return True
        if choices:
            if bet not in choices:
                if carré:
                    print("That number can't be an upper left corner!")
                    return False
                print("Please choose a number in the displayed list.")
                return False
            return True       

    # Items are too few to justify a binary search algorithm, and I have to return the row index instead of the number index. In this case there's no valid reason
    # to worry about a N runtime (N=13), so the search algorithm will be linear.
    def get_row_idx(self, number):
        for row in self.table:
            if number in row:
                return self.table.index(row)

    def get_num_idx_in_row(self, number):
        row_idx = self.get_row_idx(number)
        row = self.table[row_idx]
        return row.index(number)

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
                    validation = input("Is this ok? [y/n] ").strip().lower()
                    if validation == 'y':
                        return chosen_bet, modifier
        
    def get_bet(self, bet_type, chances_simples=chances_simples):       

        if bet_type == "Plein":
            self.print_table()
            while True:
                bet = input("\nChoose which number you want to bet on: ").strip()
                if self.bet_is_valid(bet, table=True):
                    if self.is_sure(bet):
                        # because every ther type of bet is a list type object and because the has_won() method works with the "in" operator, even this single bet
                        # must be turned in a list
                        return [int(bet)]

        if bet_type == 'Cheval':
            self.print_table()
            while True:
                first_number = input("\nChoose the first number you want to bet on: ").strip()
                if self.bet_is_valid(first_number, table=True):
                    first_number = int(first_number)
                    bet_row_idx = self.get_row_idx(first_number)
                    bet_row = self.table[bet_row_idx]
                    first_number_idx = self.get_num_idx_in_row(first_number)
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
                    
                    choices.sort() # because the maximum length of choices is 4, we can afford a runtime of N^2 and use the python built-in bubble sort method
                    second_number = input("Choose a number adjacent to {first}: {choices} ".format(first=first_number, choices=choices)).strip()
                    if self.bet_is_valid(second_number, choices):
                        bet = [first_number, int(second_number)]
                        if self.is_sure(bet):
                            return bet
        
        if bet_type == "Transversale Plein":
            self.print_table(num_row=True)
            choices = [i+1 for i in range(len(self.table))]
            while True:
                num_row = input("\nChoose which row you want to bet on: [1-13] ").strip()
                if self.bet_is_valid(num_row, choices=choices):
                    num_row = int(num_row)
                    # zero game
                    if num_row == 1:
                        bet = [0, 2]
                        third_num = input("\nChoose which number will complete the traverse: [1, 3] ").strip()
                        if self.bet_is_valid(third_num, choices=[1, 3]):
                            bet.append(int(third_num))
                            bet.sort()
                        else:
                            continue
                    else:    
                        bet = self.table[num_row-1]
                    if self.is_sure(bet):
                        return bet

        if bet_type == "Carré":
            self.print_table()
            while True:
                upper_left_corner = input("\nChoose the number that will be the upper left corner of the square: ").strip()
                choices = [0] + [i for i in range(33) if i % 3 != 0]
                if self.bet_is_valid(upper_left_corner, choices=choices, carré=True):
                    upper_left_corner = int(upper_left_corner)
                    # zero game
                    if upper_left_corner == 0:
                        bet = [0] + self.table[1]
                    else:
                        bet = [upper_left_corner]
                        upper_left_corner_row_idx = self.get_row_idx(upper_left_corner)
                        upper_left_corner_row = self.table[upper_left_corner_row_idx]
                        upper_left_corner_idx = self.get_num_idx_in_row(upper_left_corner)
                        bet.append(upper_left_corner_row[upper_left_corner_idx + 1])
                        next_row = self.table[upper_left_corner_row_idx + 1]
                        bet.extend(next_row[upper_left_corner_idx:upper_left_corner_idx+2])
                    if self.is_sure(bet):
                        return bet

        if bet_type == "Transversale Simple":
            self.print_table(num_row=True, no_zero=True)
            while True:
                first_row_idx = input("\nChoose the first traverse you want to bet on: [1-12] ").strip()
                choices = [i for i in range(1, len(self.table))]
                if self.bet_is_valid(first_row_idx, choices=choices):
                    first_row_idx = int(first_row_idx)
                    adjacents_rows_ids = []
                    if first_row_idx > 1:
                        adjacents_rows_ids.append(first_row_idx - 1)
                    if first_row_idx < 12:
                        adjacents_rows_ids.append(first_row_idx + 1)
                    if len(adjacents_rows_ids) == 1:
                        bet = self.table[first_row_idx] + self.table[adjacents_rows_ids[0]]
                    else:                        
                        adjacent_row_idx = input("\nChoose which adjacent traverse will complete your bet: {} ".format(adjacents_rows_ids)).strip()
                        if self.bet_is_valid(adjacent_row_idx, choices=adjacents_rows_ids):
                            bet = self.table[first_row_idx] + self.table[int(adjacent_row_idx)]
                        else:
                            continue
                    bet.sort()
                    if self.is_sure(bet):
                        return bet

        if bet_type == "Colonne":
            self.print_table(num_col=True)
            while True:
                col_idx = input("\nChoose which column you want to bet on: [1-3] ").strip()
                if self.bet_is_valid(col_idx, choices=[1, 2, 3]):
                    col_idx = int(col_idx) - 1
                    bet = [row[col_idx] for row in self.table if row[col_idx] != 0]
                    if self.is_sure(bet):
                        return bet

        if bet_type == "Douzaine":
            self.print_table(num_dozen=True)
            while True:
                num_dozen = input("\nChoose which dozen you want to bet on: [1-3] ")
                if self.bet_is_valid(num_dozen, choices=[1, 2, 3]):
                    dozen_coefficient = int(num_dozen) - 1
                    bet = [num + 12 * dozen_coefficient for num in range(1, 13)]
                    if self.is_sure(bet):
                        return bet

        if bet_type in chances_simples:
            bet = chances_simples[bet_type][0]
            print("\nYou have bet on every {chance} number ({list}).".format(
                chance = chances_simples[bet_type][1],
                list = ', '.join([str(num) for num in bet])
                ))
            return bet

    def get_result(self):
        result = randint(0, 36)
        print("...the ball stops in {num}, {color}!\n".format(
            num = result,
            color = "red" if result in self.red_nums else "black" 
        ))
        return result

    def has_won(self, bet, result):
        if result in bet:
            print("Chanté, you win!")
            return True    
        print("Sashé, you lose...")
        return False