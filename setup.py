import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="lantern3",
    version="0.1.0",
    license="MIT",
    author="taekop",
    author_email="taekop@naver.com",
    description="Light up the Ethereum blockchain",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/taekop/lantern3.py",
    packages=setuptools.find_packages(),
    keywords="ethereum",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["web3>=6.0.0,<7"],
    python_requires=">=3.9,<4.0",
)
