from textnode import TextNode, TextType
from utils import *
from blockutils import *
from htmlutils import *
from os import mkdir, listdir
from os.path import exists, join, isfile
from shutil import copy, rmtree, copytree
import re


def copy_dir(source_dir, target_dir):
    rmtree(target_dir)
    #mkdir(target_dir)
    copytree(source_dir, target_dir)
    
    
def extract_title(markdown):
    title = re.findall(r"#{1} (.*){1}", markdown)[0]
    return title.strip()


def generate_page(from_path, template_path, dest_path):
    print(f"Generating from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path, "r") as md_file:
        markdown = md_file.read()
    md_file.close()
    
    html = markdown_to_html_node(markdown).to_html()
    
    template = ""
    with open(template_path, "r") as template_file:
        template = template_file.read()
    template_file.close()
    
    page = template.replace("{{ Title }}", extract_title(markdown))
    page = page.replace("{{ Content }}", html)
    
    with open(dest_path, "w") as dest_file:
        dest_file.write(page)
    dest_file.close()
    
    # print(html)
    
    
def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    dir = listdir(content_dir_path)
    print(dir)
    for d in dir:
        print(d, isfile(content_dir_path+"/"+d))
        if isfile(content_dir_path+"/"+d):
            if not exists(dest_dir_path):
                mkdir(dest_dir_path)
            generate_page(content_dir_path+"/index.md", template_path, dest_dir_path+"/index.html")
        else:
            generate_pages_recursive(content_dir_path+"/"+d, template_path, dest_dir_path+"/"+d)
    pass


def main():
    # with open("src/markdown.md", "r") as markdown:
    #     markdown_to_html_node(markdown.read())
    # markdown.close()
    
    # print("\n")
    # copy_dir("./static/", "./public/")
    # generate_page("./content/index.md", "template.html", "./public/index.html")
    generate_pages_recursive("./content", "template.html", "./public")


if __name__ == "__main__":
    main()
    