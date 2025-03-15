from textnode import TextNode, TextType
from leafnode import LeafNode
import re

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)


def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        split_node = node.text.split(delimiter)
        if len(split_node)%2 == 0 or len(split_node) == 1:
            raise Exception(f"invalid syntax - missing {delimiter}")
        for i in range(0, len(split_node)):
            node_type = TextType.TEXT
            if i%2 !=0:
                match(delimiter):
                    case("_"):
                        node_type = TextType.ITALIC
                    case("**"):
                        node_type = TextType.BOLD
                    case("`"):
                        node_type = TextType.CODE
                    case _:
                        raise Exception(f"invalid delimiter {delimiter}")
            
            new_nodes.append(TextNode(split_node[i], node_type))
    
    return new_nodes

def extract_markdown_images(text):
    urls = re.findall(r"\(([^\(\)]*)\)", text)
    alt_text = re.findall(r"!\[([^\[\]]*)\]", text)
    tuples = []
    for i in range(0, len(urls)):
        trimmed_url = urls[i].replace("(", "").replace(")", "")
        trimmed_alt = alt_text[i].replace("![", "").replace("]", "")
        tuples.append((trimmed_alt, trimmed_url))
    return tuples

def extract_markdown_links(text):
    urls = re.findall(r"\(([^\(\)]*)\)", text)
    alt_text = re.findall(r"(?<!!)\[([^\[\]]*)\]", text)
    tuples = []
    for i in range(0, len(urls)):
        trimmed_url = urls[i].replace("(", "").replace(")", "")
        trimmed_alt = alt_text[i].replace("[", "").replace("]", "")
        tuples.append((trimmed_alt, trimmed_url))
    return tuples
        

main()