import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "google.com")
        node4 = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

   
    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "google.com")
        self.assertEqual("TextNode(This is a text node, link, google.com)", repr(node))
    



if __name__ == "__main__":
    unittest.main()