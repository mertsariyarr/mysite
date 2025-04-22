from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    # obj = TextNode("This is some text", TextType.LINK, "https://www.boot.dev")
    # print(obj)
    obj = HTMLNode("a", None, None, {"href": "google.com", "target": "blank"})
    print(obj)
main()