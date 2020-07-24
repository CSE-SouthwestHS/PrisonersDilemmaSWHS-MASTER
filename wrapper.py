import argparse
import glob
import os
import prisoners_dilemma

argparser = argparse.ArgumentParser(description="A wrapper for prisoners_dilemma.py that handles starting main()")
argparser.add_argument("-r", "--random", action="store_true", help="Randomizes player order")
argparser.add_argument("-e", "--suppress", action="store_true", help="Suppresses traceback generated by modules")
argparser.add_argument("-d", "--directory", default="./examplemodules", type=str, help="Path to load modules from")
argparser.add_argument("-s", "--step", action="store_true", help="Allows you to manually step into each round (good for small groups)")
argparser.add_argument("paths", nargs="*", default=[], type=str, help="path of team modules to load")
args = argparser.parse_args()

dirpath = args.directory if ('/' or '\\') == args.directory[-1] else f"{args.directory}/"
assert os.path.isdir(dirpath), f"There is no directory named {dirpath}"

paths = glob.glob(dirpath + '*.py')

for path in args.paths:
    paths.append(path)

prisoners_dilemma.main(glob.glob(dirpath + '*.py'),
                       args.random,
                       args.suppress,
                       args.step)