from textnode import TextNode, TextType
from utils import *
from blockutils import *
from htmlutils import *

def main():
    # textnode = TextNode("Node name", TextType.BOLD, "https://www.google.com")
    # print(textnode)
    
    # node1 = TextNode("Hallo, ![schwarzes ross auf rotem grund](https://ferrari.com) und so weiter", TextType.TEXT)
    # node2 = TextNode("Hier ist nichts", TextType.TEXT)
    # node3 = TextNode("Es gibt erstens ![erster bild text](https://erstesbild.com) und zweites ![https://zweiter bild text](zweitesbild.com)", TextType.TEXT)
    # node4 = TextNode("![only image](https://onlyimage.com)", TextType.TEXT)
    
    # nodes = [node1, node2, node3, node4]
    
    # split_nodes = split_nodes_image(nodes)
    # for node in split_nodes:
    #     print(node)
    
    # text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    # print(text_to_textnodes(text))
    
    # print(block_to_block_type("### Hallo"))
    # print(block_to_block_type("Ne, der nicht"))
    # print(block_to_block_type("######## Kein Heading"))
    # print(block_to_block_type("- eins\n- zwei"))
    # print(block_to_block_type("1. erstens\n2. zweitens"))
    # print(block_to_block_type("```bool echte() { return false; }```"))
    # print(block_to_block_type("> No amount of money ever bought a second of time\n> Alohomora"))
    # print(block_to_block_type("######## Kein Heading"))

    with open("src/markdown.md", "r") as markdown:
        markdown_to_html_node(markdown.read())
    markdown.close()


if __name__ == "__main__":
    main()
    