from setuptools import setup

version = '0.1a0'


setup(
    name='harmony_tools',
    version=version,
    packages=['harmony_tools', ],
    package_dir={'harmony_tools': 'harmony_tools'},
    entry_points={
        'console_scripts': ['harmony_tools=harmony_tools.cli:main'],
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
