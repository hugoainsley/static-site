import unittest
from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split_node_code(self):
        node = TextNode("This is `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is ", TextType.TEXT, None), TextNode("code", TextType.CODE, None), TextNode("", TextType.TEXT, None)])

    def test_split_node_bold(self):
        node = TextNode("This is **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None), TextNode("", TextType.TEXT, None)])

    def test_split_node_italic(self):
        node = TextNode("This is _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None), TextNode("", TextType.TEXT, None)])
