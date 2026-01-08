import random
def play_game():  # Wrap in function
    # Your code above
    secret = random.randint(1,100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
      try:
          guess = int(input("Enter your guess: "))
          attempts += 1
          if guess < 1 or guess > 100:
              print("Guess 1-100")
              attempts -= 1
              continue
          if guess == secret:
              print(f"Correct in {attempts} attempts.")
              break
          elif guess < secret:
              print("Lower")
              continue
          else:
              print("Higher")
              continue
      except:
          print("Input only be Integer")
          continue
    else:
      print(f"Game Over! was secret {secret}!")
    print("Game Completed")
    return attempts < max_attempts  # True if won
    

while True:
    won = play_game()
    if input("Play again? (y/n): ").lower() != 'y':
        break

