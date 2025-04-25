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
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children=children, props=props)

    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag must be required")
        if self.children is None:
            raise ValueError("children must be required")
        html = f"<{self.tag}>{self.props_to_html()}"

        for child in self.children:
            html += child.to_html()
        return html + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
