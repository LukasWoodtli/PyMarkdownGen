# -*- coding: utf-8 -*-
"""This file contains the API for a Markdown
document. It's a simple Object Oriented API."""
__author__ = 'Lukas Woodtli'

from . import PyMarkdownGen as pmg

class Document(object):
    """This class represents a Markdown document.
    
    Usually a document is saved in a single file.
    
    """

    
    def __init__(self, file_path=""):
        """The constructor generates a Markdown
        document.
        
        Args:
          file_path (string, optional): the path
            of the Markdown document.
            
        """
        
        self.file_path = file_path
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
        self.md_text += pmg.gen_image_link(url, title, alt_text)


    def add_reference(self, reference_id, reference_text, text=""):
        md_text, references = pmg.gen_reference(reference_id,
                                                reference_text,
                                                text,
                                                self.references_list)
        self.md_text += md_text
        self.references_list = references


    def add_new_line(self):
        self.md_text += pmg.gen_new_line()


    def add_section(self):
        self.md_text += pmg.gen_section()


    def add_italic(self, text, alternative=False):
        self.md_text += pmg.gen_italic(text, alternative)


    def add_bold(self, text, alternative=False):
        self.md_text += pmg.gen_bold(text, alternative)


    def add_monospace(self, text):
        self.md_text += pmg.gen_monospace(text)


    def add_strikethrough(self, text):
        self.md_text += pmg.gen_strikethrough(text)


    def add_ordered_list(self, list_items):
        self.md_text += pmg.gen_ordered_list(list_items)


    def add_un_ordered_list(self, list_items, bullet_char="*"):
        self.md_text += pmg.gen_un_ordered_list(list_items, bullet_char)


    def add_block_quote(self, text, simple=False):
        self.md_text += pmg.gen_block_quote(text, simple)


    def get_markdown_text(self, append_references=False):
        if append_references:
            self.md_text += "\n"
            for ref in self.references_list:
                self.md_text += ref

        return self.md_text

    def save_file(self):
        with open(self.file_path, 'w') as out_file:
            out_file.writelines(self.md_text)
