from setuptools import setup, find_packages
import os

import inplace_activity_stream


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author="Eric Brelsford",
    author_email="eric@596acres.org",
    name='django-inplace-activity-stream',
    version=inplace_activity_stream.__version__,
    description=('Place based activites for Django.'),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/596acres/django-inplace-activity-stream/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.3.1',
        'django-activity-stream==0.4.4',
    ],
    packages=find_packages(),
    include_package_data=True,
)
