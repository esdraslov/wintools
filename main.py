import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("target", help="the file to be target, no every action need it", required=False)
parser.add_argument("extra", required=False, help="some extra info, no every action need it")
args = parser.parse_args()
