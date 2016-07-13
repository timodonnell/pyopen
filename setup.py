try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.0.3"

setup(
    name="pyopen",
    version=version,
    author="Tim O'Donnell",
    author_email="timodonnell@gmail.com",
    packages=["pyopen", "pyopen.loaders"],
    url="https://github.com/timodonnell/pyopen",
    license="Apache License",
    description="launch an interactive ipython session with specified files opened and parsed",
    long_description=open('README.rst').read(),
    download_url='https://github.com/timodonnell/pyopen/tarball/%s' % version,
    entry_points={
        'console_scripts': [
            'pyopen = pyopen.command:run',
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=[
        "humanize",
        "traitlets",
        "six",
        "xlrd",
        "pandas>=0.16.1",
        "nose>=1.3.1",
    ]
)
