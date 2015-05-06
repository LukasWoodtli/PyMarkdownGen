# -*- coding: utf-8 -*-
"""Procedural API for generating Markdown.

This module provides Python functions for generating `Markdown`_ text.

.. _Markdown:
    http://daringfireball.net/projects/markdown/

"""
__author__ = 'Lukas Woodtli'

from collections import defaultdict


def gen_table(data, aligning=None):
    """Generates a table from a 2 dimentional list.
    
    The format of the generated table is as described at: 
    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables
    The function adds a new line to the end.

    The first row of data is used as headers for the table.
    
    Args:
      data 2d-list of strings: The data to be represented as table.
      aligning (list of strings): The aligning for each row. The entries have
        following meaning:
        '^' center
        '<' left align
        '>' right align
        If no aligning list is provided, all columns are left aligned. If the 
        aligning list has less entries than columns in data the remaining columns 
        are left aligned. If the provided aligning list has more entries than 
        columns in data the unused entries are ignored.
      
    Returns:
      string: A markdown string containing the table.
      
    """
    # no aligning: default is left
    if not aligning:
        aligning = ["<"] * len(data[0])

    if len(data[0]) > len(aligning):
        difference = len(data[0]) - len(aligning)
        aligning.extend(["<"] * difference)

    assert len(aligning) >= len(data[0])

    # calculate max size of each column
    columnSizes = defaultdict(int)
    for row in data:
        for column, cell in enumerate(row):
            columnSizes[column] = max(columnSizes[column], len(cell))

    # headers
    str = "|"
    for col, cell in enumerate(data[0]):
        FORMAT_STR = " {{:" + aligning[col] + "{}}} |"
        FORMAT_STR = FORMAT_STR.format(columnSizes[col])
        str += FORMAT_STR.format(cell)
    str += "\n"

    # headers separating line
    str += "|"
    for i in range(len(data[0])):
        left_char = "-"
        right_char = "-"
        if aligning[i] == '>':
            right_char = ":"
        elif aligning[i] == '^':
            left_char = ":"
            right_char = ":"

        str += left_char + "-" * columnSizes[i] + right_char + "|"
    str += "\n"

    # rest of table
    for row in data[1:]:
        str += "|"
        for col, cell in enumerate(row):
            FORMAT_STR = " {{:" + aligning[col] + "{}}} |"
            FORMAT_STR = FORMAT_STR.format(columnSizes[col])
            str += FORMAT_STR.format(cell)
        str += "\n"


    return str


def gen_heading(headingText, depth=1, alternative=False):
    """Creates a Markdown heading.
    
    This function creates a heading of the given depth. There
    is also an alternative format for the depth 1 and 2.
    A line break is added to the output.
    
    Args:
      headingText string: The name of the heading.
      depth int: The level (depth) of the heading.
      alternative bool: If this is set to true and the depth is
        1 or 2 then the alternitive fotmat of headings is used.
    
    Returns:
      string: The heading text formatted as heading.
      
    """
    if alternative and depth == 1:
        str = headingText + "\n"
        str += "=" * len(headingText)
        return str + "\n"
    if alternative and depth is 2:
        str = headingText + "\n"
        str += "-" * len(headingText)
        return str + "\n"
    else:
        str = "#" * depth
        str += " "
        str += headingText
        return str + "\n"


def gen_link(url, text="", alternativeText=""):
    """Generate a link to an URL.
    
    Args:
      url string: The URL for the link.
      text string: The text to display instead of the URL.
      alternativeText string: The alternative text (usually 
        displayed as tool tip).
      
    Returns:
      string: The URL formatted as Markdown link.
      
    """  
    if text is "" and alternativeText is "":
        return url
    elif alternativeText is "":
        return '[{}]({})'.format(text, url)
    else:
        return '[{}]({} "{}")'.format(text, url, alternativeText)


def gen_image_link(url, title, alt_text):
    """Generate a link to an image.
    
    Args:
      url string: The URL for the image link.
      title string: The title of the image to display.
      alt_text string: The alternative text (if the image can not be displayed).
      
    Returns:
      string: The image URL formatted as Markdown link.
      
    """ 
    return '![{}]({} "{}")'.format(alt_text, url, title)


0
def gen_reference(reference_id, reference_text, text="", references_list=None):
    if text is "":
        str = " [{}]".format(reference_id)
    else:
        str = "[{}][{}]".format(text, reference_id)
    ref = "[{}]: {}\n".format(reference_id, reference_text)
    if not references_list:
        references_list = []
    references_list.append(ref)
    return str, references_list
    
def gen_new_line():
    """Generate a new line.
    
    Markdown uses two spaces and a line break for creating a new line in
    the output.
    
    Returns:
      stringh The chars needed for a new line.
      
    """
    return "  \n"

def gen_section():
    """Create a new section.
    
    Markdown uses two line breaks to create a new section.
    
    Returns:
      string: The string with the characters for a new section.
      
    """
    return "\n\n"



def gen_italic(text, alternative=False):
    if alternative:
        return "_" + text + "_"
    else:
        return "*" + text + "*"

def gen_bold(text, alternative=False):
    if alternative:
        return "__" + text + "__"
    else:
        return "**" + text + "**"

def gen_monospace(text):
    return "`" + text + "`"

def gen_strikethrough(text):
    return "~~" + text + "~~"

def gen_ordered_list(list_items):
    # if isinstance(a, collections.Iterable):
    str = ""
    for i, text in enumerate(list_items):
        str += "{}. {}\n".format(i+1, text)

    return str

def gen_un_ordered_list(list_items, bullet_char="*"):
    str = ""
    for item in list_items:
        str += "{} {}\n".format(bullet_char, item)
    return str

def gen_block_quote(text, simple=False):
    if simple:
        return "> " + text + "\n"
    else:
        text = text.splitlines()
        str = ""
        for line in text:
            str += "> " + line + "\n"
        return str
