from leafnode import LeafNode
from textnode import TextNode, TextType
import re


def text_node_to_html_node(text_node: 'TextNode'):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value=text_node.text, props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Undefined TextNode.text_type")
        
    
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:      
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        fragments = node.text.split(delimiter)
        
        if len(fragments) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in range(len(fragments)):
            if fragments[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(fragments[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(fragments[i], text_type))
        
    return new_nodes


def extract_markdown_images(text):
    re_alt_image = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(re_alt_image, text)
    return matches
    
    
def extract_markdown_links(text):
    re_alt_link = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(re_alt_link, text)
    return matches
    

def split_nodes_image(old_nodes: list[TextNode]):
    # find images
    # split node text on image
    # construct new nodes from this
    # append
    new_nodes = []
    if len(old_nodes) == 0:
            return new_nodes
    
    for old_node in old_nodes:       
        if old_node.text == "":
            continue
        
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        image_list = extract_markdown_images(old_node.text)
        if len(image_list) == 0:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
            
        for image_link in image_list:
            image_text = image_link[0]
            image_url = image_link[1]
            
            image_string = f'![{image_text}]({image_url})'
            pre_string, post_string = text.split(image_string, 2)

            pre_node = TextNode(pre_string, TextType.TEXT)
            image_node = TextNode(image_text, TextType.IMAGE, image_url)
            
            if len(pre_node.text) != 0:
                new_nodes.append(pre_node)
            new_nodes.append(image_node)
            
            text = post_string
            
        if len(text) != 0:
            final_node = TextNode(text, TextType.TEXT)
            new_nodes.append(final_node)
            
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    # find links
    # split node text on link
    # construct new nodes from this
    # append
    new_nodes = []
    if len(old_nodes) == 0:
            return new_nodes
    
    for old_node in old_nodes:       
        if old_node.text == "":
            continue
        
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        link_list = extract_markdown_links(old_node.text)
        if len(link_list) == 0:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
            
        for link_link in link_list:
            link_text = link_link[0]
            link_url = link_link[1]
            
            link_string = f'[{link_text}]({link_url})'
            pre_string, post_string = text.split(link_string, 2)

            pre_node = TextNode(pre_string, TextType.TEXT)
            link_node = TextNode(link_text, TextType.LINK, link_url)
            
            if len(pre_node.text) != 0:
                new_nodes.append(pre_node)
            new_nodes.append(link_node)
            
            text = post_string
            
        if len(text) != 0:
            final_node = TextNode(text, TextType.TEXT)
            new_nodes.append(final_node)
            
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    blocks = []
    for block in sections:
        block = block.strip()
        
        if len(block) != 0:
            blocks.append(block)
            
    return blocks