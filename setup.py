import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="MultiImage-Noupin",
    version="1.0.0",
    author="Noupin",
    author_email="author@example.com",
    description="Package for eaxy image conversion.",
    install_requires=required,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Noupin/MultiImage",
    project_urls={
        "Bug Tracker": "https://github.com/Noupin/MultiImage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    
)