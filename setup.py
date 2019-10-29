from setuptools import find_packages, setup

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flask_test",
    version=version,
    author="Bob",
    author_email="bob@emai.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages("src"),
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        'flask',
        'gunicorn'
    ]
)

