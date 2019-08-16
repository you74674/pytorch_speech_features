try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

setup(name='pytorch_speech_features',
      version='0.6',
      description='Pytorch Speech Feature extraction',
      license='MIT',
      url='https://github.com/you74674/pytorch_speech_features',
      packages=['pytorch_speech_features'],
      install_requires=[
        'numpy',
        'torch'
      ]
    )
