import unittest

from htmlnode import HTMLNode

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

   
            
        
    

if __name__ == "__main__":
    unittest.main()




