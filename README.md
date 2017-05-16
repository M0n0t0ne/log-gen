# log-gen
The aim of this script is to help you manually log system or file changes through the command line. With the help of switches, you can generate a log file that best suites your needs, aiming at being both functional and highly customizable. 

### Installation
In the terminal, type git clone https://github.com/M0n0t0ne/log-gen
### Usage
python log-gen.py [-h] [-g] [-d] [-s] [-b] [-c] [-a] [-r] [-t]

  -h : Displays a list of options and their descriptions
  -g : Generates the log "skeleton" in the directory defined in the global HOME variable; default is your home directory
  -d : Prompts you to delete the log file
  -b : Backs up your log file in ~/backup/; can be configured by editing the global BACKUP variable
