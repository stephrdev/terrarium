from setuptools import find_packages, setup


setup(
    name='terrarium',
    version='0.1.0',
    author='Stephan Jaekel',
    url='https://github.com/stephrev/terrarium',
    packages=find_packages('', exclude=['testing']),
    include_package_data=True,
    tests_require=[],
    install_requires=[],
    dependency_links=[],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
