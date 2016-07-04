#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import datetime
import logging
import os
import sys
from argparse import ArgumentParser
from jinja2 import Environment, PackageLoader, FileSystemLoader
from z3c.rml import rml2pdf

logger = logging.getLogger(__name__)

def fetch_table():
    # Initialize the result array.
    csv_data = []
 
    # Open the CSV file.
    csv_file = None
    path = os.path.join('itemize', 'data.csv')
    try:
        csv_file = open(path, 'r')
    except IOError as e:
        logger.debug('Could not open CSV file from path (%s)' % path)

    if csv_file is None:
        try:
            csv_file = open('data.csv', 'r')
        except IOError as e:
            sys.exit(str(e))

    # Parse content.
    for row in csv.reader(csv_file, delimiter=','):
        row_data = []
        for column in row:
            row_data.append(column)
        csv_data.append(row_data)

    # Close CSV file.
    csv_file.close()

    return csv_data


def parse_arguments():
    # Parse arguments.
    parser = ArgumentParser(description='Create data-driven receipts.')
    parser.add_argument(
        '-d', '--log', dest='loglevel', action='store', default='ERROR',
        help=(
            'set log level [DEBUG, INFO, WARNING, ERROR, CRITICAL] '
            '(default: ERROR)')
    )
    args = parser.parse_args()

    # Configure logger.
    numeric_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.loglevel.upper())
    logging.basicConfig(level=numeric_level)


def load_template(template_name):
    # Load the RML template into the preprocessor.
    logging.info('Loading RML Template.')
    env = None
    try:
        logging.debug('Loading templates package with PackageLoader.')
        env = Environment(loader=PackageLoader('itemize', 'templates'))
    except ImportError as e:
        logging.debug('Loading templates package with FileSystemLoader.')
        env = Environment(loader=FileSystemLoader('templates'))

    template = env.get_template('%s/template.prep' % template_name)
    logging.info('Loaded RML Template.')

    return template


def main(argv):

    parse_arguments()
    template = load_template('example')

    # Fetch table data.
    table = fetch_table()

    # Do preprocessing.
    logging.info('Rendering template.')
    rml_text = template.render({
        'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'name': 'Company',
        'website': 'www.company.com',
        'email': 'sales@company.com',
        'table': table
    })
    logging.info('Rendered template.')

    # Generate PDF output.
    logging.info('Generating PDF document.')
    pdf = rml2pdf.parseString(rml_text)
    logging.info('Generated PDF document.')

    # Save the PDF.
    logging.info('Saving PDF document.')
    with open('output.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf.read())
    logging.info('Saved PDF document.')


if __name__ == '__main__':
    main(sys.argv[1:])
