import json
from bracket import Bracket


def main():
    f = open('data/bracket.json')
    data = json.load(f)
    bracket = Bracket(data)
    bracket.run()

if __name__ == '__main__':
    main()
