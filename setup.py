from sphinxtheme_replicape import _version as version

from setuptools import setup

# README into long description
# with codecs.open('README.rst', encoding='utf-8') as f:
#     readme = f.read()

setup(
    name='sphinxtheme_replicape',
    version=version.__version__,
    description='Theme based on Prettydocs theme',
    long_description='Theme for Sphinx',
    author='Andrew Mirsky',
    author_email='andrew@mirskytech.com',
    url='https://github.com/replicape/sphinx-replicape',
    packages=['sphinxtheme_replicape'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'replicape = sphinxtheme_replicape',
        ]
    },
    classifiers=[
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
    ],
)
