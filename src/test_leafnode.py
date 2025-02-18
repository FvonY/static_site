import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html_tag_value(self):
        node = LeafNode(tag="h1", value="Hello World")
        self.assertEqual(
            node.to_html(),
            "<h1>Hello World</h1>"
        )
        
    def test_to_html_tag_value_props(self):
        node = LeafNode(
            tag="a",
            value="Click Me!",
            props={"href": "https://google.com"}
        )
        self.assertEqual(node.to_html(),
                         '<a href="https://google.com">Click Me!</a>')
        
    def test_to_html_value_missing(self):
        node = LeafNode(
            tag="p",
            value=None
        )
        self.assertRaises(ValueError, node.to_html)
        
    def test_to_html_tag_missing(self):
        node = LeafNode(
            tag=None,
            value="Zehn kleine Jägermeister"
        )
        self.assertEqual(node.to_html(), "Zehn kleine Jägermeister")
        
if __name__ == "__main__":
    unittest.main()
