from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"


class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,node):
        if self.text != node.text:
            return False
        if self.text_type != node.text_type:
            return False
        if self.url != node.url:
            return False
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html(textnode):
    if textnode.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", textnode.text)
    if textnode.text_type == TextType.NORMAL_TEXT:
        return LeafNode(None, textnode.text)
    if textnode.text_type == TextType.CODE_TEXT:
        return LeafNode("code", textnode.text)
    if textnode.text_type == TextType.LINK_TEXT:
        return LeafNode("a", textnode.text, {'href':textnode.url})
    if textnode.text_type == TextType.IMAGE_TEXT:
        return LeafNode("img", "",{'src':textnode.url,'alt':textnode.text})
    if textnode.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", textnode.text)
    raise Exception("Invalid text node")
