"""
Keeping track of a scrabble game
Exercise with validating inputs, dictionaries and object oriented programming in Python3
"""

#mapping letter:points for score calculation
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_to_points = {letter:points for letter, points in zip(letters, points)}

"""
Defining new custom class Player
"""

class Player:

  #giving Player a constructor
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.words_played = []

  #giving each Player a string representation
  def __repr__(self):
    return "A player named {}.".format(self.name)

  #defining play_word() method, which:
  #  1. check whether there's any invalid character in the word
  #  2. append the word in words played dict
  #  3. then convert the word to points
  #  4. print the word's score
  #  5. assign that value to player's points
  def play_word(self):
    #1
    while True:
      word = input().upper()
      invalid_input = 0
      for letter in word:
        if letter not in letters:
          print("Invalid input. Words can be composed only by plain letters. Please check your spell.")
          invalid_input += 1
        else:
          continue
      if invalid_input == 0:
        break      
    #2
    self.words_played.append(word)
    #3
    points = 0
    for letter in word:
      points += letter_to_points[letter]
    #4
    print("Wonderful! You scored {} points.".format(points))
    #5
    self.points += points

"""
Setting up the game
"""

print("Welcome to a new session of Scrabble!")

#getting the number of players and checking whether is a number
print("How many people will play the game?")
while True:
  try:
    num_players = int(input())
  except ValueError:
    print("Invalid input. Please insert a number greater than 1.")
    continue
  if num_players <= 1:
    print("Invalid input. Please insert a number greater than 1.")
    continue
  else:
    break
 

#instanciating a number of players equals to the value given before, each one with a given name
players = {}
for player_num in range(1, (num_players + 1)):
  print("Please insert player {} name:".format(player_num))
  player_name = input().title()
  players[player_num] = Player(player_name)

"""
Play the game
"""

round_count = 1
#beginning round routine
while True:
  for n in range(1, player_num + 1):

    #print the current round when it's up to player 1
    if n == 1:
      print("Round {}.".format(round_count))
    
    #turn routine
    print("It's up to {}. What word did you compose?".format(players[n].name))
    players[n].play_word()
  
  #at round's end, print the total score of each player
  print("It's the end of round {}. Let's see who's winning:".format(round_count))
  for player in players.values():
    print("{player}: {points}.".format(player=player.name, points = str(player.points)))

  #ask whether will be another round
  while True:
    print("Do you want to play another round? [y,n]")
    round_check = input("")
    #checking input's sanity
    if round_check != "y" and round_check != "n":
      print("Invalid input. Please answer y or n.")
    else:
      break
  
  #if there will be another round, update round counter and repeat round routine
  if round_check == "y":
    round_count += 1

  #else break round routine
  else:
    break

"""
End game
"""

#building the final rank
final_scores = {player.points:player.name for player in players.values()}
score_ranking = [score for score in final_scores]
score_ranking.sort()
score_ranking.reverse()
print("This is the final rank:")
for i in range(len(score_ranking)):
  print("{rank}. {player} with {points} points.".format(rank=i+1, player=final_scores[score_ranking[i]], points=score_ranking[i]))

#printing the list of word played by each players
for player in players.values():
  print("The words played by {player} are: {words}".format(player=player.name, words=player.words_played))

#say goodbye and shut down
print("Thank you for having played with me! Hope you had fun!")
input("Press enter to shut me down.")