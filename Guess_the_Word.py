#list of words to pick from
words = ["Adventure", "Chocolate", "Happiness", "Journey", "Reflection", "Galaxy", "Sunshine","Discovery","Euphoria","Friendship","Harmony"]

#choose a word
choose = int(input("Input number between 0-10: "))

#turn word to list
word = words[choose].lower()

word_list = list(word)

#spaces representing number of letters
for _ in word_list:
    print ("-", end=" ")

# num of turns
turns = 12

#true/false
correct = []
wrong = "wrong answer"

guessed = ("Input a single letter: ")


while turns -= 1: 
    print(input(guessed))


if guessed in word_list:
    print(guessed)
else:
    print("_")
