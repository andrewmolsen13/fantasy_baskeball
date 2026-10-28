class BasketballPlayer(): # Class naming convention uses CapWords/Upper CamelCase

    def __init__(self, name):
        self.name = name
        self.games = {}
        self.games_dad = []

    def add_game (self, game_stats):
        game_number = len(self.games) +1 
        # To simplify this you could just add the game number as the index 
        # and then print "Game " in front of it when printing it out.
        # You could also just use a list. When you iterate over a list you
        # could use the index as the game number. Unless you plan on changing
        # the game number in the future.
        self.games[f"Game {game_number}"] = game_stats

    def add_game_dad(self, game_stats):
        self.games.add(game_stats)

    def display_stats (self):
        print(f"\n{"=" * 32}")
        print(f"{self.name} - Stats")
        print(f"\n{"=" * 32}")
        for game, stats in self.games.items():
            print(f"\n{game}")
            for stat, value in stats.items():
                print(f"{stat.capitalize():<12}: {value}\n")

    def display_stats_dad(self):
        print(f"\n{"=" * 32}")
        print(f"{self.name} - Stats")
        print(f"\n{"=" * 32}")
        for idx, stats in enumerate(self.games_dad):
            print(f"\nGame {idx + 1}")
            for stat, value in stats.items():
                print(f"{stat.capitalize():<12}: {value}\n")

    def calculate_averages(self):
        totals = {}

        for game in self.games.values():
            for stat, value in game.items():
                if stat not in totals:
                    totals[stat] = value
                else:
                    totals[stat] += value

        averages = {}
        for stat, total in totals.items():
            average = total  / len(self.games)
            averages[stat] = average 

        return averages

def get_game_stats ():
    stats = {}
    stats["points"] = get_valid_number("How many points did they score? ") # Nice job creating a function for this so you don't duplicate the checking code.
    stats["assists"] = get_valid_number("How many assists did they have? ")
    stats["rebounds"] = get_valid_number("How many rebounds did they have? ")
    stats["steals"] = get_valid_number("How many steals did they have? ")
    stats["blocks"] = get_valid_number("How many blocks did they have? ")
    stats["minutes"] = get_valid_number("How many minutes did they play? ")
    return stats

def menu():
    menu_options = [1,2,3,4]
    option = get_valid_number("Welcome to your fantasy basketball assistant! What would you like to do?\n"
                   "1. Input new players\n"
                   "2. View stats\n"
                   "3. Compare Players \n"
                   "4. Quit\n")
    
    while int(option) not in menu_options:
        option = input("Please select a valid number 1-4: ")

    return int(option)

def get_valid_number(prompt):
    valid = False

    while not valid: # I see you used the shortened version without the == True here. Nice job.
        try: # Good use of try/except. Also using a specific Error class instead of a generic except statement
            number = int(input(prompt))
            valid = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    return number

def compare_stats(players, comparison):
    comparison_averages = {}
    for name in comparison:
        player = players[name]
        comparison_averages[name] = player.calculate_averages()
    
    print("\nPLAYER COMPARISON")
    print("-" * (15 + 20 * len(comparison)))

    print(f"{'Statistic':<15}", end="")

    for name in comparison:
        print(f"{name:<20}", end="")

    print()
    print("-" * (15 + 20 * len(comparison)))

    # Display averages for each player
    stats = ["points", "assists", "rebounds", "steals", "blocks", "minutes"]

    for stat in stats:
        print(f"{stat.capitalize():<15}", end="")

        for name in comparison:
            average = comparison_averages[name].get(stat, 0)
            print(f"{average:<20.1f}", end="")

        print()

    print("-" * (15 + 20 * len(comparison)))