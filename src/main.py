from textnode import TextNode, TextType
from filecopy import copy_files
from pagegenerator import generate_pages_recursive
import os
import sys


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./static/content"
template_path = "./static/template.html"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print(basepath)
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    copy_files("static", "docs")
    generate_pages_recursive(
        os.path.join(dir_path_content),
        template_path,
        os.path.join(dir_path_public),
        basepath
    )

main()