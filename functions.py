class basketball_player():

    def __init__(self, name):
        self.name = name
        self.games = {}

    def add_game (self, game_stats):
        game_number = len(self.games) +1 
        self.games[f"Game {game_number}"] = game_stats

    def display_stats (self):
        print(f"\n{"=" * 32}")
        print(f"{self.name} - Stats")
        print(f"\n{"=" * 32}")
        for game, stats in self.games.items():
            print(f"\n{game}")
            for stat, value in stats.items():
                print(f"{stat.capitalize():<12}: {value}\n")




def get_game_stats ():
    stats = {}
    stats["points"] = get_valid_number("How many points did they score? ")
    stats["assists"] = get_valid_number("How many assists did they have? ")
    stats["rebounds"] = get_valid_number("How many rebounds did they have? ")
    stats["steals"] = get_valid_number("How many steals did they have? ")
    stats["blocks"] = get_valid_number("How many blocks did they have? ")
    stats["minutes"] = get_valid_number("How many minutes did they play? ")
    return stats

def menu():
    menu_options = [1,2,3,4]
    option = input("Welcome to your fantasy basketball assistant! What would you like to do?\n"
                   "1. Input new players\n"
                   "2. View stats\n"
                   "3. Compare Players \n"
                   "4. Quit\n")
    while int(option) not in menu_options:
        option = input("Please select a valid number 1-2: ")

    return int(option)

def get_valid_number(prompt):
    valid = False

    while not valid:
        try:
            number = int(input(prompt))
            valid = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    return number