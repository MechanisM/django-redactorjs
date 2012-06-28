import os
from setuptools import setup
from redactor import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-redactorjs',
    version=".".join(map(str, VERSION)),
    description='This reusable Django app using WYSIWYG editor redactorjs.com',
    long_description=readme,
    author="Igor 'TigorC' Tokarev",
    author_email='TigorC@gmail.com',
    url='http://github.com/TigorC/django-redactorjs',
    packages=['redactor'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
    'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
