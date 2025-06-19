from setuptools import setup, find_packages

setup(
    name='pypinyin_g2pw_torch',
    version='0.1.0',
    description='A pypinyin converter that uses g2pw_torch for polyphonic character disambiguation with PyTorch models.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='baicai1145',
    author_email='your.email@example.com',  # Please change this
    url='https://github.com/baicai1145/g2pw-torch',
    packages=find_packages(),
    install_requires=[
        'pypinyin',
        # This will be resolved by the workspace setup in pyproject.toml
        'g2pw_torch',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
    ],
    python_requires='>=3.8',
) 