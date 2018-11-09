from setuptools import setup

version = '0.1a0'


setup(
    name='guitar_gammas',
    version=version,
    packages=['guitar_gammas', ],
    package_dir={'guitar_gammas': 'guitar_gammas'},
    entry_points={
        'console_scripts': ['guitar_gammas=guitar_gammas.cli:main'],
    },
    license='MIT',
    author='a1fred',
    author_email='demalf@gmail.com',
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite="tests",
)
