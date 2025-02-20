from utils import *
from blockutils import *
from parentnode import ParentNode
from leafnode import LeafNode
import re


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def handle_heading_to_html(block):
    sections = re.findall(r"(#{1,6}) (.*)", block)
    pre, text = sections[0]
    n = len(pre)
    
    header_node = ParentNode(f"h{n}", text_to_children(text))
    return header_node


def handle_unordered_list_to_html(block):
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        sections = re.findall(r"([-*]+) (.*)", line)
        pre, text = sections[0]
        
        list_node = ParentNode("li", text_to_children(text))
        list_items.append(list_node)
    
    unordered_list_node = ParentNode("ul", list_items)
    return unordered_list_node


def handle_ordered_list_to_html(block):
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        sections = re.findall(r"(\d+)\. (.*)", line)
        pre, text = sections[0]
        
        list_node = ParentNode("li", text_to_children(text))
        list_items.append(list_node)
        
    ordered_list_node = ParentNode("ol", list_items)
    return ordered_list_node


def handle_code_to_html(block):
    text = block[3:-3]
    
    #sections = text.split("\n")
    #text = " ".join(sections)
    text = text.lstrip("\n")
    
    code_node = ParentNode("code", text_to_children(text))
    return ParentNode("pre", [code_node])


def handle_quote_to_html(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        else:
            stripped_lines.append(line.lstrip(">").strip())
    stripped_quote = " ".join(stripped_lines)
    
    quote_node = ParentNode("blockquote", text_to_children(stripped_quote))
    return quote_node


def handle_paragraph_to_html(block):
    lines = block.split("\n")
    text = " ".join(lines)
    paragraph_node = ParentNode("p", text_to_children(text))
    return paragraph_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    block_types = []
    for block in blocks:
        block_types.append(block_to_block_type(block))
        
    
    nodes = []
    for block, type in zip(blocks, block_types):
        #print(block, type)
        match type:
            case BlockType.HEADING:
                nodes.append(handle_heading_to_html(block))
                
            case BlockType.UNORDERED_LIST:
                nodes.append(handle_unordered_list_to_html(block))
                
            case BlockType.ORDERED_LIST:
                nodes.append(handle_ordered_list_to_html(block))
                
            case BlockType.CODE:
                nodes.append(handle_code_to_html(block))
            
            case BlockType.QUOTE:
                nodes.append(handle_quote_to_html(block))
            
            case BlockType.PARAGRAPH:
                nodes.append(handle_paragraph_to_html(block))
                
    # print(nodes)
    
    mother_node = ParentNode("div", nodes)
    
    # print(mother_node.to_html())
    # for node in nodes:
    #     print(node.to_html())
    return mother_node
