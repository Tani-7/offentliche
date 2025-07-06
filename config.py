import argparse
import configparser

def main(zahl1, zahl2):
    ergebnis = zahl1 * zahl2
    print(f'Das Ergebnis ist {ergebnis}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-z1', type=int, help='Eine Zahl', default=1)
    parser.add_argument('-z2', type=int, help='Eine weitere Zahl', default=1)
    parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='Konfigurationsdatei')

    args = parser.parse_args()

    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)

        # Umwandlung der Werte in Integer
        args.z1 = int(config['ARGUMENTE']['z1'])
        args.z2 = int(config['ARGUMENTE']['z2'])

    main(args.z1, args.z2)
