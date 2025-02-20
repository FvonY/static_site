from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block: str):
    # HEADING
    heading_starts = ("#", "##", "###", "####", "#####", "######")
    sections = block.split(" ", 1)
    if sections[0] in heading_starts:
        return BlockType.HEADING
    
    # CODE
    ticks = "```"
    if block.startswith(ticks) and block.endswith(ticks):
        return BlockType.CODE
    
    # QUOTE
    lines = block.split("\n")
    ret_quote = True
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            ret_quote = False
            break
    if ret_quote:
        return BlockType.QUOTE

    # UNORDERED_LIST
    ret_ul = True
    for line in lines:
        if line.startswith("* ") or line.startswith("- "):
            continue
        else:
            ret_ul = False
            break
    if ret_ul:
        return BlockType.UNORDERED_LIST
    
    # ORDERED_LIST
    ret_ol = True
    n = 1
    for line in lines:
        if line.startswith(f"{n}. "):
            n += 1
            continue
        else:
            ret_ol = False
    if ret_ol:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH