# -*- coding: utf-8 -*-
"""This file contains the API for a Markdown
document. It's a simple Object Oriented API."""
__author__ = 'Lukas Woodtli'

from . import PyMarkdownGen as pmg

class Document(object):
    """This class represents a Markdown document.

    Usually a document is saved in a single file.

    """


    def __init__(self):
        """The constructor generates a Markdown
        document.

        Args:
          file_path (string, optional): the path
            of the Markdown document.

        """

        self.md_text = ""
        self.references_list = []


    def add_text(self, text):
        """Adds a plain text.

        This is just a convenience function.

        """

        self.md_text += text


    def add_table(self, data, aligning=None):
        """Adds a table to the Markdown document.

        Args:
          data (2-d list of strings): The data to be
            represented as a table. The first row is used
            as column titles.
          aligning (list of chars): Sets the alignment for
            each column:
            '<': left align
            '>': right align
            '^': center

            Default is left align.

        """

        self.md_text += pmg.gen_table(data, aligning)


    def add_heading(self, heading_text, depth=1, alternative=False):
        """Adds a heading of the given depth to the document.

        Args:
          heading_text (string): The text of the heading.
          depth (int): The depth (level) of the heading.
          alternative (bool): For the depth 1 and 2 there is an alternative
            representation.
            on.

        """

        self.md_text += pmg.gen_heading(heading_text, depth, alternative)



    def add_link(self, url, text="", alt_text=""):
        """Adds a link to the document.

        Args:
          url (string): The URL for the link.
          text (string, optional): The text that is shown
            instead of the URL.
          alt_text(string,optional): The alternative text
            for the link.

        """

        self.md_text += pmg.gen_link(url, text, alt_text)



    def add_image_link(self, url, title, alt_text):
        """Add a link to an image.

        Args:
          url (string): The URL to the image.
          title (string): The title of the image.
          alt_text (string): An alternative text for the image.

        """

        self.md_text += pmg.gen_image_link(url, title, alt_text)


    def add_reference(self, reference_id, reference_text, text=""):
        """Add a in-file reference.

        Args:
          referece_id (string): The ID of the reference.
          reference_text (string): The text that is displayed
            later in the document.
          reference_text (string, optional): An alternative
            reference text.

        """

        md_text, references = pmg.gen_reference(reference_id,
                                                reference_text,
                                                text,
                                                self.references_list)
        self.md_text += md_text
        self.references_list = references


    def add_references_list(self):
        """Adds the list of references to the document
        and clears the list."""

        for ref in self.references_list:
            self.md_text += ref

        self.references_list = []


    def add_new_line(self):
        """Adds a new line to the Markdown document."""

        self.md_text += pmg.gen_new_line()



    def add_section(self):
        """Create a new section in the Markdown document."""

        self.md_text += pmg.gen_section()



    def add_italic(self, text, alternative=False):
        """Add italic text to the document.

        Args:
          text (string): Text to be set in italics.
          alternative (bool, optional): Use the alternative style.

        """

        self.md_text += pmg.gen_italic(text, alternative)


    def add_bold(self, text, alternative=False):
        """Add bokd text to document.

        Args:
          text (string): The text to type bolt.
          alternative(bool, optional): Use alternative style.

        """

        self.md_text += pmg.gen_bold(text, alternative)


    def add_monospace(self, text):
        """Add text that is typed in a mono space font.

        Args:
          text (string): The text that has to be typed
            in a mono space font.

        """

        self.md_text += pmg.gen_monospace(text)


    def add_strikethrough(self, text):
        """Add text that is striked through

        Args:
          text (string): Text to be striked.

        """

        self.md_text += pmg.gen_strikethrough(text)


    def add_ordered_list(self, list_items):
        """Creates an ordered list.

        Args:
          list_items (list of strings): The items to be
            listed.

        """
        self.md_text += pmg.gen_ordered_list(list_items)


    def add_un_ordered_list(self, list_items, bullet_char="*"):
        """Creates and adds an unordered list.

        The bullet char can be provided.

        Args:
          list_items (list of strings): The items to be
            listed.
          bullet_char (char, optional): The bullet character,
            default: '*'

        """

        self.md_text += pmg.gen_un_ordered_list(list_items, bullet_char)


    def add_block_quote(self, text, simple=False):
        """Add a block quote.

        Args:
          text (string): The text for the block quote.
          simple (bool, optional): If True only the first
            row is prepended witch '> '
        """

        self.md_text += pmg.gen_block_quote(text, simple)


    def add_html_comments(self, comment_text):
        """Adds a text as HTML comment to the document.

        Args:
          comment_text (string): The text to put in the
            c
            HTML comment in the document.

        """

        self.md_text += pmg.gen_html_comments(comment_text)



    def get_markdown_text(self, append_references=False):
        """Get the complete text with Markdown foratting.

        Args:
          append_references (bool, optional): If True it appends
            any reference added earlier in the document.
            Default: False

        """

        if append_references:
            self.add_section()
            self.add_references_list()

        return self.md_text


    def save_to_file(self, file_path):
        """Saves the Markdown text to the file with the
        given path.

        Args:
          file_path(string): The path of the file where
            the Markdown text is written to.
            If no file path is provided the path set in the
            constructor is taken. If either variables are set
            an error ocurs.

        """

        open(file_path, 'w').writelines(self.md_text)
