from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    # obj = TextNode("This is some text", TextType.LINK, "https://www.boot.dev")
    # print(obj)
    # obj = HTMLNode("a", None, None, {"href": "google.com", "target": "blank"})
    obj = LeafNode("a", "text")
    obj2 = ParentNode("p", [obj])
    # print(obj2.to_html())

main()