from setuptools import setup, find_packages

setup(
    name='exportjsonrecipe',
    version=0.1,
    packages=find_packages(),
    entry_points={
        'zc.buildout': ['default = exportjsonrecipe:ExportJsonRecipe'],
    },
)
