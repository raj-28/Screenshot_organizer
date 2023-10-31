from setuptools import setup

setup(
    name="ssmanager",
    version="0.1",
    packages=["ssmanager"],
    install_requires=[],
    entry_points={"console_scripts": ["ssmanager=ssmanager.ssmanager:main"]}
)
