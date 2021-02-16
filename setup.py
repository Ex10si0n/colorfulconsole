import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorfulconsole",
    version="0.0.1",
    author="Ex10si0n",
    author_email="yzb.ex10si0n@icloud.com",
    description="Colorful console output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ex10si0n/color.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)


