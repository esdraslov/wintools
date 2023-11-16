import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("target", help="the file to be target, no every action need it, if no needs, add a \"\"") # for non-target or non-extra is just add a empty string
parser.add_argument("extra", help="some extra info, no every action need it, if no needs, add a \"\"")
args = parser.parse_args()
