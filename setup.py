import setuptools

with open('README.md', mode='r', encoding='UTF-8') as file:
    long_description = file.read()

setuptools.setup(
    name='MusicKuwo',
    version='0.1.1',
    author='Xiaocaicai',
    author_email='xiaocaicai_email@sina.com',
    description='A kuwo music python API.',
    long_description=long_description,
    python_requires='>=3.4.0',
    long_description_content_type='text/markdown',
    url='https://github.com/xiaocaicai-github/MusicKuwo',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
