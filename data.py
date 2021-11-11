from tinydb import TinyDB


def save_tournament(place, date, game_type):
    tournament_table = TinyDB('tournament_table.json')
    tournament_table.truncate()  # clear the table first
    serialized_tournament = {'lieu': place,
                             'date': date,
                             'cadence de jeu': game_type
                             }
    tournament_table.insert(serialized_tournament)
    return tournament_table


def save_players(players):
    players_table = TinyDB('players_table.json')
    players_table.truncate()  # clear the table first
    for player in players:
        serialized_player = {
            'name': player.name,
            'birth': player.birth,
            'elo': player.elo,
            'gender': player.gender
        }

        players_table.insert(serialized_player)
    return players_table


def save_games(rounds, games, rounds_in_tournament, games_in_round):
    games_table = TinyDB('games_table.json')
    games_table.truncate()  # clear the table first

    for i in range(rounds_in_tournament):
        for table, player in games[i].tables.items():
            serialized_games = {
                'numéro de la ronde:': i+1,
                'table n°:': table,
                'joueurs': f"{player[0].name}-contre- {player[1].name}",
                'résultat de la partie': f"({player[0].score_game[i]}-{player[1].score_game[i]})"
            }
            games_table.insert(serialized_games)
    return games_table


def save_results(players, rounds, rounds_in_tournament, pn):
    results_table = TinyDB('results_table.json')
    results_table.truncate()  # clear the table first
    for j in range(rounds_in_tournament):
        for i in range(pn):
            serialized_results = {
                'numéro de la ronde:': j+1,
                'joueurs': players[i].name_elo,
                'classement': players[i].rank[j]
            }
            results_table.insert(serialized_results)
    return results_table
