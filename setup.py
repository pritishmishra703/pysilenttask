from setuptools import setup, find_packages

setup(
    name='pysilenttask',
    version='1.5',
    description='Effortlessly create and manage background-running Python scripts using pysilenttask.',
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
