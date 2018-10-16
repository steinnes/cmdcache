from setuptools import setup, find_packages
import fastentrypoints


setup(
    name='cmdcache',
    version='0.2.0',
    description='Simple way to run a command and cache the stdout.  Useful for example when caching cmd output in command completion bash scripts.',
    url='https://github.com/steinnes/cmdcache',
    author='Steinn Eldjarn Sigurdarson',
    author_email='steinnes@gmail.com',
    keywords=['cache', 'cli', 'output'],
    install_requires=["sh==1.11"],
    py_modules=['cmdcache'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points='''
        [console_scripts]
        cmdcache=cmdcache:main
    ''',
)
