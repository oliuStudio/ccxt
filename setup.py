import os
from setuptools import setup, find_packages

# Get all Python files in the root directory that should be part of the ccxt package
def get_py_modules():
    modules = []
    for file in os.listdir('.'):
        if file.endswith('.py') and not file.startswith('setup') and file != '__init__.py':
            modules.append(file[:-3])  # Remove .py extension
    return modules

# Get all packages (directories with __init__.py)
def get_packages():
    packages = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and os.path.exists(os.path.join(item, '__init__.py')):
            packages.append(item)
            # Add subpackages
            for root, dirs, files in os.walk(item):
                for dir_name in dirs:
                    subpackage_path = os.path.join(root, dir_name)
                    if os.path.exists(os.path.join(subpackage_path, '__init__.py')):
                        # Convert path to package name
                        package_name = subpackage_path.replace(os.sep, '.')
                        packages.append(package_name)
    return packages

# Get package data
def get_package_data():
    package_data = {}
    
    # Add static dependencies and protobuf files
    for package in get_packages():
        data_files = []
        package_dir = package.replace('.', os.sep)
        
        if os.path.exists(package_dir):
            for root, dirs, files in os.walk(package_dir):
                for file in files:
                    if not file.endswith('.py') and not file.endswith('.pyc'):
                        rel_path = os.path.relpath(os.path.join(root, file), package_dir)
                        data_files.append(rel_path)
        
        if data_files:
            package_data[package] = data_files
    
    return package_data

setup(
    name="ccxt",
    version="4.5.17",
    description="Modified CCXT with Lighter Exchange Support",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="oliuStudio",
    license="MIT",
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.32.3",
        "pytz>=2024.1",
    ],
    py_modules=get_py_modules(),
    packages=get_packages(),
    package_data=get_package_data(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
