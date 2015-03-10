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





def main():
    data = [
        ["abcdefghij", "aaa", "b"],
        ["b", "c", "b"],
        ["dddddddddd", "a", "c"]
    ]

    print gen_table(data)


if __name__ == "__main__":
    main()
