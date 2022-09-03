import setuptools

with open('README.md', mode='r', encoding='UTF-8') as file:
    LongDescription = file.read()

setuptools.setup(
    name='MusicKuwo',
    version='1.0.0',
    author='Xiaocaicai',
    author_email='xiaocaicai_email@sina.com',
    description='A kuwo music python API.',
    long_description=LongDescription,
    python_requires='>=3.8.0',
    long_description_content_type='text/markdown',
    url='https://github.com/XiaocaicaiGithub/MusicKuwo',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
