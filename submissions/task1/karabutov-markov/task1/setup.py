from setuptools import setup, find_packages

setup(
    name='task1',
    version='0.1',
    #namespace_packages=['task1'],
    description='nash_equilibrium',
    authir='Markov & Karabutov',
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
    include_package_data=True,
)
