import argparse
import sys
import configparser


def main(zahl1, zahl2):
    Ergebnis =  zahl1*zahl2
    print(f'Das Ergebnis stehet als: {Ergebnis}')


if __name__ == '__main__':
    parser== argparse.ArgumentParser()
    parser.add_argument('-z1',type= int, help='Eine Nummer', default=1)
    parser.add_argument('-z2',type= int, help='Eine Weitere Nummer', default=1))
    parser.add_parser('--config','-c', type=argparse.FileType('r'), help='config file')
    parser.add_argument('-o',dest='output', type=argparse.FileType('w'), help='output file', default=sys.stdout)


    args = parser.parser_args()
    if args.config:
        config= configparser.ConfigParser()
        config.read_file(args.config)
        #Werte in ganze Zahlen umwandeln
        args.z1 =  int(config['ARGUMENTE'][z1])
        args.z2 =  int(config['ARGUMENTE'][z2])


    main(args.z1, args.z2, args.output)