from setuptools import setup

setup(name='gbpix',
      version='0.1',
      py_modules=['gbpix'],
      install_requires=['Click',
                        'Pillow'],
      entry_points='''
            [console_scripts]
            gbpix=script:cli
      ''')
