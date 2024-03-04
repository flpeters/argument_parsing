from pkg_resources import parse_version
from setuptools import setup, find_packages, __version__ as setuptools_version
assert parse_version(setuptools_version)>=parse_version('36.2')

def add_minimum_python_version(min_python:str, data:dict):
    "Adds classifiers and python_requires information to data"
    assert '2.0' <= min_python, "A python version below '2.0' is not possible."
    if min_python not in py_v:
        print(f"[WARNING]: Minimum Python version '{min_python}' in '{file_found}' is not recognized.\n"\
              f"           Recognized versions are: {py_v}")
    else:
        data['python_requires'] = f'>={min_python}'
        data['classifiers'].append('Programming Language :: Python')
        if   '2.0' <= min_python < '3.0':
            data['classifiers'].append('Programming Language :: Python :: 2')
        elif '3.0' <= min_python < '4.0':
            data['classifiers'].append('Programming Language :: Python :: 3')
            data['classifiers'].append('Programming Language :: Python :: 3 :: Only')
        if min_python in py_v:
            data['classifiers'].extend([f'Programming Language :: Python :: {v}' for v in py_v[py_v.index(min_python):]])


def add_development_status(status:int, data:dict):
    "Adds the development status classifier. Options are from 1 through 7."
    try:
        data['classifiers'].append(f'Development Status :: {dev_status[status-1]}')
    except (ValueError, IndexError):
        raise ValueError(f"Status '{status}' is an invalid value in '{file_found}'. \n"\
                         "It can only take on one of the following: {'1', '2', '3', '4', '5', '6', '7'}") from None


py_v = '2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12 3.13'.split()
dev_status = ['1 - Planning', '2 - Pre-Alpha', '3 - Alpha', '4 - Beta',
              '5 - Production/Stable', '6 - Mature', '7 - Inactive' ]

metadata = dict(name             = 'argument_parsing',
                entry_points     = dict(console_scripts = list()),
                install_requires = list(), # ['pip', 'packaging']
                extras_require   = dict(),
                classifiers      = list(),
                project_urls     = dict())

metadata['license'] = 'GNU General Public License v2 (GPLv2)'
metadata['classifiers'].append('License :: OSI Approved :: GNU General Public License v2 (GPLv2)')


add_minimum_python_version('3.8', metadata)
add_development_status(3, metadata)
metadata['classifiers'].append('Intended Audience :: Developers')

git_url = 'https://github.com/flpeters/argument_parsing'
metadata['url']                         = git_url # homepage
metadata['download_url']                = git_url # TODO: use pypi url
metadata['project_urls']['Source Code'] = git_url

doc_url = git_url
metadata['project_urls']['Documentation'] = doc_url

bug_tracker_url = 'https://github.com/flpeters/argument_parsing/issues'
metadata['project_urls']['Bug Tracker'] = bug_tracker_url

metadata.update(author='Florian Peters',
                version='0.0.1',
                description='A zero dependency argument parser written in python.')

metadata.update(packages             = find_packages(where='.'),
                include_package_data = True,
                zip_safe             = False)

try:
    metadata['long_description']              = open('README.md').read()
    metadata['long_description_content_type'] = 'text/markdown'
except FileNotFoundError: pass

setup(**metadata)