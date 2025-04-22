import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr_(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual("TextNode(This is a text node, bold, google.com)", node.__repr__())
        

if __name__ == "__main__":
    unittest.main()