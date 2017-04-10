from setuptools import find_packages
from setuptools import setup

setup(name='scraping',
      setup_requires=['setuptools_scm'],
      use_scm_version={'write_to': 'scraping/version.txt'},
      description="package for scraping data from rakuten.co.jp",
      packages=find_packages(),
      test_suite = 'tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/scraping-run'],
      zip_safe=False)
