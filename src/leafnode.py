from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)        
        
    def to_html(self):
        if self.value is None:
            raise ValueError(f"LeafNode value is None. Tag: {self.tag} URL: {self.url}")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"