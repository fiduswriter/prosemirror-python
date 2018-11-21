import os
from setuptools import find_packages, setup
import js2py
from npm.bindings import npm_run


stderr, stdout = npm_run('install')
stderr, stdout = npm_run('run','bundle')

if not os.path.exists('prosemirror'):
    os.makedirs('prosemirror')

js2py.translate_file('lib/index.js', 'prosemirror/__init__.py')

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='prosemirror-python',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Js2Py==0.59',
    ],
    include_package_data=True,
    license='AGPL License',
    description='Python translation of prosemirror parts needed to modify a document in Python',
    long_description=README,
    url='https://www.github.org/fiduswriter/prosemirror-python',
    author='Johannes Wilm',
    author_email='johannes@fiduswriter.org',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
