#!/usr/bin/python3

""" this a python3 script that prints a message """

import sys


def main():

    """ prints out a message using write """

    message = "and that piece of art is useful - Dora Korpar, 2015-10-19"

    sys.stderr.write(message + "\n")


if __name__ == "__main__":
    main()
    sys.exit(1)
