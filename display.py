from rich.table import Table


class Display:
    def print_welcome(players, console, round_number, pn):
        if round_number == 1:
            print()
            print(
                "-----Bienvenue aux Tournoi international d'échecs OPENCLASSROOMS----- \n"
            )
            print(
                f"---------------------- {pn} particitants-----------------------------\n"
            )

            welcome = Table(show_header=True, header_style="bold magenta")
            welcome.add_column("nom (élo)", style="dim", width=60)
            welcome.add_column("date de naissance")
            for i in range(pn):
                welcome.add_row(players[i].name_elo, players[i].birth)
            console.print(welcome)
        input("appuyer sur une touche pour continuer")

    def pairing_before_round(players, games, console, round_number):
        print()
        print(f"--------appariement avant la ronde:{round_number}-------- \n")
        before_round = Table(show_header=True, header_style="bold magenta")
        before_round.add_column("table n°", width=14)
        before_round.add_column("joueur avec les blancs", style="dim", width=36)
        before_round.add_column("score", style="dim", width=12)
        before_round.add_column("joueur avec les noirs", style="dim", width=36)
        before_round.add_column("score", style="dim", width=12)
        for key, value in games.tables.items():
            before_round.add_row(
                str(key),
                value[0].name_elo,
                str(value[0].score_after_last_game),
                value[1].name_elo,
                str(value[1].score_after_last_game),
            )
        console.print(before_round)
        input("appuyer sur une touche pour continuer")

    def print_score_after_last_round(players, games, rounds, console, round_number, pn):
        players_temp = sorted(
            players, key=lambda x: x.score_after_last_game, reverse=True
        )
        print()
        print(
            f"----------résultat de la partie et scores des joueurs après la ronde: {round_number}"
            " -------------------------------"
        )
        print()

        after_round = Table(show_header=True, header_style="bold magenta")
        after_round.add_column("table n°", width=14)
        after_round.add_column("joueur avec les blancs", style="dim", width=36)
        after_round.add_column("score", style="dim", width=12)
        after_round.add_column(f"résultat de la ronde:{round_number}", width=14)
        after_round.add_column("joueur avec les noirs", style="dim", width=36)
        after_round.add_column("score", style="dim", width=12)
        i = 0
        for key, value in games.tables.items():
            after_round.add_row(
                str(key),
                value[0].name_elo,
                str(value[0].score_after_last_game),
                f"({value[0].score_game[round_number-1]}-{value[1].score_game[round_number-1]})",
                value[1].name_elo,
                str(value[1].score_after_last_game),
            )
            i += 1
        console.print(after_round)

        print()
        print(f" ---------scores et rang après la ronde:{round_number} -------------")
        print()
        result = Table(show_header=True, header_style="bold magenta")
        result.add_column("rang", width=8)
        result.add_column(" joueur(élo)", style="dim", width=36)
        result.add_column("score", style="dim", width=8)
        for i in range(pn):
            same_score = False
            if i == 0:
                j = i + 1
            else:
                if (
                    players_temp[i - 1].score_after_last_game
                    == players_temp[i].score_after_last_game
                ):
                    same_score = True
                if not same_score:
                    j = i + 1
            result.add_row(
                str(j),
                players_temp[i].name_elo,
                str(players_temp[i].score_after_last_game),
            )
            players_temp[i].rank.append(j)
        console.print(result)
        input("appuyer sur une touche pour continuer")
