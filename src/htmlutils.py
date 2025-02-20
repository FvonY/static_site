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
    
    node = ParentNode(f"h{n}", text_to_children(text))
    return node


def handle_unordered_list_to_html(block):
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        sections = re.findall(r"([-*]+) (.*)", line)
        pre, text = sections[0]
        
        list_node = ParentNode("li", text_to_children(text))
        list_items.append(list_items)
    
    unordered_list_node = ParentNode("ul", list_items)
    return unordered_list_node


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
                children = []
                
                for line in block.split("\n"):
                    child_node = LeafNode("li", line)
                    children.append(child_node)
                
                node = ParentNode("ul", children)
                nodes.append(node)
                
            case BlockType.ORDERED_LIST:
                children = []
                
                for line in block.split("\n"):
                    child_node = LeafNode("li", line)
                    children.append(child_node)
                    
                node = ParentNode("ol", children)
                nodes.append(node)
                
            case BlockType.CODE:
                code_node = LeafNode("code", block)
                node = ParentNode("pre", code_node)
                nodes.append(node)
            
            case BlockType.QUOTE:
                node = LeafNode("blockquote", block)
                nodes.append(node)
            
            case BlockType.PARAGRAPH:
                node = LeafNode("p", block)
                nodes.append(node)
                
    #print(nodes)
    
    mother_node = ParentNode("div", nodes)
    
    for node in nodes:
        print(node.to_html())
            
    pass