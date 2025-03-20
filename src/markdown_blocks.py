from enum import Enum
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode
from node_funcs import text_node_to_html_node, text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            blocks.remove(blocks[i])
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED
    return BlockType.PARAGRAPH

def block_type_to_tag(block_type, heading_amount=1):
    match(block_type):
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.CODE:
            return "code"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED:
            return "ul"
        case BlockType.ORDERED:
            return "ol"
        case BlockType.HEADING:
            return f"h{heading_amount}"
        case _:
            raise Exception("invalid block type")
        
def text_to_children(text, block_type):
    nodes = []
    match(block_type):
        case BlockType.QUOTE:
            text = text.replace("> ", "")
            text = text.replace("\n", " ")
            text_nodes = (text_to_textnodes(text))
            for text_node in text_nodes:
                    print(text_node)
                    nodes.append(text_node_to_html_node(text_node))
        case BlockType.PARAGRAPH:
            text = text.replace("\n", " ")
            text_nodes = (text_to_textnodes(text))
            for text_node in text_nodes:
                    print(text_node)
                    nodes.append(text_node_to_html_node(text_node))
        case BlockType.HEADING:
            text = text.replace("#", "").strip()
            lines = text.split("\n")
            for line in lines:
                text_nodes = (text_to_textnodes(line))
                for text_node in text_nodes:
                    nodes.append(text_node_to_html_node(text_node))
        case BlockType.UNORDERED:
            text = text.replace("-", "").strip()
            lines = text.split("\n")
            for line in lines:
                text_nodes = (text_to_textnodes(line))
                children = []
                for text_node in text_nodes:
                    children.append(text_node_to_html_node(text_node))
                nodes.append(ParentNode("li", children))
        case BlockType.ORDERED:
            lines = text.split("\n")
            for line in lines:
                line = line[3:]
                text_nodes = (text_to_textnodes(line))
                children = []
                for text_node in text_nodes:
                    children.append(text_node_to_html_node(text_node))
                nodes.append(ParentNode("li", children))
        case BlockType.CODE | _:
            raise Exception("invalid block type")
    return nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print(block_type)
        if block_type == BlockType.HEADING:
            heading_amount = len(block.split(" ")[0])
            tag = block_type_to_tag(block_type, heading_amount)
        else:
            tag = block_type_to_tag(block_type)
        if block_type == BlockType.CODE:
            block = block.replace("```\n", "").replace("```", "")
            node = ParentNode("pre", [text_node_to_html_node(TextNode(block, TextType.CODE))])
        else:
            node = ParentNode(tag, text_to_children(block, block_type))
        nodes.append(node)
    return ParentNode("div", nodes)