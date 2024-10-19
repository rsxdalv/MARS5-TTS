import setuptools

setuptools.setup(
    name="mars5",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="CAMB.AI",
    description="MARS5: A novel speech model for insane prosody",
    url="https://github.com/camb-ai/mars5-tts",
    project_urls={},
    scripts=[],
    # include_package_data=True,
    # package_data={
    #     "": ["*.txt"],
    # },
    install_requires=[
        "torch",
        "torchvision",
        "torchaudio",
        "numpy>=1.23.5",
        "regex",
        "librosa",
        "vocos",
        "encodec",
        "safetensors",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
