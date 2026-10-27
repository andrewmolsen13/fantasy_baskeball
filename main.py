
from functions import *
# Open the menu
run = True
players = {}
while run == True:
    menu_option = menu()

    if menu_option == 1:
        #Enter the number of players you want to input
        num_players = int(input("How many players would you like to input? "))



        for i in range(num_players):
            
            name = input(f"What is player {i + 1}'s name? ").lower().title()
            
            players[name] = basketball_player(name)

        # ask number of games 

        num_games = int(input("How many games would you like to input? "))
        for player in players.values():
            for i in range(num_games):
                print(f"Enter stats for {player.name}'s game #{i+1}")
                game_stats = get_game_stats()
                player.add_game(game_stats)
                player.display_stats()

    elif menu_option == 2:
        if len(players) == 0:
            print("There are no players in the database, please input a player")
        else:
            print("What player's stat would you like to see?")
            for name in players:
                print(name)
            player_choice = input("Select a player: ").lower().title()
            if player_choice in players:
                selected_player = players[player_choice]
                selected_player.display_stats()
            else:
                print("Invalid name, please try again")

    elif menu_option == 3:
        run = False