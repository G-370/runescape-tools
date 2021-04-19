# Runescape Tools
A couple of python scripts to automate planning and estimations of profit I do in the MMORPG RuneScape.

## viswax
An interactive command-line program for automating profit calculation of vis wax production.

You need python 3.9+ to run it, and you call it on the command line like:
```batch
python viswax.py
```

You're meant to register every attempt with the command: 
"attempt slot1rune slot2rune slot3rune visproduced".
Ex: 
```batch
attempt water earth air 70
attempt water fire cosmic 50
```
And then later use "profit" to show your profit and cost.

Or instead of registering every attempt, you can register your last attempt then use the command "set-try x" to set your amount of Tries.
Ex:
```batch
attempt water fire cosmic 50
set-try 2
```
To get the list of avaible commands, inspect the source or use the command "help"


## to-dos
1. Treat unexpected values and invalid states in the GoldbergReportMachine
2. Make a GUI for viswax
3. Research the viability of compiling the tools to executables.