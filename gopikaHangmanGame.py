import random

words = ["python", "computer", "program", "hangman", "student"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts, used = 6, []

print("Welcome to Hangman! You have 6 chances.")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha() or guess in used:
        print("Invalid or already used letter!")
        continue

    used.append(guess)
    if guess in word:
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

    print(" ".join(guessed))

print("You Win! 🎉" if "_" not in guessed else f"You Lose! 💀 The word was: {word}")

