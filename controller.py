class Controller:

    player_no_play_list = []
    move_player = ''

    def manage_odd_nomber_players(players, rounds, pn, round_number, games_in_round, played=False):
        if pn % 2 == 0:
            pass
        else:
            if round_number == 1:
                if played == True:
                    print(f'le joueur {players[pn-1].name_elo} ne joue pas cette ronde et gagne 1 point')
                    players[pn-1].score_after_last_game += 1
                    Controller.move_player = players[pn-1]

            else:
                if played == False:
                    find = False
                    i= games_in_round 
                    while find == False:
                        i-=1
                        for j in range(2):
                            if rounds.pairing_players[i][j].name in Controller.move_player.opponent:
                                print()
                                Controller.no_play = rounds.pairing_players[i][j].name_elo
                                Controller.move_player.opponent.remove(rounds.pairing_players[i][j].name)
                                rounds.pairing_players[i][j].score_after_last_game +=1
                                rounds.pairing_players[i].insert(j,Controller.move_player)
                                del rounds.pairing_players[i][j+1]
                                find = True
                                break
                    
                if played == True:
                    print(f'\n le joueur {Controller.no_play} ne joue pas cette ronde et gagne 1 point \n')
                    
    def manage_user_main():
        select_pn = False
        while select_pn == False:
            pn = input("veuillez entrer le nombre de joueurs (un nombre entre 4 et 100000)")
            try: 
                pn = int(pn)
                if pn >=4 :
                    select_pn = True
            except ValueError:
                print("\n Oops!  Ce n'est pas un mombre valide... \n")

        select_rounds_in_tournament = False
        while select_rounds_in_tournament == False:
            rounds_in_tournament = input("veuillez entrer le nombre de rondes(tour de jeu)")
            try: 
                rounds_in_tournament = int(rounds_in_tournament)
                if rounds_in_tournament <= int(pn/2)*2-1:
                    select_rounds_in_tournament = True
            except ValueError:
                print("\n Oops!  Ce n'est pas un mombre valide... \n")
        return pn,rounds_in_tournament

    def manage_user_details(game_type, place, date):
        print(f'\n Le tournoi {game_type} se déroule le {date} à {place}')
        choice = input("Entrer 'y ou Y' pour yes,\
         \n si vous voulez modifier les paramètres par défauts \
         \n ou une autre touche pour passer")
        if choice.lower() == "y":
            date = input('entrer la date \n')
            place = input('entrer le lieu \n')
            keys = ['1', '2', '3']
            values = ['bullet(3min)', 'blitz(5min)', 'partie rapide(20min)']
            time_control = dict(zip(keys,values))
            for key , value in time_control.items():
                print(key,':',value)
            select_key = 'a'
            while select_key not in keys:  
                select_key = input('veuillez entrer 1,2 ou 3')
            game_type = time_control[select_key]

        return game_type, place, date

    def verify_data(tournament_table, players_table, games_table, results_table):
        choice = input("voulez-vous inspecter les données sauvegardées? \
            \n entrez 'y ou Y' pour yes")
        if choice.lower() == "y":
            print()
            print('affiche la sauvegarde "tournoi" \n')
            print(tournament_table.all(),'\n')
            print()
            print('affiche la sauvegarde "joueurs" \n')
            print()
            for item in players_table:
                print(item)
            print()
            print('affiche tout "les parties" \n')
            print()
            for item in games_table:
                print(item)
            print()
            print('affiche tout "résultats par ronde" \n')
            for item in results_table:
                print(item)