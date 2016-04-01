import os
import sys
from os.path import dirname
sys.path.append(dirname(__file__))
from monkey_parser import MonkeyParser


f = open(os.path.join(os.path.abspath(os.sep), "temp\monkey_tmp.txt"))
paths = []
for _line in iter(f):
    _line = _line.strip().rstrip()
    paths.append(_line)
f.close()

os.remove(os.path.join(os.path.abspath(os.sep), "temp\monkey_tmp.txt"))

parser = MonkeyParser(paths[0], paths[1])
parser.parse_line(parser.get_lines()[3])


