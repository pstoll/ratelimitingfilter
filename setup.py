try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ratelimitingfilter',
      version='0.1',
      description='A rate limiting filter for the logging system',
      url='https://github.com/wkeeling/ratelimitingfilter',
      author='Will Keeling',
      author_email='will@zifferent.com',
      maintainer='Will Keeling',
      maintainer_email='will@zifferent.com',
      license='MIT',
      packages=['ratelimitingfilter'])
