from setuptools import setup, find_packages


setup(
    name='essentialkit',
    version='0.2',
    packages=find_packages(),
    instal_requires=[
        'pandas',
        'clickhouse_driver'
    ]
)