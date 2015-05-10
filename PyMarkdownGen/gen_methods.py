__author__ = 'Boot'


def gen_stub(string):
    txt = string.strip()
    func_name = string.replace("\n", "")

    method_name = func_name.replace("gen_", "add_")
    method_name = "    " + method_name + "\n"

    func_call = func_name.replace(":", "").replace("def", "").strip()
    func_call = "        md_text = " + func_call + "\n\n"

    code = method_name + func_call

    return code


with open("PyMarkdownGen.py") as in_file:
    lines = in_file.readlines()
    lines = [line for line in lines if line.startswith("def")]
    for line in lines:
        print gen_stub(line)