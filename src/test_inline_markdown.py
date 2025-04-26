import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_text
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is a text with a **bolded** word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],new_node
        )
    def test_delim_bold_double(self):
        node = TextNode("This is a text with **bold** and another **bolder**", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and another ", TextType.TEXT),
                TextNode("bolder", TextType.BOLD)
            ], new_node
        )

    def test_delim_italic(self):
        node = TextNode("This is a text with _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
                
            ], new_nodes
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


class TestExtractImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        matches2 = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches2)
        matches3 = extract_markdown_images(
            "This is a text without any links or images"
        )
        self.assertListEqual([], matches3)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_text(
            "This is a text with [alt text](https:google.com)"
        )
        self.assertListEqual([("alt text", "https:google.com")], matches)
        matches2 = extract_markdown_text(
            "This is a text with [alt text](https:google.com) and this is an another text of [second text](google.com)"
        )
        self.assertListEqual([("alt text", "https:google.com"), ("second text", "google.com")], matches2)
        matches3 = extract_markdown_text(
            "This is a text without any link."
        )
        self.assertListEqual([], matches3)



    
if __name__ == "__main__":
    unittest.main()


