from tinydb import TinyDB

def save_players(players):
    players_table = TinyDB('players_table.json')
    players_table.truncate() # clear the table first
    for player in players:
        serialized_player = {
         'name':player.name, 
         'birth':player.birth,
         'elo':player.elo,
         'gender':player.gender
        }

        players_table.insert(serialized_player)

def save_games(rounds,games,rounds_in_tournament,games_in_round):
    games_table = TinyDB('games_table.json')
    games_table.truncate() # clear the table first

    for i in range(rounds_in_tournament):
        for j in range(games_in_round):
            serialized_games = {
            'numéro de la ronde:': i+1,
            'table n°:'          : j+1,
            'joueurs'            : f"{rounds[i].pairing_players[j][0].name_elo} -contre- {rounds[i].pairing_players[j][1].name_elo}",
            'résultat de la partie': f"({rounds[i].pairing_players[j][0].score_game}-{rounds[i].pairing_players[j][1].score_game})"
            }
    games_table.insert(serialized_games)





"""

for key,value in games.tables.items():
                after_round.add_row(str(key), value[0].name_elo, 
                str(value[0].score_after_last_game),
                 f"({rounds.pairing_players[i][0].score_game}-{rounds.pairing_players[i][1].score_game})", 
                 value[1].name_elo, str(value[1].score_after_last_game))
                i+=1




    print()
    print('affiche tout \n')
    print(players_table.all(),'\n')

    print('affiche que les noms\n')
    for item in players_table:
        print(item['name'])
       
"""














"""
class Player:
def __init__(self, name, age):
self.name = name
 self.age = age
player = Player(name='John', age=22)
Je peux sérialiser l'instance comme ceci :
serialized_player = {
 'name': player.name, 
 'age': player.age
}
Une instance sérialisée peut être reconvertie en une instance comme suit :
name = serialized_player['name']
age = serialized_player['age']
player = Player(name=name, age=age)
Pour sauvegarder plusieurs joueurs en utilisant TinyDB, tu dois d'abord sérialiser 
toutes les instances de joueurs, puis les charger dans la table des joueurs comme 
ceci :
from tinydb import TinyDB
db = TinyDB(‘db.json’)
players_table = db.table(‘players’)
players_table.truncate() # clear the table first
players_table.insert_multiple(serialized_players)
Pour recharger les joueurs sérialisés, tu peux faire ceci :
serialized_players = players_table.all()

"""

