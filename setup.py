from setuptools import setup, find_packages
import fastentrypoints


setup(
    name='cmdcache',
    version='0.1.1',
    description='Simple way to run a command and cache the stdout.  Useful for example when caching cmd output in command completion bash scripts.',
    url='https://github.com/steinnes/cmdcache',
    author='Steinn Eldjarn Sigurdarson',
    author_email='steinnes@gmail.com',
    keywords=['cache', 'cli', 'output'],
    install_requires=["sh==1.11"],
    py_modules=['cmdcache'],
    entry_points='''
        [console_scripts]
        cmdcache=cmdcache:main
    '''
)
