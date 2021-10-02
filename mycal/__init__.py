"""
my arithmatic
=============

my own arithmatic
"""

"""
root directory
"""
# 'dub', 'inc', 'mydub', 'myinc'
from mycal.dub import *
from mycal.inc import *

# this works as well, relative import
# from .dub import *
# from .inc import *

"""
subpackages
"""
# import 'addx', 'mulx', 'myadd', 'mymul'
from mycal.addx.addx import * # myadd(1,2,3)
from mycal.mulx.mulx import * # mymul(1,2,3)

# import 'addx', 'mulx'
# from mycal.addx import addx # addx.myadd(1,2,3)
# from mycal.mulx import mulx # mulx.mymul(1,2,3)

# this does not work!!!
# import mulx.mulx
# import addx.addx