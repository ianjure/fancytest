from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='fancytest',
    version='1.0',
    packages=find_packages(),
    author="Ian Jure Macalisang", 
    author_email="ianjuremacalisang2@gmail.com",
    description="Test function call instances using a simple decorator.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    requires=['termcolor', 'time']
)