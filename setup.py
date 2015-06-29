#!/usr/bin/env python
from distutils.core import setup

setup(
    name = 'itemize',
    version = '0.1',
    description = 'Itemize generates receipts.',
    author = 'Jared Contrascere',
    author_email = 'jcontra@gmail.com',
    url = 'https://github.com/libretees/itemize',
    install_requires=['lxml==3.4.4',
                      'Pillow==2.8.2',
                      'preppy==2.3.2',
                      'Pygments==2.0.2',
                      'PyPDF2==1.24',
                      'reportlab==3.2.0',
                      'svg2rlg==0.3',
                      'z3c.rml==2.9.2',
                      'zope.event==4.0.3',
                      'zope.interface==4.1.2',
                      'zope.schema==4.4.2',],
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)