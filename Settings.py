import os.path
import json


class Settings:
    settings = {
        "numDecks": 1,
        "promptName": True,
        "adminMode": False,
        "starting_bal": 100
    }

    def __init__(self):
        if os.path.exists("settings.json"):
            s = open("settings.json")
            self.settings = json.load(s)
        else:
            with open("settings.json", "w") as outfile:
                json.dump(self.settings, outfile)

    def get_num_decks(self):
        return self.settings['numDecks']

    def set_num_decks(self, value):
        self.settings['numDecks'] = value

    def get_prompt(self):
        return self.settings['promptName']

    def set_prompt(self, value):
        self.settings['promptName'] = value

    def get_admin_mode(self):
        return self.settings['adminMode']

    def set_admin_mode(self, value):
        self.settings['adminMode'] = value

    def set_starting_bal(self, value):
        self.settings['starting_bal'] = value

    def get_starting_bal(self):
        return self.settings['starting_bal']

    def settings_menu(self):
        print("1. Change Number of Decks\n"
              "2. Prompt Name on Start\n"
              "3. Turn on Admin Mode\n"
              "4. Change Starting Bal\n"
              "5. Exit and Save Settings\n")
        choice = int(input("Enter a number between 1 and 4: "))
        while choice is not type(int) or choice < 0 or choice > 4:
            print("You did not enter a valid integer.")
            choice = int(input("Enter a number between 1 and 4: "))

        if choice == 1:
            choice = int(input("How many decks do you want to play with? "))
            while choice is not type(int):
                choice = int(input("Please enter a valid integer: "))
            self.set_num_decks(choice)
        elif choice == 2:
            choice = input("Would you like to prompt for name at start of program? ")
            while choice != "Y" or "N":
                choice = (input("Enter a valid option: "))
            if choice == "Y":
                self.set_prompt(True)
            else:
                self.set_prompt(False)
        elif choice == 3:
            choice = input("Would you like to turn on admin mode? ")
            while choice != "Y" or "N":
                choice = (input("Enter a valid option: "))
            if choice == "Y":
                self.set_admin_mode(True)
            else:
                self.set_admin_mode(False)
        elif choice == 4:
            choice = int(input("What would you like the starting balance to be? "))
            while choice is not type(int):
                choice = int(input("Please enter a valid integer: "))
            self.set_starting_bal(choice)
        elif choice == 5:
            with open("settings.json", "w") as outfile:
                json.dump(self.settings, outfile)
            print("Settings saved successfully")
