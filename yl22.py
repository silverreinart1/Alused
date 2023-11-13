import random

while True:
    user_action = input("Kas (kivi, paber, käärid)?: ")
    possible_actions = ["kivi", "paber", "käärid"]
    computer_action = random.choice(possible_actions)
    print(f"\nSina {user_action}, Arvuti {computer_action}.\n")

    if user_action == computer_action:
        print(f"vali {user_action}. See oli viik! ")
    elif user_action == "kivi":
        if computer_action == "käärid":
            print("Sa oled võitja! WWW")
        else:
            print("Anlaki! LLL")
    elif user_action == "paber":
        if computer_action == "kivi":
            print("Sa oled võitja! WWW")
        else:
            print("Anlaki! LLL")
    elif user_action == "käärid":
        if computer_action == "paber":
            print("Sa oled võitja! WWW")
        else:
            print("Anlaki! LLL")

    play_again = input("Uuesti? (ja/ei): ")
    if play_again.lower() != "ja":
        break