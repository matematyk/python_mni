
import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='projekt_metodyka_nauczania',
    version='1.0.1',
    url='https://github.com/matematyk/python_mni/',
    license='MIT',
    maintainer='Marcin Wierzbinski',
    maintainer_email='',
    description='Projekt z Metodyki Nauczania Informatyki',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'wheel',
        'networkx',
        'matplotlib',
    ],
    extras_require={

    },
)