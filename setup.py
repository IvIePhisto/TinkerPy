from setuptools import setup, find_packages
import sys, os

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'README.md')) as f:
      long_description = f.read()

version = '0.1.0'

setup(name='TinkerPy',
      version=version,
      description="Tools tinkering with basic Python stuff.",
      long_description=long_description,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='tool built-ins decorator dict mapping Unicode',
      author='Michael Pohl',
      author_email='pohl-michael@gmx.biz',
      url='https://github.com/IvIePhisto/TinkerPy',
      license='MIT License',
      packages=find_packages(exclude=['tests']),
      test_suite='tests',
      include_package_data=False,
      zip_safe=True,
)
