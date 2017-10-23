from setuptools import setup, find_packages

setup(
    name='nifcloud-uri',
    version='0.0.1',
    description='NIF CLOUD IaaS API uri Generator',
    url='https://github.com/kzmake/nifcloud-uri-python',
    author='Kazuki Iwata',
    author_email='kazu.0516.k0n0f@gmail.com',
    license='MIT',
    keywords='nifcloud api uri nifty cloud',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
)
