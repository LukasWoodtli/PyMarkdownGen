API Documentation
=================

This Python library is divided in two parts. There is a Procedural API
that is used to construct Markdown strings. The functions in this part
of the library just return strings.

The second part of the library introduces a `Document` class. It is based
on the procedural API and adds some functionality. There are methods to add
Markdown text to the `Document` class. When the document is fully generated
the Markdown text can be saved to a file. Or it can be used 
for further processing from Python.

Procedural API
--------------
This is the simple procedural API that contains only simple functions.

.. automodule:: PyMarkdownGen.PyMarkdownGen
  :members:

Object Oriented API
-------------------
This APO is based on the simple procedural API. It wraps the procedural
API in a `Document` class and adds some functionality.

.. automodule:: PyMarkdownGen.Document
  :members:
