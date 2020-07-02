# PrisonersDilemmaSWHS
#### Coded by [Arthur Goldman](https://github.com/gefjon) (Minneapolis Southwest High School, Class of 2017)
Contributors:
* [Henning Tonko](https://github.com/HenningTonko) Added -r (random) argument (SWHS Class of 2018)
* [Themistocles Megas](https://github.com/Themis3000) Improved code optimization, python 3.8 support, -e argument, & rule compliance. (SWHS Class of 2021)

#### Brought to you by Gabriel A Pass (PLTW Computer Science Instructor)

#### For more information contact: gabriel@gapmedia.org

This is a Python 3 implementation of the age-old problem of logic and game theory.  It was inspired by a Python 2 approach by PLTW (Project Lead the Way) for their Computer Science Principles course.  This implementation of the dilemma was coded from scratch by the Southwest High School students credited above.  It contains no source material other than the age-old dilemma.  Our approach provides a new formulation of the classic conundrum, with new rules, more data on your opponent allowing a more rigorous playing field, and, of course, more new opportunities to cheat ( ͡° ͜ʖ ͡°).  We are providing this new Python 3 Iterated Prisoner's Dilemma to the community of Python students and developers with a [GNU Public License](https://github.com/CSE-SouthwestHS/PrisonersDilemmaSWHS-MASTER/blob/master/LICENSE) for your enjoyment and challenge.

## Requirements

This code requires `Python 3.6 or above` and depends on `pandas`.  
Pandas can be installed with:
```
python -m pip install pandas
```

With these Requirements, you are ready to run your tournament.  See the [OFFICIAL_RULES](https://github.com/CSE-SouthwestHS/PrisonersDilemmaSWHS-MASTER/blob/master/OFFICIAL_RULES.md) to understand how to play.

## Running the Program

Tournaments are run via `iterated-dilemma.py`.  Competitors create modules like those in the [examplemodules](https://github.com/CSE-SouthwestHS/PrisonersDilemmaSWHS-MASTER/tree/master/examplemodules) directory.  Each of these presents a different approach to competing against opponent modules, by colluding or betraying in iterative rounds.  Effective competitors will find the most cunning strategies to predict and outsmart the betrayals of their opponents, inducing an opponent to collude as often as possible while sometimes being betrayed.  

To run an actual tournament, `iterated-dilemma.py` requires parameter arguments.
If modules for your competition are contained in a directory, use the command flag `-d <directory-path>`:
```
./iterated-dilemma.py -d examplemodules
```

Alternately, to manually select modules, you can enter the names of the .py files as parameters.

For example, if modules are named...
```
player1.py
WinningTeam.py
C:\Users\Me\Desktop\weSuck.py
```
...run `./iterated-dilemma.py player1.py WinningTeam.py C:\Users\Me\Desktop\weSuck.py`. 
Any number of modules can be given.

Additional Options:
* `-r` argument:  Randomizes player order.
* `-e` argument:  Error messages from player modules are suppressed when printing results.

## Hosting a Tournament

The Iterative Prisoners Dilemma can be staged on GitHub.  To host your own tournament, Fork this repository and upload it as a new repository to your own GitHub account.  Each competing team can clone the repository, branch it, program and test their module solution.  When ready to compete players can send a pull request to your master branch.  Merge all your competitors branches and run the competition.  

(Using a Git server is by no means a requirement to host a tournament, however it provides an ideal collaborative environment.)

* In the OFFICIAL_RULES, players are instructed to place modules ready for competition in the `tournament` directory.  
* It is usually ideal to have players also compete against classic solutions from the `examplemodules` directory.
* If you plan to include any `examplemodules` copy them to the `tournament` directory before allowing your players to clone the repository.
* Run the tournament using:
```
./iterated-dilemma.py -d tournament
```

## Notes & FAQ

Note: In PyCharm and IDEs with a 'RUN Program' function, add parameters such as `-d tournament` by adding a "Run Configuration" for `iterated-dilemma.py`.  In PyCharm, make the following menu selection: [Run] > [Edit Configuration]
Then add parameters such as `-r -d tournament` to the "Parameters" field.

Note: When running the program in Cmd or PowerShell, if Python files are not set to open in Python (i.e. if `.py` files open in an IDE), You may have to enter something like:

```
python iterated-dilemma.py -d examplemodules
python iterated-dilemma.py player1.py WinningTeam.py C:\Users\Me\Desktop\youLose.py
python iterated-dilemma.py
```

Each team's module should conform to Python 3.6 or above and must provide several things:

`team_name`: a string, no more than 16 characters long, containing no newlines or other weird blank space (must not match regex [^a-zA-Z\d\s:.,'%`])

`strategy_name`: a string, no more than 70 characters long, containing no newlines or other weird blank space (must not match regex [^a-zA-Z\d\s:.,'%`])

`strategy_description`: a string, no more then 350 characters long, containing no newlines or other weird blank space (must not match regex [^a-zA-Z\d\s:.,'%`])

`move(my_history, their_history, my_score, their_score, opponent_name)`: Your definition for this function returning either `'b'` or `'c'` for BETRAY or COLLUDE. You can also `import GLOBALS` and return `GLOBALS.BETRAY` or `GLOBALS.COLLUDE` to make non-hard coded responses (see usage in example3 & 4). `my_moves` and `their_moves` are strings containing the responses each player has made so far during one round of the iterated dilemma, and `my_score` and `their_score` are ints that will usually be negative containing each player's score so far in this round.



### *Enjoy!*