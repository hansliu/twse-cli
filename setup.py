from distutils.core import setup
setup(
  name='twsecli',
  packages=['twsecli'],
  version='0.1.5',
  description='TWSE unofficial command-line interface',
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
