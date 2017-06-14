
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = ['docopt', 'termcolor']


setup(
    name='stacks',
    version='0.0.1',
    description='stacks for stack graphs',
    url='https://github.com/Denniskamau/stacks.git',
    license="MIT License",
    author='Dennis Kamau',
    author_email='denniskamau3@gmail.com',
    install_requires=dependencies,
    packages=['stacks', ],
    entry_points={
        'console_scripts': [
            'stacks=stacks.main:start'
        ],
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)