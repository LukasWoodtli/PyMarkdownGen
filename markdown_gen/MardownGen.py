__author__ = 'Boot'

from collections import defaultdict

def gen_table(data):
    # calculate max size of each column
    columnSizes = defaultdict(int)
    for row in data:
        for column, cell in enumerate(row):
            columnSizes[column] = max(columnSizes[column], len(cell))

    # headers
    str = "|"
    for col, cell in enumerate(data[0]):
        FORMAT_STR = " {{:<{}}} |".format(columnSizes[col])
        str += FORMAT_STR.format(cell)
    str += "\n"

    # headers separating line
    str += "|"
    for i in range(len(data[0])):
        str += "-" * columnSizes[i] + "--|" # add 2 dashes for spacing around text
    str += "\n"

    # rest of table
    for row in data[1:]:
        str += "|"
        for col, cell in enumerate(row):
            FORMAT_STR = " {{:<{}}} |".format(columnSizes[col])
            str += FORMAT_STR.format(cell)
        str += "\n"


    return str


def gen_heading(headingText, depth = 1, alternative = False):
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
    if text is "" and alternativeText is "":
        return url
    elif alternativeText is "":
        return '[{}]({})'.format(text, url)
    else:
        return '[{}]({} "{}")'.format(text, url, alternativeText)

def gen_image_link(url, title, alt_text):
    return '![{}]({} "{}")'.format(alt_text, url, title)

def gen_reference(reference_id, reference_text, text="", references_list = None):
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
    return "  \n"

def gen_section():
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

def gen_un_ordered_list(list_items, bullet_char = "*"):
    str = ""
    for item in list_items:
        str += "{} {}\n".format(bullet_char, item)
    return str
