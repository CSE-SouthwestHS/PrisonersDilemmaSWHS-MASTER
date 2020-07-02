import argparse
import glob
import os
import prisoners_dilemma

argparser = argparse.ArgumentParser()
argparser.add_argument("-r", action="store_true", help="Randomizes player order")
argparser.add_argument("-e", action="store_true", help="Suppresses traceback generated by modules")
argparser.add_argument("-d", default="./examplemodules", type=str, help="Path to load modules from")
args = argparser.parse_args()

dirpath = args.d if ('/' or '\\') == args.d[-1] else f"{args.d}/"
assert os.path.isdir(dirpath), f"There is no directory named {dirpath}"

prisoners_dilemma.main(glob.glob(dirpath + '*.py'),
                       args.r,
                       args.e)
