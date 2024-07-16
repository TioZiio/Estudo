
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument(
    '-t', '--training',
    help='Mostra tudo',
    type=str, # Tipo do dado;
    metavar='STRING',
    default='Você é pobre', # Valor padrão;
    required=False,
    nargs='+', # Recebe mais de um valor;
)
parser.add_argument(
    '-a', '--all',
    help='Mostra tudo',
    # type=str, # Tipo do dado;
    metavar='STRING',
    # default='Você é pobre', # Valor padrão;
    required=False,
    # nargs='+', # Recebe mais de um valor;
    action='append',
)
parser.add_argument(
    "-v", "--verbose",
    help='Mostra tudo',
    action='store_true',
    required=False
)
args = parser.parse_args()


if args.all is None:
    print('Valor de -a não inserido')
    print(args.verbose)
    if args.training is None:
        print('Valor de -t não inserido')
    else:
        print(args.training)
else:
    print(args.training)
    print(args.all)
    print(args.verbose)
