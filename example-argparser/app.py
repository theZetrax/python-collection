#!/usr/bin/python3
import argparse

APP_DESCRIPTION = "A simple console program using argument parser module to add numbers"

def boot():
    global args
    parser = argparse.ArgumentParser(description=APP_DESCRIPTION)
    parser.add_argument('num1', help="The first number", type=float)
    parser.add_argument('num2', help="The second number", type=float)
    args = parser.parse_args()

def action():
    return args.num1 + args.num2

if __name__ == "__main__":
    boot()
    value = action()
    print("Sum is: %.2f"%(value))
