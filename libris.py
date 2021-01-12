#!/usr/bin/env python3
"""
Program that retrieves bibliographic information from Libris from a
given set of search parameters.
"""

import argparse
import json
import urllib.request

def search_libris(args):
    """ Search Libris using http request """

    _uri = 'http://libris.kb.se/xsearch?query'

    if args.isbn:
        with urllib.request.urlopen('{u}=isbn:{i}&format=json'.format(u=_uri, i=args.isbn)) as url:
            data = json.loads(url.read())
            book = data['xsearch']['list'][0]

    print('{}\n'.format(json.dumps(data, indent=4, sort_keys=False)))

    print('{a}\n{t}\n{d}\n{i}'.format(
        a=book['creator'],
        t=book['title'],
        d=book['date'],
        i=book['isbn']))

def parse_args():
    """ Parse the argument list """

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('isbn',
                        type=str,
                        help='ISBN to search for')


    args = parser.parse_args()

    return args


def main():
    """ This is the main function """

    args = parse_args()

    search_libris(args)

if __name__ == '__main__':
    main()
