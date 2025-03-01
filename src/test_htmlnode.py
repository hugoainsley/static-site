import unittest

from htmlnode import HTMLNode

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
