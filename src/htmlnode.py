class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props is not None:
            for prop in self.props:
                html += f' {prop}="{self.props[prop]}"'
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        match None:
            case self.value:
                raise ValueError("All leaf nodes must have a value")
            case self.tag:
                return str(self.value)
            case _:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        match None:
            case self.tag:
                raise ValueError("All parent nodes must have a tag")
            case self.children:
                raise ValueError("All children must have a value")
            case _:
                children_html = ""
                for child in self.children:
                    children_html += child.to_html()
                return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

