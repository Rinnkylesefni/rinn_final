import random
coin_result = random.randint(1,2)

choice = int(input("Enter your choise (head for1/tail for2) : "))

if choice == 1 and coin_result == 1:
    print("Its head. you won")
elif choice == 1 and coin_result == 2:
    print("its tail. you lose ")
elif choice == 2 and coin_result == 2:
    print("Its tail you won")
elif choice == 2 and coin_result == 1:
    print("Its head. you lose")
  