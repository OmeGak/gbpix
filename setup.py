from setuptools import setup

setup(name='gbpix',
      version='0.1',
      entry_points='''
            [console_scripts]
            gbpix=gbpix.cli:cli
      ''')
