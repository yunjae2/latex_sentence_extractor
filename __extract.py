#!/usr/bin/env python3
import sys
import re

def extract(strings):
    sentence=""
    for string in strings:
        string = string.strip()
        if not string or string.startswith("%"):
            continue

        string = re.sub(r"~\\cite{[^{]*}", "", string)
        string = re.sub(r"~\\ref{[^{]*}", "", string)

        if not sentence:
            sentence = string
        else:
            sentence += " " + string

        if sentence.endswith("."):
            print(sentence)
            sentence = ""


def main():
    if len(sys.argv) > 1:
        print("usage: %s" % sys.argv[0])
        print("Input text strings to stdin stream.")
        sys.exit(1)
    extract(sys.stdin)


if __name__ == "__main__":
    main()
