from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='twsecli',
  packages=['twsecli'],
  version='0.1.6',
  description='TWSE unofficial command-line interface',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Hans Liu',
  author_email='hansliu.tw@gmail.com',
  url='https://github.com/hansliu/twsecli',
  keywords=['twse'],
  python_requires='>=3',
  classifiers=[
    'Programming Language :: Python :: 3',
  ],
  entry_points={
    'console_scripts': [
      'twsecli=twsecli:main',
    ],
  }
)
