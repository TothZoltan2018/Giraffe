i = 1
while i <= 10:
    print(i)
    i += 1

print("Loop is done.")

# Basic guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
"""
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lost!")
else:
    print("You win!")
"""
# Az en megoldasom egyszerubb:
while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1

if guess != secret_word:
    print("You lost!")
else:
    print("You win!")

# for loop = c# foreach loop
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

for index in range(3, 10):  # 3...9
    print(index)

for index in range(len(friends)):
    print(friends[index])
