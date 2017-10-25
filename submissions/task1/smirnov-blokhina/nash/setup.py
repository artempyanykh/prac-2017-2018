from setuptools import setup

setup(name='nash',
      version='1.0',
      description='Nash_equilibrium',
      url='https://github.com/smvlx/nash',
      license='MIT',
      packages=['nash'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      zip_safe=False)
