from setuptools import setup

setup(
    name="magisterka",
    packages=["magisterka"],  # Explicitly specify the package name
    package_dir={"magisterka": "."},  # Map package to current directory
    python_requires=">=3.7",
    install_requires=[],
)
