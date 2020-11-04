#!/usr/bin/python3
import argparse

APP_DESCRIPTION = "A simple console program using argument parser module"

def main():
    global args
    parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
    parser.add_argument('pos', nargs=1, help="positional argument")
    parser.add_argument('--contains', help="Does it contain")
    args = parser.parse_args()

def action():
    value = int(args.pos) * 2
    print("Arguments contain: %d"%(value))

if __name__ == "__main__":
    main()
    action()
