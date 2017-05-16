# log-gen
The aim of this script is to help you manually log system or file changes through the command line. With the help of switches, you can generate a log file that best suites your needs, aiming at being both functional and highly customizable. 

## Installation
In the terminal, type git clone https://github.com/M0n0t0ne/log-gen in your home directory
## Usage
python log-gen.py [-h] [-g] [-d] [-s] [-b] [-c] [-a] [-r] [-t]

- h : Displays a list of options and their descriptions
- g : Generates the log "skeleton" in the directory defined in the global HOME variable; default is your home directory
- d : Prompts you to delete the log file
- b : Backs up your log file in ~/backup/; can be configured by editing the global BACKUP variable
- s : Shows your log file in the terminal; same as doing "cat CHANGELOG.txt"
- c : Creates an entry header; this displays the current date and helps seperate changes and additions from different days
- a : Creates an "addition tag", which indicates something that has been added to a system or program. Indicated by the color green
- r : Creates a "removal tag", which indicates something has has been removed from a system or program. Indictated by the color red
- t : Creates a "todo tag", which indicates something that you plan on doing to a system or program. Indicated by the color cyan

### Getting Started
1. Go into the same directory as log-gen.py <--- An installation file is coming soon
2. In the terminal, type "python3 log-gen -g" to generate a CHANGELOG.txt file in your home directory
3. While still in the terminal, type "python3 log-gen -c" to create an entry header for today
4. Now type "python3 log-gen -a" to create an addition tag. Remember, this is for indicating added programs or changes
5. Now type "python3 log-gen -r" to create a removal tag, type something random.
6. Now type "python3 log-gen -t" to create a todo tag, and again, type something random
7. TO see your log, you can either "cat CHANGELOG.txt" or do "python3 log-gen -s"
8. Finally, to delete your log, type "python3 log-gen -d" in the log-gen directory.

*Please note that this script is still early in development, changes will be made and suggestions are welcome. 
