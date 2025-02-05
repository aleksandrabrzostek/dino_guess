import requests
from dinosay import dinoprint, DINO_TYPE
import sys

def main():
    info()
    dino = get_random_dino()[0]
    prompt = get_random_dino()[1]
    ask_and_update(dino, prompt)

def info():
    msg = "Welcome to the DINO GUESS game. You get a random dino to guess. If you lose, you get eaten!\nBut not by me! I don't eat meat... Good luck! You have 10 guesses."
    dinoprint(msg,DINO_TYPE['brachiosaur'])

def get_random_dino():
    dino_url = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"
    r = requests.get(dino_url).json()
    dino_name = r['Name'].upper()
    dino_desc = r['Description']
    return dino_name, dino_desc

def asf_for_prompt(prompt):
    prompt_answer = input("\nDo you want a little clue? [Y/N]: ").strip().upper()
    if prompt_answer == "Y":
        print(prompt, end="\n")

def ask_and_update(dino, prompt):
    count = 10
    letters = list(dino)
    guessed_letters = []
    for x in letters:
        guessed_letters.append("_")

    print(*guessed_letters)

    while "_" in guessed_letters:
        input_letter = input("Type a letter: ").strip().upper()
        for x in range(len(letters)):
            if input_letter == letters[x]:
                guessed_letters[x] = input_letter
        print(*guessed_letters)
        count-=1
        if count == 5:
            asf_for_prompt(prompt)
        if count == 0:
            sys.exit("\nSorry...T-rex is about to eat you!\n")
    sys.exit("\nCongrats! You don't get eaten!\n")
    

if __name__ == "__main__":
    main()
