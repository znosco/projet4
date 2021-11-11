import random


class Game:
    def __init__(self, tables):
        self.tables = tables

    def make_game(rounds_in_tournament):
        game_list = []
        for i in range(rounds_in_tournament):
            game = Game(tables={})
            game_list.append(game)
        return game_list

    def players_score(players, rounds, games_in_round):

        for i in range(games_in_round):
            # for random gain
            cast_point = random.randrange(1, 4)
            if cast_point == 1:
                cast_point_white = 0
                cast_point_black = 1
            if cast_point == 2:
                cast_point_white = 0.5
                cast_point_black = 0.5
            if cast_point == 3:
                cast_point_white = 1
                cast_point_black = 0

            # take into account the ranking of players:
            if (
                rounds.pairing_players[i][0].elo - rounds.pairing_players[i][1].elo
                > 130
            ):
                cast_point_white = 1
                cast_point_black = 0
            if (
                0
                <= rounds.pairing_players[i][0].elo - rounds.pairing_players[i][1].elo
                <= 65
            ):
                cast_point_white = cast_point_black = 0.5
            if (
                rounds.pairing_players[i][1].elo - rounds.pairing_players[i][0].elo
                > 130
            ):
                cast_point_white = 0
                cast_point_black = 1

            # add points
            rounds.pairing_players[i][0].score_game.append(cast_point_white)
            rounds.pairing_players[i][0].score_after_last_game += cast_point_white
            rounds.pairing_players[i][1].score_game.append(cast_point_black)
            rounds.pairing_players[i][1].score_after_last_game += cast_point_black

    def sorted_paring_players(rounds, games_in_round):
        score_list = []
        list_best_in_top = []
        pairing_list_temp = rounds
        for i in range(games_in_round):
            sum_points = (
                rounds.pairing_players[i][0].score_after_last_game
                + rounds.pairing_players[i][1].score_after_last_game
            )
            score_list.append(sum_points)
        i = 0
        while len(score_list) > 0:
            sum_points = (
                pairing_list_temp.pairing_players[i][0].score_after_last_game
                + pairing_list_temp.pairing_players[i][1].score_after_last_game
            )
            if sum_points == max(score_list):
                score_list.remove(max(score_list))
                list_best_in_top.append(
                    [
                        pairing_list_temp.pairing_players[i][0],
                        pairing_list_temp.pairing_players[i][1],
                    ]
                )
                del pairing_list_temp.pairing_players[i]
            i += 1
            if i >= len(score_list):
                i = 0
        rounds.pairing_players = list_best_in_top

    def make_tables(self, players, rounds, games_in_round, round_number):
        keys = list(i for i in range(1, games_in_round + 1))
        values = list(rounds.pairing_players[i] for i in range(games_in_round))
        if round_number == 1:
            pass
        else:
            Game.sorted_paring_players(rounds, games_in_round)
        values = list(rounds.pairing_players[i] for i in range(games_in_round))
        self.tables = dict(zip(keys, values))
