#!/usr/bin/env python
# -*- coding: utf-8 -*-
from z3c.rml import rml2pdf
import datetime
import preppy
import csv
import sys

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
    template = preppy.getModule('itemize/template.prep')

    # Fetch table data.
    table = fetchTable()

    # Do preprocessing.
    rmlText = template.get(
        datetime.datetime.now().strftime("%Y-%m-%d"), 'LibreTees', 
        'www.libretees.com', 'contact@libretees.com', table)

    # Generate PDF output.
    pdf = rml2pdf.parseString(rmlText)

    # Save the PDF.
    with open('output.pdf', 'w') as pdfFile:
        pdfFile.write(pdf.read())

if __name__ == '__main__':
    main(sys.argv[1:])
