from setuptools import setup, find_packages

setup(
    name="ccxt",
    version="4.5.17",
    packages=find_packages(include=["ccxt", "ccxt.*"]),
    install_requires=[
        "requests>=2.32.3",
        "pytz>=2024.1",
    ],
    python_requires=">=3.8",
)
