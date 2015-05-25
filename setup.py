from setuptools import setup
exec(open('PyMarkdownGen/version.py').read())


setup(name='PyMarkdownGen',
      version=__version__,
      description='Library to generate markdown formatted text',
      url='https://github.com/LukasWoodtli/PyMarkdownGen',
      author='Lukas Woodtli',
      author_email='woodtli.lukas@gmail.com',
      license='Eclipse Public License - v 1.0',
      packages=['PyMarkdownGen'],
      zip_safe=False)
