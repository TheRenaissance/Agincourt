try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A text-based game based on the battle of Agincourt',
    'author': 'The Renaissance',
    'url': 'URL to get it at',
    'download_url': 'Where to download it at',
    'author_email': 'buycomputer40@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Agincourt'],
    'scripts': [],
    'name': 'Agincourt'
}

setup(**config)
