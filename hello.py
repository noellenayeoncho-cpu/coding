import random
secret_number=random.randint(1, 100)
attempts=0
print("Welcome to the game.")
print("This is a life or death situation.")
print("If you don't guess it right, I will fire you.")
print("Imagine what your dog might think about you then.")
while True:
    guess=int(input("Enter your guess. Remember, your life depends on it: "))
    attempts+=1
    
    if guess<secret_number:
        print("Too low. This is what your dog thinks of you now:( TRY AGAIN! ITS SERIOUS!")
    elif guess>secret_number:
        print("Too high. Brink of death. ARE YOU KIDDING ME? THINK MORE!")
    else:
        print("Correct! Wow, you escaped.")
        break    