from setuptools import find_packages, setup

# get the version from the version file
with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

# get readme contents
with open("README.md", "r") as fh:
    long_description = fh.read()

# create a list from requirements
with open("requirements/prod.txt", "r") as requirements_file:
    requirements = [ requirement.strip() for requirement in requirements_file.readlines() ] 

setup(
    name="BookshelfAPI",
    version=version,
    author="Bob",
    description="Bookshelf API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bob-crutchley/python-flask-bookshelf-api",
    packages=find_packages("src"),
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=requirements
)
