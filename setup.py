from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Data Frame Profiling'
LONG_DESCRIPTION = 'A package that allows to easily profile your dataframe, check for missing values, outliers, data types.'

# Setting up
setup(
    name='df_profiling',
    version=VERSION,
    author="Sam Faraday",
    author_email="<saurater@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(include=['df_profiling']),
    install_requires=['pandas'],
    keywords=['python', 'profiling', 'outliers', 'missing values'],
    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
