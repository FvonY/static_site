from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode.tag is missing")
        if self.children is None:
            raise ValueError("ParentNode.children is missing")
        
        html_of_children_list = []
        for child in self.children:
            html_of_children_list.append(child.to_html())
            
        html_of_children_string = "".join(html_of_children_list)
        
        return f'<{self.tag}>{html_of_children_string}</{self.tag}>'
        
        