from setuptools import setup

setup(name='station-service',
      version='0.1.0',
      packages=['service'],
      entry_points={
          'console_scripts': [
              'station-service = service.__main__:main'
          ]
      },
)