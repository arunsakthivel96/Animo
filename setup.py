#!/usr/python

import sys,os
#from color import *

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    BLUE_BG = '\033[1;44m'
    GREEN = '\033[92m'
    GREEN_BG = '\033[4;42m'
    YELLOW = '\033[93m'
    YELLOW_BG = '\033[43m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

color = Color()

def main():

	print "Hello>".format(color.RED)

	if __name__ == '__main__':

		
		main()

