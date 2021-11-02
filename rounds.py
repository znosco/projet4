
class Round:

    def __init__(self, pairing_players):
        self.pairing_players = pairing_players

    def make_rounds(rounds_in_tournament):
        round_temp = []
        for i in range(rounds_in_tournament):
            rounds = Round(pairing_players=[])
            round_temp.append(rounds)
        return round_temp
            
    def turn_around_me(players, games_in_round, move=1):
        """exemple : if 8 players : 4 tables---> 1 play 5 , 2 play 6, 3 play 7 , 4 play 8
        ---> fixed player[0] and all players turn arround tables
        """
        tables = games_in_round
        player_end_list = players[2*tables-1]
        for i in range(move):
            if tables ==2:
                players.remove(player_end_list)
                players.insert(tables-1,player_end_list)
            else:
                backup_player = player_end_list
                players.insert (tables, players[1])
                players.remove(players[1])
                players.remove(player_end_list)
                players.insert(tables-1,player_end_list)
       
   
    def pairing(self,players,games_in_round,round_number,pn):
        """pairing players for the first round        
        """
       


        def play_game(self, players, games_in_round):
        #add pairing players and del opponent
            for i in range(games_in_round):
                self.pairing_players.append([players[i],
                                            players[i+games_in_round]])
                players[i].opponent.remove(players[i+games_in_round].name)
                players[i+games_in_round].opponent.remove(players[i].name)

        def can_you_play_with_me(players,number_game=0):

            i = number_game
            p1 = players[i].name
            p1_opp = players[i].opponent
            p2 = players[i+games_in_round].name
            no_played_together = p2 in p1_opp
            return no_played_together

        if round_number == 1:
            play_game(self,players,games_in_round)
            
        else:
            def seek(self, players, games_in_round):
                match = 0
                count_len = 0
                n = -0.5
                while match < games_in_round:
                    n += 0.5
                    for j in range(pn-1):
                        count = 0
                        for i in range (games_in_round):
                            delta = abs(players[i].score_after_last_game - players[i+games_in_round].score_after_last_game)
                            no_played_together = can_you_play_with_me(players, number_game=0)
                            if delta <= 0 + n and no_played_together == True:
                                count +=1
                        if match < count:
                            match = count 
                        if match == games_in_round:
                            play_game(self, players, games_in_round)
                            break             
                        else:
                            Round.turn_around_me(players, games_in_round, move=1)
               
            seek(self, players, games_in_round)