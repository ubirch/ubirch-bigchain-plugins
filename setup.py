import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ubirch-bigchain-event-plugin",
    version="1.0.0",
    author="Victor Patrin",
    author_email="victor.patrin150@gmail.com",
    description="A python utils ubirch for ubirch anchoring services.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ubirch/ubirch-bigchain-plugins",
    packages=setuptools.find_packages(exclude=['bin', 'tests']),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'bigchaindb-driver >= 0.5.3'
    ],
)
