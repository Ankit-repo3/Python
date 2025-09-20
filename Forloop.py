for i in range(10):              # 0 to 9
    print("Number:", i)          # print number 0 to 9 next line



secret_number = 6
attempts = 3

for attempt in range(attempts):
    guess = int(input("guess number between 1 to 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")