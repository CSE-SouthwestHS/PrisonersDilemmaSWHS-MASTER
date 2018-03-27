# PrisonersDilemmaSWHS
*Coded by Arthur Goldman (Computer Science Student - Minneapolis Southwest High School, 2017)*

*Brought to you by Gabriel A Pass (PLTW Computer Science Instructor)*

*For more information contact: gabriel@gapmedia.org*

## Requirements

This iterated prisoner's dilemma requires `Python 3.6 or above` and depends on `pandas`.  
Pandas can be installed with:

```
python -m pip install pandas
```

With these Requirements, you are ready to run your tournament.  See the OFFICIAL_RULES for more information the competition.

Note: Python 3.6 is available for Enthought Canopy 2.1 and will come standard in Canopy 2.2
At this time, other IDEs may be easier to use.

## Running a Tournament

To run a tournament, Run `iterated-dilemma.py` with the names of your modules.
For example, if you have team modules named:
```
player1.py
myTeam.py
WinningTeam666.py
/home/Documents/my-python-modules/weSuck.py
```
run `./iterated-dilemma.py foo.py bar.py WinningTeam666.py /home/Documents/my-python-modules/weSuck.py`. Any number of modules can be given.

Alternately, if you've got a directory that contains your modules, and the only `.py` files in it are your modules, you can use the command-line flag `-d <directory-path>`:

```
./iterated-dilemma.py -d modules
```

## Notes & FAQ

Note: In PyCharm and IDEs with a RUN program function, add parameters such as `-d modules` by adding a "Run Configuration" for `iterated-dilemma.py`.  In PyChar, make the following menu selection: [Run] > [Edit Configuration]

Note: If Python files are not set to open in Python (i.e. if `.py` files open in an IDE), You may have to do something like:

```
python iterated-dilemma.py -d modules
python iterated-dilemma.py foo.py bar.py Winningteam666.py /home/Documents/my-python-modules/weSuck.py
python iterated-dilemma.py
```

Each team's module should conform to Python 3.6 and must provide several things:

`team_name`: a string, no more than 16 characters long, containing no newlines or other weird blank space

`strategy_name`: a string, no more than 20 characters long, containing no newlines or other weird blank space

`strategy_description`: a string containing no newlines or other weird blank space

`move(my_moves, their_moves, my_score, their_score)`: a function that returns either `'b'` or `'c'` for BETRAY or COLLUDE. You can also `import GLOBALS` and return `GLOBALS.BETRAY` or `GLOBALS.COLLUDE`. `my_moves` and `their_moves` are strings containing the moves that each player has taken so far in this iterated dilemma, and `my_score` and `their_score` are ints that will usually be negative containing each player's score so far in this round.

FYI: Python 3.6 is required because the code depends on `importlib.util`.
*Enjoy!*
