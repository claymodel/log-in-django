import os
import re
from setuptools import setup, find_packages


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        return readme.read()


def version():
    pattern = re.compile(r'__version__ = \'([\d\.]+)\'')
    with open(os.path.join('log_in_django', '__init__.py')) as f:
        data = f.read()
        return re.search(pattern, data).group(1)


setup(
    name='log-in-django',
    version=version(),
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    description='Collecting log in Django application from requests and responses in JSON format.',
    long_description=readme(),
    url='https://github.com/claymodel/log-in-django',
    author='Elias Hasnat',
    author_email='android.hasnat@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Framework :: Django",
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.10.8",
        "Framework :: Django :: 1.11.14",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.0.7",
    ],
    keywords='django log json',
    install_requires=[
        'django>=1.4',
        'six',
        'elasticsearch>=2.0.0',
        'certifi'
    ]
)
