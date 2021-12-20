import json
from bracket import Bracket


def main():
    f = open('data/bracket.json')
    data = json.load(f)
    bracket = Bracket(data)
    bracket.run(display_history=True)

if __name__ == '__main__':
    main()
