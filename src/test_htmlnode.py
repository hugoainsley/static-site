import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            htmlnode = HTMLNode("p", "This is a paragraph", None, None)
            htmlnode.to_html()
    
    def test_props_to_html(self):
        htmlnode = HTMLNode("p", "This is a paragraph", None, {"align":"left"})
        props = htmlnode.props_to_html()
        self.assertEqual(props, ' align="left"')

    def test_repr(self):
        htmlnode = HTMLNode("p", "This is an HTML node", None, {"align":"left"})
        self.assertEqual(str(htmlnode), "HTMLNode(p, This is an HTML node, None, {'align': 'left'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_value_none(self):
        with self.assertRaises(ValueError):
            leafnode = LeafNode("p", None)
            leafnode.to_html()

    def test_tag_none(self):
        leafnode = LeafNode(None, "Hello, world!")
        self.assertEqual(leafnode.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)
            parent_node.to_html()

    def test_to_html_with_no_tag(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None, "child")
            parent_node.to_html()
