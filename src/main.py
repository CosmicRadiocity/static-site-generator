from textnode import TextNode, TextType
from filecopy import copy_files
from pagegenerator import generate_pages_recursive
import os

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./static/content"
template_path = "./static/template.html"

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    copy_files("static", "public")
    generate_pages_recursive(
        os.path.join(dir_path_content),
        template_path,
        os.path.join(dir_path_public),
    )

main()