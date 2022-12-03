from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='chand',
    version='0.0.2',
    packages=['chand'],
    include_package_data=True,
    url='https://github.com/armanyazdi/chand',
    license='MIT',
    author='Arman Yazdi',
    description='A Python library for converting currencies to Iranian Rial and Toman.',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='currency converter, crypto converter, iranian rial, iranian toman',
    install_requires=['requests', 'bs4'],
    python_requires='>= 3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Persian',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ],
    project_urls={
        'Source': 'https://github.com/armanyazdi/chand',
        'Documentation': 'https://pypi.org/project/chand',
    },
)
