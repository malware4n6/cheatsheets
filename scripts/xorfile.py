import argparse
import logging
import sys
from binascii import unhexlify

try:
    from rich.logging import RichHandler
    from rich.console import Console
    rich_support = True
except:
    rich_support = False

__author__ = "malware4n6"
__copyright__ = "malware4n6"
__license__ = "The Unlicense"

def setup_logging(verbose: bool):
    """Setup basic logging
    """
    global rich_support
    logformat = "[%(asctime)s] %(levelname)s\t%(name)s\t%(message)s"
    if rich_support:
        logging.basicConfig(
            level=logging.DEBUG if verbose else logging.INFO,
            # format=logformat, datefmt="%Y-%m-%d %H:%M:%S",
            format="%(message)s", datefmt="[%X]",
            handlers=[RichHandler(console=Console(stderr=True))]
        )
    else:
        logging.basicConfig(
            level=logging.DEBUG if verbose else logging.INFO,
            stream=sys.stderr, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
        )

log = logging.getLogger('xf')

def xorfile(filein, key, fileout=None):
    # check key
    try:
        k = unhexlify(key.replace(' ', ''))
    except Exception as exc:
        log.error(str(exc))
        return
    
    with open(filein, 'rb') as fd:
        content = fd.read()
    xored = []
    keylen = len(k)
    log.debug(f'{keylen=}')
    for i, v in enumerate(content):
        xored.append(v ^ k[i%keylen])
    xored = bytes(xored)
    if fileout:
        with open(fileout, 'wb') as fd:
            fd.write(xored)
    else:
        print(xored.decode(), end='')

def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Yaradiff :: configuration generator")
    parser.add_argument("-i", "--input", required=True,
                        help="input file",
                        type=str)
    parser.add_argument("-o", "--output", required=False, help="optional output file", type=str, default=None)
    parser.add_argument("-k", "--key", required=True, help="xor key (hex, i.e '22 44')", type=str)
    parser.add_argument("-v", "--verbose", help="set logging level to DEBUG (INFO by default)",
                        action="store_true")
    return parser.parse_args(args)


def main(args):
    """
    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.verbose)
    log.debug('start')
    xorfile(args.input, args.key, args.output)
    log.debug('end')

def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
