from setuptools import setup, find_packages

setup(
    name="py-h264",
    version="0.2.2",
    description="A Python library for encoding videos to H.264 and converting images to videos.",
    author="Orphan Byte",
    author_email="orphanbyte@proton.me",
    license="MIT",
    url="https://github.com/orphanbyte/py-h264",
    packages=find_packages(),
    package_dir={"": "pyh264"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.8",
    include_package_data=True,
)