from textnode import TextNode, TextType
from filecopy import copy_files

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)
    copy_files("static", "public")

main()