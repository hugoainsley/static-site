import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
