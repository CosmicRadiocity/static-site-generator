import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_to_string(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("HTMLNode(a, None, None, href=\"https://www.google.com\" target=\"_blank\")", str(node))

    def test_props_to_html(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())

    def test_to_html(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(NotImplementedError, lambda: node.to_html())
        


if __name__ == "__main__":
    unittest.main()