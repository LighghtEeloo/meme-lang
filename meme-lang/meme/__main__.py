import click
from sys import stdin
from meme import *

@click.command()
@click.option('--generate', '-g', 'mode', flag_value='generate',
              default=True)
@click.option('--interpret', '-i', 'mode', flag_value='interpret')
@click.argument('filename', type=click.Path(exists=True), required=False)
def main(mode, filename):
    target: Meme

    if mode == 'generate':
        target = MemeGenerator()
    elif mode == 'interpret':
        target = MemeInterpreter()
    else:
        raise Exception()

    if filename is None:
        target.with_file(stdin)
    else:
        target.with_open(filename)

    if mode == 'generate':
        target.trans()
    elif mode == 'interpret':
        target.format()
    else:
        raise Exception()

    target.print()


if __name__ == '__main__':
    main()
