from setuptools import setup, find_packages

setup(
    name='multilingual_subtitle_generator',
    version='1.0.0',
    author='Dexiao & Annan',
    author_email='info.deanclub@gmail.com',
    description='A tool for generating multilingual subtitles using WhisperX and LLMs',
    long_description=open('readme.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Dean-Club/Dean-Translator.git',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'torchvision',
        'torchaudio',
        'aiohttp',
        'deepl',
        'openai-whisper',
        'whisperx',
        'transformers',
        'sentencepiece',
        'ctranslate2',
        'scipy',
        'soundfile',
        'soxr',
        'matplotlib',
        'requests',
        'tqdm',
        'protobuf',
        'rich',
    ],
    extras_require={
        'cpu': ['torch'],  # 适用于没有 CUDA 的设备
        'cuda': ['torch @ https://download.pytorch.org/whl/cu124/torch-2.0.1%2Bcu124-cp310-cp310-win_amd64.whl']  # 适用于 CUDA 计算机
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
