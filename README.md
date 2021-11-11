# projet4

1) Presentation:

The goal of this project is to create a chess tournament with any number of players (even or odd) and any rounds.
By trying to be as close to reality as possible.

2) The different classes / files and their functions:

a) The main.py file:
>This is the main program, it manages the execution and the order of the various events.
 
b) The Chessplayers class:
>It creates a list of instances of the Chessplayers class.
>The list is sorted by descending order.
Attributes :
- name
- elo (ranking that reflects the strength of the player)
- score_game
- score_after_last_game
- opponent (list of possible opponents)
- gender
- birth
- name_elo
- rank

 c) The Rounds class:
- It manages the pairing of players:
 -->1st round: The players are matched according to their elo (Swiss system).
 -->Next round: The players are paired:
- who have not played together (each player checks that their opponent is on their 'opponent' list, this list is updated with each pairing)
- according to the scores, the program tries to find the combination which corresponds to the smallest difference in points between each player.

d) The Game class:
- It manages the results of the games, the scores and the game tables
-The result of a game is generated randomly but also depends on the strength of each player.
-The pairs of matched Players are ranked by score, the best players play table1, ect ..
 
e) The Controller class:
>Pairings are designed for a number of even players, the Controller class manages (alone), the case where the number of players is odd.
>It also manages user choices and allows verification of recorded data.

d) The Display class;
>It displays:
- The list of players
- For each round:
- The pairing of players (table number, opponent, score, elo)
- The results of the round (results of the games)
- The player who is exempt from playing in case of an odd number of players
-The score and the classification after the round

c) The Data file
>Save tournament data in JSON format.


to create the virtual environment(window's users):
```sh
python -m venv env
pip install -r requirements.txt
```
for activate environment use activate.bat(window's users):
```sh
env/scripts/activate.bat
```
for use the code:
```sh
python main.py
```
