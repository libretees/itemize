#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import csv
import datetime
import logging
from argparse import ArgumentParser
from jinja2 import Environment, PackageLoader
from z3c.rml import rml2pdf

logger = logging.getLogger(__name__)

def fetchTable():
    # Initialize the result array.
    data = []
 
    # Parse content.
    with open('itemize/data.csv', 'r') as csvFile:
        for row in csv.reader(csvFile, delimiter=','):
            rowData = []
 
            for key, col in enumerate(row):
                rowData.append(col)
 
            data.append(rowData)

    return data


def main(argv):
    # Parse arguments.
    parser = ArgumentParser(description='Create data-driven receipts.')
    parser.add_argument('-d', '--log', dest='loglevel', action='store', default='ERROR',
                        help='set log level [DEBUG, INFO, WARNING, ERROR, CRITICAL] (default: ERROR)')
    args = parser.parse_args()

    # Configure logger.
    numeric_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.loglevel.upper())
    logging.basicConfig(level=numeric_level)

    # Load the RML template into the preprocessor.
    logging.info('Loading RML Template.')
    env = Environment(loader=PackageLoader('itemize', 'templates'))
    template = env.get_template('example/template.rml')
    logging.info('Loaded RML Template.')

    # Fetch table data.
    table = fetchTable()

    # Do preprocessing.
    logging.info('Rendering template.')
    rmlText = template.render({'date':    datetime.datetime.now().strftime("%Y-%m-%d"),
                               'name':    'Company',
                               'website': 'www.company.com',
                               'email':   'sales@company.com',
                               'table':   table,})
    logging.info('Rendered template.')

    # Generate PDF output.
    logging.info('Generating PDF document.')
    pdf = rml2pdf.parseString(rmlText)
    logging.info('Generated PDF document.')

    # Save the PDF.
    logging.info('Saving PDF document.')
    with open('output.pdf', 'w') as pdfFile:
        pdfFile.write(pdf.read())
    logging.info('Saved PDF document.')


if __name__ == '__main__':
    main(sys.argv[1:])
