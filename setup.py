from setuptools import setup, find_packages
from setuptools.command.test import test as test_cmd
from os import path

version = '0.1'

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class Test(test_cmd):
    def run_tests(self):
        import coverage
        cov = coverage.Coverage()
        cov.start()

        res = super().run_tests()

        cov.stop()
        cov.report()
        cov.html_report()
        cov.xml_report()

        return res


setup(
    name='harmony_tools',
    version=version,
    packages=find_packages(),
    package_dir={'harmony_tools': 'harmony_tools'},
    entry_points={
        'console_scripts': ['harmony_tools=harmony_tools.cli:main'],
    },
    license='MIT',
    url='https://github.com/a1fred/harmony_tools',
    author='a1fred',
    author_email='demalf@gmail.com',
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite="tests",
    cmdclass={
      'test': Test,
    },
    tests_require=[
        'coverage'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
