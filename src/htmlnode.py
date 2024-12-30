class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This feature needs to implemented")

    def props_to_html(self):
        if self.props == None:
            raise Exception("No html attributes provided")
        attributes = ""
        for prop in self.props:
            value = self.props[prop]
            attributes += f' {prop}="{self.props[prop]}" '

        return attributes

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"




