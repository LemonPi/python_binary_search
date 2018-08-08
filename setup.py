from setuptools import setup, find_packages

setup(name='binary_search',
      version='0.1.0',
      # typing
      python_requires='>=3.5.*',
      packages=find_packages(),
      test_suite='pytest',
      tests_require=[
          'pytest',
      ],
      )
