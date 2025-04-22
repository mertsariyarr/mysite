from textnode import TextNode, TextType

def main():
    obj = TextNode("This is some text", TextType.LINK, "https://www.boot.dev")
    print(obj)


main()