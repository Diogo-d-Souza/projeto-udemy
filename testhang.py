word = list("cavalo")
spaces = []
player_live = 6

for num_letters in range(len(word)):
    spaces.append("_")

while spaces != word:
    player_letter = input("Which letter do you wanna try guess? ")
    for position in range(len(spaces)):
        letter = word[position]
        if letter == player_letter:
            spaces[position] = letter
    if player_letter not in word:
        player_live -= 1
        
            
    print(spaces)
    

print("you win")