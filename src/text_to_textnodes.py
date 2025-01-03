from textnode import TextType, TextNode
from split_nodes import split_nodes_image, split_nodes_links, split_nodes_delimiter


def text_to_textnodes(text):
    node = TextNode(text, TextType.NORMAL_TEXT)
    bold_text = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
    italic_text = split_nodes_delimiter(bold_text, "*", TextType.ITALIC_TEXT)
    code_block = split_nodes_delimiter(italic_text,"`", TextType.CODE_TEXT)
    image_links = split_nodes_image(code_block)
    link_text = split_nodes_links(image_links)
    return link_text

