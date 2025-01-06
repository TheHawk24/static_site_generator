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
            return ""
        attributes = ""
        for prop in self.props:
            value = self.props[prop]
            attributes += f' {prop}="{self.props[prop]}"'
        return attributes

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"



class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value")
        if self.tag == None:
            return self.value
        htmltag = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return htmltag

    def __eq__(self,node):
        if self.tag != node.tag:
            return False
        if self.value != node.value:
            return False
        if self.props != node.props:
            return False
        return True


    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):

    def __init__(self,tag, children, props=None):
        super().__init__(tag,children=children,props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("HTML tag is missing")
        if self.children == None:
            raise ValueError("Inline tags missing")
        htmltag = f"<{self.tag}{self.props_to_html()}>{"".join(list(map(lambda x: x.to_html(),self.children)))}</{self.tag}>"
        return htmltag

    
    def __eq__(self,node):
        if self.tag != node.tag:
            return False
        if self.children != node.children:
            return False
        if self.props != node.props:
            return False
        return True


    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.children},{self.props})"








