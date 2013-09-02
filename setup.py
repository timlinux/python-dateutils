#!/usr/bin/env python

from setuptools import setup

setup(
        name='DateUtils',
        version='0.6.5',
        description='Various utilities for working with datetime objects.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        zip_safe=False,
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            ],
        install_requires=[
            'argparse',
            'python-dateutil',
            'pytz (>=2013b)'
            ],
        entry_points={
            'console_scripts': [
                'dateadd = dateutils.dateadd:main',
                'datediff = dateutils.datediff:main',
                ],
            },
        packages=[
            'dateutils',
            ],
        )
