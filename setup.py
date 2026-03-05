from setuptools import setup, find_packages

setup(
    name="asomm",
    version="0.1.0",
    description="بوت موسيقى عربي مبني على Pyrogram و PyTgCalls",
    author="osamavvs",
    url="https://github.com/osamavvs/asomm",
    packages=find_packages(),
    install_requires=[
        "pyrogram==2.0.106",
        "tgcrypto==1.2.5",
        "yt-dlp",
        "pytgcalls"
    ],
    python_requires=">=3.8",
)
