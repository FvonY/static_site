from textnode import TextNode, TextType

def main():
    textnode = TextNode("Node name", TextType.BOLD, "https://www.google.com")
    print(textnode)

if __name__ == "__main__":
    main()
    