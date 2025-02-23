import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudops_commander",
    version="0.1.0",
    author="Your Name",
    author_email="you@example.com",
    description="A package for simplifying cloud deployments, automating CI/CD pipelines, and monitoring microservices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cloudops_commander",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
