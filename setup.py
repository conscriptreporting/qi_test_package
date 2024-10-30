# setup.py

from setuptools import setup, find_packages

setup(
    name='qi_test_package',
    version='0.1',
    packages=find_packages(),
    description='A trivial test package.',
    author='Qi Gao',
    author_email='qgao1997@163.com',  # 使用你的真实电子邮箱
    url='https://github.com/conscriptreporting/qi_test_package',  # 可以使用真实URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
