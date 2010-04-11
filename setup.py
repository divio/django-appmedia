from setuptools import setup, find_packages
import os
import appmedia

setup(
    author="Patrick Lauber",
    author_email="digi@treepy.com",
    name='django-appmedia',
    version=appmedia.__version__,
    url = 'http://github.com/divio/django-appmedia',
    description='Handling django app media',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    requires=[
        'django (>1.1.0)',
    ],
    
    packages=find_packages(),
    package_dir={
        'appmedia': 'appmedia',
    },
    zip_safe = False
)