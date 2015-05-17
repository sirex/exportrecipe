from setuptools import setup, find_packages

setup(
    name='exportrecipe',
    version=0.1,
    packages=find_packages(),
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
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development',
    ],
)
