from slacker import Slacker
import sys
import functions

slack = Slacker(sys.argv[1])

functions.initialise('', slack)
