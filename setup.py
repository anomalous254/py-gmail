from setuptools import setup, find_packages

setup(
    name='pygmail',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'jinja2>=3.0.0',
    ],
    author='Peter Nyando',
    description='This is an unofficial python module providing convenient way of sending emails using gmail smtp services',
    url='https://github.com/anomalous254/pygmail',
    license='MIT',
)
