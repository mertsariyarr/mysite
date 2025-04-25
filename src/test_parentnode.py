import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
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

    def test_to_html_with_props(self):
        grandchild_node = LeafNode("b", "sometext")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("a", [child_node], {"href": "google.com"})
        self.assertEqual(parent_node.to_html(), '<a> href="google.com"<span><b>sometext</b></span></a>')


    def test_repr(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("div", child_node, {"href": "google.com"})
        self.assertEqual(parent_node.__repr__(), "ParentNode(div, LeafNode(b, child, None), {'href': 'google.com'})")

    def test_err(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("div", None, {"href": "google.com"})
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_err2(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode(None, child_node)
        with self.assertRaises(ValueError):
            parent_node.to_html()

       








if __name__ == "__main__":
    unittest.main()




