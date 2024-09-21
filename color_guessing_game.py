import random
balance = 1000

while True:
    colors = ["red", "blue", "green", "yellow", "purple"]
    correct_color = random.choice(colors)
    chosen_color = input("Enter a color (e.g., red, blue, green): ")
    if chosen_color.lower() == correct_color:
        balance += 100
        print(f"Congratulations! You won ₹100. Your new balance is ₹{balance}.")
    else:
        balance -= 110
        print(f"Oops! You lost ₹110. Your new balance is ₹{balance}.")
    play_again = input("Do you want to play again? (yes/no): ")
    
    if play_again.lower() != ("yes"):
        break

print("Thanks for playing! Have a great day!")
