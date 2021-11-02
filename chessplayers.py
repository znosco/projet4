from faker import Faker

import random

class Player:
    def __init__(self,
                 name,
                 elo,
                 score_game,  
                 score_after_last_game,                    
                 opponent,
                 ranking, 
                 gender, 
                 birth,
                 name_elo,
                 ):
        self.birth= birth
        self.name = name
        self.gender = gender
        self.elo = elo
        self.score_game = score_game
        self.ranking = ranking
        self.score_after_last_game = score_after_last_game
        self.opponent = opponent
        self.name_elo = name_elo
    
    def make_fake_list_attributs(self):
        fake = Faker(['fr_FR'])
        birth = fake.date_between(start_date='-75y', end_date='-7y')
        self.birth =str(birth)
        self.elo = random.randrange(1400,2201,10)
        cast_gender = random.randrange(1,3)
        if cast_gender == 1:
            self.gender = 'M'
            self.name = fake.name_male()
        else:
            self.gender = 'F'
            self.name = fake.name_female()


    def make_players(pn,random_tournament):
        players_temp = []
        for i in range(pn):
            player = Player(name='', 
                            elo=0,
                            score_game=0,
                            score_after_last_game=0,
                            opponent=[], 
                            ranking=0, 
                            gender='', 
                            birth='',
                            name_elo='',
                            )
            if random_tournament == True:
                player.make_fake_list_attributs()
            players_temp.append(player)
            players = sorted(players_temp, 
                              key=lambda x: x.elo, reverse=True)      
        def make_opponent(players):
            for i in range(pn):
                for j in range(pn):
                    if j != i:
                        players[i].opponent.append(players[j].__dict__['name'])
        make_opponent(players)
        def make_name_elo(players):
            for i in range(pn):
                players[i].name_elo = f"{players[i].name} ({players[i].elo})"
        make_name_elo(players)

        return players
