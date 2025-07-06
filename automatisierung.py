import argparse

def berechne_ergebnis(zahl1, zahl2):
    ergebnis = zahl1 * zahl2
    print(f'Das Ergebnis ist {ergebnis}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-z1', type=int, help='Eine Zahl', default=1)
    parser.add_argument('-z2', type=int, help='Eine weitere Zahl', default=1)

    args = parser.parse_args()
    berechne_ergebnis(args.z1, args.z2)
