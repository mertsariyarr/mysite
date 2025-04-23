import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "text", None, {"href": "google.com", "target": "blank"})
        node2 = HTMLNode("a", "text", None, {"href": "google.com", "target": "blank"})
        self.assertEqual(node,node2)

    def test_err(self):
        node = HTMLNode("a", "text", None, {"href": "google.com", "target": "blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_prop(self):
        node = HTMLNode("a", "text", None, {"href": "google.com", "target": "blank"})
        self.assertEqual(' href="google.com" target="blank"', node.props_to_html())

   
    def test_values(self):
        node = HTMLNode("div", "I wish I could read",)
        self.assertEqual(node.tag, "div")  
        self.assertEqual(node.value, "I wish I could read")    
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"},)
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_prop(self):
        node = LeafNode("a", "this is a google", {"href": "google.com"})
        self.assertEqual(node.to_html(), '<a href="google.com">this is a google</a>')
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "google.com")
        self.assertEqual(node.to_html(), "google.com")




if __name__ == "__main__":
    unittest.main()




