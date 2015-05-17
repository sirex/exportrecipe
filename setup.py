import os.path
from setuptools import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='exportrecipe',
    version='0.2',
    license='MIT',
    description="Buildout recipe to export buildout configuration to JSON file.",
    long_description=(read('README.rst') + '\n' + read('CHANGES.rst')),
    author='Mantas Zimnickas',
    author_email='sirexas@gmail.com',
    url='https://bitbucket.org/sirex/rubygemsrecipe',
    py_modules=['exportrecipe'],
    install_requires=[
        'zc.buildout',
    ],
    extras_require={
        'tests': ['mock'],
    },
    entry_points={
        'zc.buildout': ['default = exportrecipe:ExportRecipe'],
    },
    classifiers=[
        'Framework :: Buildout :: Recipe',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
