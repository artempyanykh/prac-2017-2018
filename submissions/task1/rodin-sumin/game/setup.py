from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='game',
      version='0.1',
      description='zero-sum game',
      url='',
      author='Rodin_Sumin',
      author_email='kg-1205@rambler.ru',
      license='MIT',
      packages=['game'],
      test_suite='nose.collector',
      tests_require=['nose'],
      )