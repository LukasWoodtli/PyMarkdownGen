
__author__ = 'Boot'

from . import PyMarkdownGen as pmg

class Document(object):

    def __init__(self, file_path=""):
        self.file_path = file_path
        self.md_text = ""
        self.references_list = []

    def add_text(self, text):
        self.md_text += text

    def add_table(self, data, aligning=None):
        self.md_text += pmg.gen_table(data, aligning)


    def add_heading(self, heading_text, depth=1, alternative=False):
        self.md_text += pmg.gen_heading(heading_text, depth, alternative)


    def add_link(self, url, text="", alt_text=""):
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
