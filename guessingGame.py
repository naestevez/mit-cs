x = 100
epsilon = 0.01
l = 0
h = x
c = (h+l)/ 2

print ("Please think of a number between 0 and 100!")
print ("Is your secret number " + str(c) + "?")
print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")


if raw_input() == l:
    print("it's lower than 50..hmm")
elif raw_input() == h:
    print("it's higher than 50...hunn")
elif raw_input() == c:
    print(str(c) + " is the right answer?!")
else:
    print("Sorry, I did not understand your input.")
    

