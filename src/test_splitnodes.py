import unittest

from textnode import TextNode, TextType
from main import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):

    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual([
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                        ], new_nodes)
        
    def test_missing_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "`", TextType.CODE))

    def test_multi_split(self):
        node = TextNode("This is **text** with two **bold** words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual([
                            TextNode("This is ", TextType.TEXT),
                            TextNode("text", TextType.BOLD),
                            TextNode(" with two ", TextType.TEXT),
                            TextNode("bold", TextType.BOLD),
                            TextNode(" words", TextType.TEXT),
                        ], new_nodes)
        
    def test_wrong_delimiter(self):
        node = TextNode("This is text with a .code block. word", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], ".", TextType.CODE))


if __name__ == "__main__":
    unittest.main()