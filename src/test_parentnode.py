import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html_tag_value(self):
        node1 = LeafNode(tag="h1", value="Node1")      
        node2 = LeafNode(tag="h1", value="Node2")
        
        parent_node = ParentNode(tag="p", children=[node1, node2])
        self.assertEqual(parent_node.to_html(),
                         """<p><h1>Node1</h1><h1>Node2</h1></p>""")
        
    def test_to_html_nested_parents(self):
        node1 = LeafNode(tag="h1", value="Node1")      
        node2 = LeafNode(tag="h1", value="Node2")
        parent_node1 = ParentNode(tag="p", children=[node1, node2])
        
        node3 = LeafNode(tag="a", value="Node3", props={"href": "wow.com"})      
        node4 = LeafNode(tag="a", value="Node4", props={"href": "reddit.com"})
        parent_node2 = ParentNode(tag="div", children=[node3, node4])
        
        parent_node_top = ParentNode(tag="p", children=[parent_node1, parent_node2])
        self.assertEqual(parent_node_top.to_html(),
                         """<p><p><h1>Node1</h1><h1>Node2</h1></p><div><a href="wow.com">Node3</a><a href="reddit.com">Node4</a></div></p>""")
        
    def test_to_html_minimal_page(self):
        node_title = LeafNode(tag="title", value="Title")
        node_head = ParentNode(tag="head", children=[node_title])
        node_p = LeafNode(tag="p", value="Hier steht Text.")
        
        node_body = ParentNode(tag="body", children=[node_p])
        node_html = ParentNode(tag="html", children=[node_head, node_body])
        
        self.assertEqual(node_html.to_html(),
                         """<html><head><title>Title</title></head><body><p>Hier steht Text.</p></body></html>""")
        
        
if __name__ == "__main__":
    unittest.main()
