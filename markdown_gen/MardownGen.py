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
        FORMAT_STR = " {{:<{}}} |" .format(columnSizes[col])
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
            FORMAT_STR = " {{:<{}}} |" .format(columnSizes[col])
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
        return url + "\n"
    elif alternativeText is "":
        return '[{}]({})\n'.format(text, url)
    else:
        return '[{}]({} "{}")\n'.format(text, url, alternativeText)


def main():
    data = [
        ["abcdefghij", "aaa", "b"],
        ["b", "c", "b"],
        ["dddddddddd", "a", "c"]
    ]

    print gen_table(data)


if __name__ == "__main__":
    main()
