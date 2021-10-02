# Import required functions
from setuptools import setup, find_packages
# Call setup function
setup(
    author="xxx yyy",
    description="my own arithmatic package",
    name="mycal",
    version="0.1.0",
    packages=find_packages(include=["mycal", "mycal.*"]),
    install_requires=[],
    python_requires='>=3.0'
)