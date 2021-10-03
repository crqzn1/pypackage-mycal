# Import required functions
from setuptools import setup, find_packages
# Call setup function
setup(
    author="xxx yyy",
    description="my own arithmatic package",
    long_description="my own arithmatic package for testing",
    long_description_content_type="text/markdown",
    name="mycal",
    version="0.1.0",
    packages=find_packages(include=["mycal", "mycal.*"]),
    install_requires=[],
    python_requires='>=3.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
