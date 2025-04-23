class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        return False

    def to_html(self):
        raise NotImplementedError("error")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        

    def to_html(self):
        if self.value is None:
            raise ValueError("value must be required")
        if self.tag is None:
            return self.value
        
        myProp = super().props_to_html()
        return f"<{self.tag}{myProp}>{self.value}</{self.tag}>"
        