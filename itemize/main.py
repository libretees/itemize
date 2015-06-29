#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import datetime
from jinja2 import Environment, PackageLoader
from z3c.rml import rml2pdf


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
    # Load the RML template into the preprocessor.
    env = Environment(loader=PackageLoader('itemize.templates', 'example'))
    template = env.get_template('template.prep')

    # Fetch table data.
    table = fetchTable()

    # Do preprocessing.
    rmlText = template.render({'date':    datetime.datetime.now().strftime("%Y-%m-%d"),
                               'name':    'LibreTees',
                               'website': 'www.libretees.com',
                               'email':   'contact@libretees.com',
                               'table':   table,})

    # Generate PDF output.
    pdf = rml2pdf.parseString(rmlText)

    # Save the PDF.
    with open('output.pdf', 'w') as pdfFile:
        pdfFile.write(pdf.read())

if __name__ == '__main__':
    main(sys.argv[1:])
