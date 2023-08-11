
# MonsterHunter

A short game built using SQLalchemy and alembic that utilizes a data base referencing tables to perform simple game tasks. 
***

A user can: 

Run and setup the program by running -
- pip install pipenv
- pipenv shell

This will activate the virtual enviornment
- pipenv install
- python seed.py (run this in the ./lib/db directory)

Now to start the game 
- python cli.py (run this in the ./lib directory)
***

The user can use the keyboard to interact with the game, starting with selecting a character that has a randomly generated name, as well as attack, and defense stats. 
***

The user can battle monsters that are in a determined order from weakest to strongest. 
***

The player can "Attack" hit the enemy with your difference of the character attack stat and the monster defense stat (if the monster is defending)
***

The player can "Defend", negate damage dealt from monster equal to the players defense stat
***

The player can "Heal" which heals 10 health points (10% of max health of 100)
***

After defeating a monster the player will be awarded an item that will boost a stat, attack, defense, or both.
***

If the player dies a "You Died" ascii image will display
***

If the player defeates all monsters a "You Win" ascii image will display


