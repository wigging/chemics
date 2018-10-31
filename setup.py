import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chemics",
    version="0.0.1",
    author="Gavin Wiggins",
    description="Chemical engineering with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chemics/chemics",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
