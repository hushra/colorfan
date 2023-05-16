from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='Colorfan',
    version='0.1.4',
    description='A powerful python module to set console color',
    py_modules=['colorfan'],
    author='Hamidreza Ahmadi',
    author_email='hushra@pm.me',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hushra/colorfan',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    install_requires=[],
)