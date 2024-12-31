from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        if delimeter in text:
            node.text = text[:text.index(delimeter)]
            extracted_first_part = text[text.index(delimeter)+len(delimeter):]
            if delimeter in extracted_first_part:
                extracted_second_part = extracted_first_part[:extracted_first_part.index(delimeter)]
                if len(node.text) != 0:
                    new_nodes.append(node)
                new_nodes.append(TextNode(extracted_second_part,text_type))
                last_part = extracted_first_part.replace(extracted_second_part+delimeter, "")
                if len(last_part) != 0:
                    recurse = TextNode(last_part, node.text_type)
                    new_nodes.extend(split_nodes_delimiter([recurse], delimeter, text_type))
            else:
                raise Exception("Invalid markdown syntax: missing closing delimeter")

        else:
            new_nodes.append(TextNode(text, node.text_type))

    return new_nodes



