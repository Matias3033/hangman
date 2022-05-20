print("Welcome to the execution")

word = input("Insert the word to find\n")

word_list = []

for i in word:
    word_list.append(i)

counter = 0
word_guess = []

while counter < 3:
    chance = input("Guess a letter: ")
    if chance in word_list:
        word_guess.append(chance)
        if len(word_guess) == len(word_list):            
            break
    else:
        print("Wrong")
        counter += 1

if counter < 3:
    print("You win. The word is: " + word)
else:
    print("You died!")

