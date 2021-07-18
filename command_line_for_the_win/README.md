# Command line for the win

This repository contains proof of completion of the first 18 tasks in the [CMD CHALLENGE](https://cmdchallenge.com/).
The CMD Challenge is a pretty cool game to test you on Bash skills.
Everything is done via the command line and the questions are becoming increasingly complicated.

******************* Play and have fun ***************

This project is NOT mandatory at all. It is 100% optional. 

### Detail of the tasks:

:snail: Your first challenge is to print "hello world" on the terminal in a single command.
Hint: There are many ways to print text on the command line, one way is with the 'echo' command. Try it below and good luck!

:butterfly: Print the current working directory.

:bug: List names of all the files in the current directory, one file per line.

:ant: There is a file named `access.log` in the current directory. Print the contents.

:spider_web: Print the last 5 lines of `access.log`.

:whale2: Create an empty file named `take-the-command-challenge` in the current working directory.

:whale: Create a directory named `tmp/files` in the current working directory

:dolphin: Copy the file named `take-the-command-challenge` to the directory `tmp/files`

:fish: Move the file named `take-the-command-challenge` to the directory `tmp/files`

:tropical_fish: A symbolic link is a type of file that is a reference to another file.
Create a symbolic link named `take-the-command-challenge` that points to the file `tmp/files/take-the-command-challenge`.

:blowfish: Delete all of the files in this challenge directory including all subdirectories and their contents.

:wolf: There are files in this challenge with different file extensions. Remove all files with the `.doc` extension recursively in the current working directory.

:mosquito: There is a file named `access.log` in the current working directory. Print all lines in this file that contains the string "GET".

:beetle: Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".

:cricket: Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.

:spider: Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".
Note that there are no files named `access.log` in the current directory, you will need to search recursively.

:scorpion: Extract all IP addresses from files that start with "access.log" printing one IP address per line.

:fly: Count the number of files in the current working directory. Print the number of files as a single integer.

:worm: Print the contents of `access.log` sorted.

:microbe: Print the number of lines in `access.log` that contain the string "GET".

:monkey_face: The file `split-me.txt` contains a list of numbers separated by a ; character.
Split the numbers on the ; character, one number per line.

:dog: Print the numbers 1 to 100 separated by spaces.

:fox_face: This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase from all text files recursively.
Note that some files are in subdirectories so you will need to search for them.

:cat: The file `sum-me.txt` has a list of numbers, one per line. Print the sum of these numbers.

:lion: Print all files in the current directory recursively without the leading directory path.

:tiger: Rename all files removing the extension from them in the current directory recursively.

:horse: The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.
