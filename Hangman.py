word = list("cavalo")

spaces = []
player_live = 6
end_of_game = True
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for num_letters in range(len(word)):
    spaces.append("_")

while end_of_game == True:
    player_letter = input("Which letter do you wanna try guess? ")
    for position in range(len(spaces)):
        letter = word[position]
        if player_letter.lower() == letter:
            spaces[position] = letter
    if player_letter.lower() not in word:
        player_live -= 1
        print(stages[player_live])    
    print(spaces)
    if spaces == word:
        print("You win, congratulations! ")
        end_of_game = False
    elif player_live == 0:
        print("You lose :(  Good lucky next time!")
        end_of_game = False

