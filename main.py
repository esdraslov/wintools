import argparse
import tools

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("target", help="the file to be target, no every action need it, if no needs, add a \"\"") # for non-target is just add a empty string
args = parser.parse_args()
# importants arguments
action = args.action

if action == "uninstall":
    tools.uninstall.active(args.target)
