import yaml
import argparse
import sys

def main(zahl1, zahl2, ausgabe):
    ergebnis = zahl1 * zahl2
    print(f'Das Ergebnis steht als: {ergebnis}', file=ausgabe)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-z1', type=int, help='Eine Zahl', default=1)
    parser.add_argument('-z2', type=int, help='Eine weitere Zahl', default=1)
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'), help='Konfigurationsdatei im YAML-Format')
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Ausgabedatei', default=sys.stdout)

    args = parser.parse_args()

    if args.config:
        config = yaml.load(args.config, Loader=yaml.FullLoader)
        args.z1 = int(config['ARGUMENTE']['z1'])
        args.z2 = int(config['ARGUMENTE']['z2'])

    main(args.z1, args.z2, args.output)
