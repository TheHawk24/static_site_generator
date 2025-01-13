from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        if delimeter in text:
            node.text = text[:text.index(delimeter)]
            if len(node.text) != 0:
                new_nodes.append(node)
            extracted_first_part = text[text.index(delimeter)+len(delimeter):] # Remove the opening delimiter
            if delimeter in extracted_first_part: # if second delimiter is found slice up to the second delimiter
                extracted_second_part = extracted_first_part[:extracted_first_part.index(delimeter)]
                new_nodes.append(TextNode(extracted_second_part,text_type))
                last_part = extracted_first_part.replace(extracted_second_part+delimeter, "", 1)
                if len(last_part) != 0:
                    recurse = TextNode(last_part, node.text_type)
                    new_nodes.extend(split_nodes_delimiter([recurse], delimeter, text_type))
            else:
                raise Exception("Invalid markdown syntax: missing closing delimeter")

        else:
            new_nodes.append(TextNode(text, node.text_type))

    return new_nodes



def extract_markdown_images(text):
    alt_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_text 

def extract_markdown_links(text):
    url = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return url

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_images(node.text)
        if len(extracted_links) != 0:
            for link in extracted_links:
                node.text = node.text.replace(f"[{link[0]}]({link[1]})", "[]()", 1)
        else:
            if len(node.text) != 0:
                new_nodes.append(node)
                continue
            else:
                continue
        text = node.text
        delimiter = "![]()"
        first_part = text[:text.index(delimiter)]
        if len(first_part) == 0:
            new_nodes.append(TextNode(extracted_links[0][0], TextType.IMAGE_TEXT, extracted_links[0][1]))
            recurse_node = replace_recurse(text, delimiter, extracted_links, True, False)
            new_nodes.extend(split_nodes_image([recurse_node]))
        else:
            new_nodes.append(TextNode(first_part, TextType.NORMAL_TEXT))
            new_nodes.append(TextNode(extracted_links[0][0], TextType.IMAGE_TEXT, extracted_links[0][1]))
            recurse_node = replace_recurse(text, delimiter, extracted_links, True, False) 
            new_nodes.extend(split_nodes_image([recurse_node]))

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)
        if len(extracted_links) != 0:
            for link in extracted_links:
                node.text = node.text.replace(f"[{link[0]}]({link[1]})", "[]()", 1)
        else:
            if len(node.text) != 0:
                new_nodes.append(node)
                continue
            else:
                continue
        text = node.text
        delimiter = "[]()"
        first_part = text[:text.index(delimiter)]
        if len(first_part) == 0:
            new_nodes.append(TextNode(extracted_links[0][0], TextType.LINK_TEXT, extracted_links[0][1]))
            recurse_node = replace_recurse(text, delimiter, extracted_links, False, True)
            new_nodes.extend(split_nodes_links([recurse_node]))
        else:
            new_nodes.append(TextNode(first_part, TextType.NORMAL_TEXT))
            new_nodes.append(TextNode(extracted_links[0][0], TextType.LINK_TEXT, extracted_links[0][1]))
            recurse_node = replace_recurse(text, delimiter, extracted_links, False, True) 
            new_nodes.extend(split_nodes_links([recurse_node]))

    return new_nodes

def replace_recurse(text, delimiter, extracted_links, image, links):
    split_text = text[text.index(delimiter)+len(delimiter):]
    cut_links = extracted_links[1:]
    if image:
        for link in cut_links:
            split_text = split_text.replace(delimiter, f"![{link[0]}]({link[1]})", 1)
    if links:
        for link in cut_links:
            split_text = split_text.replace(delimiter, f"[{link[0]}]({link[1]})", 1)
    text = split_text
    recurse_node = TextNode(text, TextType.NORMAL_TEXT)
    return recurse_node

