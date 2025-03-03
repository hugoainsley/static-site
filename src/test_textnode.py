import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node string", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(str(node), 'TextNode(This is a text node string, bold, https://www.boot.dev)')

    def test_text_type(self): 
        with self.assertRaises(NameError):
            node = TextNode("Test text type", BOLD, "https://www.boot.dev")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_invalid_text_type(self):
        with self.assertRaises(ValueError):
            node = TextNode("span", "SPAN")
            html_node = text_node_to_html_node(node)

    def test_text_image(self):
        node = TextNode("Image alt text", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        
if __name__ == "__main__":
    unittest.main()
