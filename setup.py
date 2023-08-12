from setuptools import setup, find_packages

setup(
    name='pysilenttask',
    version='1.0',
    description='A utility for managing background tasks.',
    author='Pritish Mishra',
    author_email='pritishjan@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pysilenttask = pysilenttask.pysilenttask:main'
        ]
    },
    install_requires=[
        'pandas',
        'psutil'
    ],
)
