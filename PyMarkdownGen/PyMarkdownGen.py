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

    The first row of data is used as headers for the
    table.

    Args:
      data (2d-list of strings): The data to be represented as table.
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
    column_sizes = defaultdict(int)
    for row in data:
        for column, cell in enumerate(row):
            column_sizes[column] = max(column_sizes[column], len(cell))

    # headers
    md_str = "|"
    for col, cell in enumerate(data[0]):
        format_str = " {{:" + aligning[col] + "{}}} |"
        format_str = format_str.format(column_sizes[col])
        md_str += format_str.format(cell)
    md_str += "\n"

    # headers separating line
    md_str += "|"
    for i in range(len(data[0])):
        left_char = "-"
        right_char = "-"
        if aligning[i] == '>':
            right_char = ":"
        elif aligning[i] == '^':
            left_char = ":"
            right_char = ":"

        md_str += left_char + "-" * column_sizes[i] + right_char + "|"
    md_str += "\n"

    # rest of table
    for row in data[1:]:
        md_str += "|"
        for col, cell in enumerate(row):
            format_str = " {{:" + aligning[col] + "{}}} |"
            format_str = format_str.format(column_sizes[col])
            md_str += format_str.format(cell)
        md_str += "\n"


    return md_str


def gen_heading(heading_text, depth=1, alternative=False):
    """Creates a Markdown heading.

    This function creates a heading of the given depth. There
    is also an alternative format for the depth 1 and 2.
    A line break is added to the output.

    Args:
      headingText (string): The name of the heading.
      depth (int): The level (depth) of the heading.
      alternative (bool): If this is set to true and the depth is
        1 or 2 then the alternitive fotmat of headings is used.

    Returns:
      string: The heading text formatted as heading.

    """
    if alternative and depth == 1:
        md_str = heading_text + "\n"
        md_str += "=" * len(heading_text)
        return md_str + "\n"
    if alternative and depth is 2:
        md_str = heading_text + "\n"
        md_str += "-" * len(heading_text)
        return md_str + "\n"
    else:
        md_str = "#" * depth
        md_str += " "
        md_str += heading_text
        return md_str + "\n"


def gen_link(url, text="", alt_text=""):
    """Generate a link to an URL.

    Args:
      url (string): The URL for the link.
      text (string): The text to display instead of the URL.
      alt_text (string): The alternative text (usually
        displayed as tool tip).

    Returns:
      string: The URL formatted as Markdown link.

    """
    if text is "" and alt_text is "":
        return url
    elif alt_text is "":
        return '[{}]({})'.format(text, url)
    else:
        return '[{}]({} "{}")'.format(text, url, alt_text)


def gen_image_link(url, title, alt_text):
    """Generate a link to an image.

    Args:
      url (string): The URL for the image link.
      title (string): The title of the image to display.
      alt_text (string): The alternative text (if the image can not be displayed).

    Returns:
      string: The image URL formatted as Markdown link.

    """
    return '![{}]({} "{}")'.format(alt_text, url, title)



def gen_reference(reference_id, reference_text, text="", references_list=None):
    """Creates a in-file reference.

    A reference is contained by:
      - An ID (reference_id)
      - A text that is displayed later in the document (reference_text)
      - An optional text (text) that is displayed just before the id.

    Since the reference_text is displayed later in the document (usually at
    the end) all reference_text's can be collected in a list.

    Args:
      reference_id (string): This is a unique id to of the reference.
      reference_text (string): This is the text that should be displayed
        later in the document.
      text (string, optional): It's displayed just before the ID.
      reference_list (list of strings, optional): The reference text is
        added to this list and then the list is returned.

    Returns:
      string: The id and (optional) text.
      list of strings: Updated list with references for later use.

    """
    if text is "":
        md_str = " [{}]".format(reference_id)
    elif reference_id is "":
        reference_id = text
        md_str = "[{}][]".format(reference_id)
    else:
        md_str = "[{}][{}]".format(text, reference_id)
    ref = "[{}]: {}\n".format(reference_id, reference_text)
    if not references_list:
        references_list = []
    references_list.append(ref)
    return md_str, references_list


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
    """Creates text in italics.

    Args:
      text (string): The text to set to italics.
      alternative (bool): Use alternative format '_' instead of '*'

    Returns:
        string: The text formatted as italics.

    """
    if alternative:
        return "_" + text + "_"
    else:
        return "*" + text + "*"


def gen_bold(text, alternative=False):
    """Creates a bold text.

    Args:
      text (string): The text to set bolt.
      alternative (bool): If true '_' is used instead of '*'

    Returns:
      string: The bold formatted text.

    """
    if alternative:
        return "__" + text + "__"
    else:
        return "**" + text + "**"


def gen_monospace(text):
    """Creates a monospace typed text.

    This is often used for source code formatting.

    Args:
      text (string): The text to be formatted with
        monospace.

    Returns:
      string: The monospace formatted text.

    """
    return "`" + text + "`"


def gen_strikethrough(text):
    """ Strikes through the provided text.

    Args:
      text (string): The text to be strike through.

    Returns:
      The formatted markdown text.

    """
    return "~~" + text + "~~"


def gen_ordered_list(list_items):
    """Generates a numbered list.

    Args:
     list_items (list of strings): The items to be listed.

    Returns:
      The markdown formatted list.

    """
    # if isinstance(a, collections.Iterable):
    md_str = ""
    for i, text in enumerate(list_items):
        md_str += "{}. {}\n".format(i+1, text)

    return md_str

def gen_un_ordered_list(list_items, bullet_char="*"):
    """Generates a bullet list.

    The bullet character can be provided.

    Args:
     list_items (list of strings): The items to be listed.
     bullet_char (char, optional): The bullet character '*'
       is default.

    Returns:
      string: The markdown formatted list.

    """
    md_str = ""
    for item in list_items:
        md_str += "{} {}\n".format(bullet_char, item)
    return md_str

def gen_block_quote(text, simple=False):
    """Creates a block quoted text.

    Args:
      text (string): The text in the block quote.
      simple (bool, optional): If simple is set true
        only the first line is marked with the block
        quote char ('>'). Otherwise all lines are
        marked with the block quote char.

    Returns
      string: The formatted text as block quote.

    """
    if simple:
        return "> " + text + "\n"
    else:
        text = text.splitlines()
        md_str = ""
        for line in text:
            md_str += "> " + line + "\n"
        return md_str


def gen_html_comments(comment_text):
    """Add a HTML comment block.

    Args:
      comment_text (string): The text in the comment.

    Returns: The HTML comment with the given text.

    """

    return "<!-- " + comment_text + " -->"
