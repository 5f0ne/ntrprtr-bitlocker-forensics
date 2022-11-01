import os
import sys
from shutil import copytree, ignore_patterns

import argparse

from ntrprtr_bitlocker_forensics.Controller import Controller

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", choices=["copy"], required=True, help="The tool to use")
    # config
    parser.add_argument("--path", "-p", type=str, default="", help="Path for local copy of ntrprtr configuration files")
    args = parser.parse_args()

    c = Controller()
    c.printHeader()

    if(args.mode == "copy"):
        sourceDir = os.path.dirname(__file__)
        targetDir = os.path.join(args.path, "ntrprtr-bitlocker-config")

        if(not os.path.isdir(targetDir)):
            copytree(os.path.join(sourceDir, "config"), os.path.join(targetDir), ignore=ignore_patterns('__pycache__', '*.py'))
            print("")
            print("ntrprtr bitlocker forensics configurations copied successfully: " + targetDir)
            print("")
            c.printExecutionTime()
        else:
            print("")
            print("Directory already exists: " + targetDir)
            print("")
            c.printExecutionTime()
            exit()

    


if __name__ == "__main__":
    sys.exit(main())
