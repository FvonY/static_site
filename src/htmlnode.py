class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        html_props = ""
        if self.props is None:
            return html_props
        for prop in self.props.items():
            key, value = prop
            html_props += f' {key}="{value}"'
        return html_props

    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})")
        