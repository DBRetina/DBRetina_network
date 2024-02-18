# import
import codecs
import os.path
import setuptools

def read(rel_path):
    """Read a code file
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    """Fetch the version of package by parsing the __init__ file
    """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

# fetch readme for long description

setuptools.setup(
    name="DBRetina_viz",
    # version="0.0.6",
    version=get_version("dbretina_viz/__init__.py"),
    author="Mohit Mayank",
    author_email="mohitmayank1@gmail.com",
    description="DBRetina_viz - your interactive network visualizer dashboard",
    long_description_content_type="text/markdown",
    url="https://github.com/imohitmayank/DBRetina_viz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={'': ['datasets/*', 'assets/*', 'datasets/got/*']},
    include_package_data=True,
)