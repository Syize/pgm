import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgmreader", # Replace with your own username
    version="0.0.1",
    author="Benjamin Evans",
    author_email="19811799@sun.ac.za",
    description="A Python package for reading pgm files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BDEvan5/pgm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)