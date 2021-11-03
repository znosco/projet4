from faker import Faker
import random
import chessplayers
import data
from rounds import Round
from game import Game
from display import Display
from controller import Controller
from tinydb import TinyDB
from rich.console import Console



                  
# main program
players_number_in_tournament = pn = 8
rounds_in_tournament = 4
pn,rounds_in_tournament = Controller.manage_user_main()
round_number = 1
games_in_round = int(pn/2)
random_tournament = True
game_type = 'blitz(5min)'
place = 'Paris'
date = '01/12/2021'
game_type, place, date = Controller.manage_user_details(game_type, place, date)    

#make lists of objects
console = Console()
players = chessplayers.Player.make_players(pn,random_tournament)
rounds = Round.make_rounds(rounds_in_tournament)
games = Game.make_game(rounds_in_tournament)

# tournament begin!
Display.print_welcome(players, console, round_number, pn)

# round1 --> paring --> playing --> get results --> round2...
for i in range(rounds_in_tournament):
    #played = Controller.reset_round()
    rounds[i].pairing(players,games_in_round,round_number,pn)
    games[i].make_tables(players,rounds[i],games_in_round,round_number)
    Controller.manage_odd_nomber_players(players, rounds[i], pn)
    Display.pairing_before_round(players, games[i], console, round_number)
    Game.players_score(players,rounds[i],games_in_round)
    Controller.manage_odd_nomber_players(players, rounds[i], pn, played=True)
    Display.print_score_after_last_round(players, games[i], rounds[i], console ,round_number, pn)
    round_number += 1
#save data and verify    
tournament_table = data.save_tournament(place, date, game_type)
players_table = data.save_players(players)
games_table = data.save_games(rounds,games,rounds_in_tournament,games_in_round)
results_table = data.save_results(players, rounds, rounds_in_tournament, pn)
Controller.verify_data(tournament_table, players_table, games_table, results_table)
