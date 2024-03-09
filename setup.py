from setuptools import find_packages, setup

requirements = [
    "transformers",
    "datasets",
    "vllm",
]

setup(
    name="bonito",
    version="0.0.1",
    url="https://github.com/simulanics/bonito-llama",
    python_requires=">=3.9",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
    description="A lightweight wrapper for the Bonito model using llama.",
    packages=find_packages(),
)
