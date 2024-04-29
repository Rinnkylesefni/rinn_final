answer = 7
guess = int(input("Enter your guess within 1 to 10 : "))
if guess > answer:
    print("wrong guess. try smaller")

elif guess < answer:
    print("Wrong guess. try bigger")

elif guess == answer:
    print("BINGO ")

else:
    print("invalid input. try again")

