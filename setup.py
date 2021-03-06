# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import pkutils
import tsenum

requirements = list(pkutils.parse_requirements('requirements.txt'))
dependencies = list(pkutils.parse_requirements('requirements.txt', True))
readme = pkutils.read('README.md')
module = pkutils.parse_module('tsenum/__init__.py')
version = module.__version__
project = 'tsenum'
user = 'aboehm'

setup(
  name=project,
  version=version,
  description=module.__description__,
  long_description=readme,
	long_description_content_type='text/markdown',
  author=module.__author__,
  author_email=module.__email__,
  install_requires=requirements,
  dependency_links=dependencies,
  url=pkutils.get_url(project, user),
  download_url=pkutils.get_dl_url(project, user, version),
  classifiers=[
		pkutils.get_status(version),
		'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
		'Programming Language :: Python :: 3',
		'Topic :: Utilities',
		'Operating System :: Unix',
		'Operating System :: POSIX',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft',
  ],
	packages=find_packages(),
	platforms=[
		'MacOS X',
		'Linux',
		'Windows',
	],
	entry_points = {
		'console_scripts': [
			'tsenum=tsenum.__main__:main',
		],
	},
	keywords='utils timestamp',
	tests_require=['pytest'],
)

# vim: ft=python tabstop=2 shiftwidth=2 noexpandtab :
