import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='chemics',
    version='22.10',
    author='Gavin Wiggins',
    description='A Python package for chemical engineering',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chemics/chemics',
    packages=setuptools.find_packages(),
    install_requires=['matplotlib', 'numpy', 'pandas', 'scipy'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
    package_data={
        'chemics': ['data/*.csv'],
    },
)
