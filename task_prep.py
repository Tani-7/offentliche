import argparse
import sys
import configparser

def main(zahl1, zahl2, output_file):
    ergebnis = zahl1 * zahl2
    print(f'Das Ergebnis steht als: {ergebnis}', file=output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-z1', type=int, help='Eine Nummer', default=1)
    parser.add_argument('-z2', type=int, help='Eine weitere Nummer', default=1)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Konfigurationsdatei')
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Ausgabedatei', default=sys.stdout)

    args = parser.parse_args()        

    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        # Werte in ganze Zahlen umwandeln
        args.z1 = int(config['ARGUMENTE']['z1'])
        args.z2 = int(config['ARGUMENTE']['z2'])

    main(args.z1, args.z2, args.output)
