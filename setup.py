from setuptools import setup, find_packages


setup(
    name='drf_prettify_json_serializer_field',
    version='0.0.1',
    description='You got ugly json, we got a serializer that can massage that data into something useful',
    long_description='Serialize ugly json to pretty json',
    keywords='djangorestframework serializer field json massage presenter-pattern',
    url='https://github.com/rosscdh/drf-prettify-json_serializer-field/',
    author="Ross Crawford-d'Heureuse",
    author_email='sendrossemail@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests'])
)
