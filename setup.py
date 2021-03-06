from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.0.1'

install_requires = [
    'click',
    'flask',
    #'mcp3008',
    'requests',
    #'RPi.GPIO',
]

setup(name='nuke.irrigator',
    version=version,
    description="Automatic irrigation system for unix capable devices.",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='irrigation, raspberry',
    author='Gabor Wnuk',
    author_email='gabor.wnuk@me.com',
    url='https://gabo.re/',
    license='Apache License 2.0',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['nuke'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['nuke.irrigator=nuke.irrigator:main']
    }
)
