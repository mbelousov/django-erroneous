from setuptools import setup, find_packages

setup(
    name="django-erroneous",
    author="Mridang Agarwalla",
    author_email="mridang.agarwalla@gmail.com",
    download_url='http://github.com/mridang/django-erroneous/downloads',
    description="django-erroneous makes it easy to collect and log Django application errors.",
    url="http://github.org/mridang/django-erroneous",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(),
    include_package_data=True,
    # this will use MANIFEST.in during install where we specify additional files
    zip_safe=False,
    license="BSD License",
    install_requires=[
        'Django>=1.4',
        'South>=0.7.2'
    ],
    version='0.3.0',
)
