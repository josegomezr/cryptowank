import setuptools
from cryptowank.version import Version


setuptools.setup(name='crypto-wank',
    version=Version('1.0.0').number,
    description='A wank for cryptocurrency markets',
    long_description=open('README.md').read().strip(),
    author='José Gómez',
    author_email='1josegomezr@gmail.com',
    # url='http://path-to-my-packagename',
    py_modules=['cryptowank'],
    license='MIT License',
    zip_safe=False,
    install_requires=[
        'requests',
        'PyYAML'
    ],
    keywords='crypto coins market poloniex bitrex currencies',
    scripts=['bin/cryptowank'],
    classifiers=['Packages']
    )
