# **Py**Lagiarism #

## Introduction ##

This project is born of my will to get me feet back to programming... at my own... for something purposeful... It has been many years since I've done a project like this... my heart has always been in AI, but I had to ditch it due to personal matters... well... enough whining... let get coding...

## V 1.0 - February, 19, 2023 ##
The idea for this version, is to be really simple, and compare two given texts (initially txt files, I know this is not fancy, but we've got to start somewhere, right?), and find similarities among them.
What we want to do, is create a program, that reads two texts files, and compares both for finding similarities.
This version uses Python's [argparse](https://pypi.org/project/argparse/) and [rapidfuzz](https://pypi.org/project/rapidfuzz/), for parsing arguments and doing the comparison of strings.
The program works by reading every line of the first file and comparing to every line of the second file, calculating the similarity threshold between them, and returning the index of the line for the first file and the index of the line for the second file, and also the similarity value between the two lines.

**Usage**

`python pylagiarism --files <file 1 path> <file 2 path> --threshold <threshold value in decimals>`

The resulting file will be generated at the same location as the python file. At least for now.