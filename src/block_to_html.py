from htmlnode import ParentNode, HTMLNode
from split_blocks import markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html

def markdown_to_html_node(markdown):
    list_of_blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in list_of_blocks:
        type_of_block = block_to_block_type(block)
        if "heading" in type_of_block:
            #TextNode(f"h{type_of_block[-1]}", f"{block[type_of_block[-1]+1:]}", )
            textnodes = text_to_textnodes(block[int(type_of_block[-1])+1:])
            leafnodes = list(map(text_node_to_html, textnodes))
            htmlnodes.append(ParentNode(f"h{type_of_block[-1]}", leafnodes))

        if "paragraph" == type_of_block:
            texnodes = text_to_textnodes(block.replace("\n", " "))
            leafnodes = list(map(text_node_to_html, texnodes))
            htmlnodes.append(ParentNode("p", leafnodes))

        if "code" == type_of_block:
            textnodes = text_to_textnodes(block[2:-2])
            leafnodes = list(map(text_node_to_html, textnodes))
            htmlnodes.append(ParentNode("pre", leafnodes))

        if "quote" == type_of_block:
            block_list = block.split("\n")
            leafnodes = []
            for block in block_list:
                textnodes = text_to_textnodes(block[1:])
                for node in textnodes:
                    leafnodes.append(text_node_to_html(node))
            htmlnodes.append(ParentNode("blockquote", leafnodes))

        if "unordered_list" == type_of_block:
            block_list = block.split("\n")
            pnodes = []
            for block in block_list:
                textnodes = text_to_textnodes(block[2:])
                leafnodes = list(map(text_node_to_html, textnodes))
                pnodes.append(ParentNode("li", leafnodes))
            htmlnodes.append(ParentNode("ul", pnodes))

        if "ordered_list" == type_of_block:
            block_list = block.split("\n")
            pnodes = []
            for block in block_list:
                textnodes = text_to_textnodes(block[3:])
                leafnodes = list(map(text_node_to_html, textnodes))
                pnodes.append(ParentNode("li", leafnodes))
            htmlnodes.append(ParentNode("ol", pnodes))

    top_node = ParentNode("div", htmlnodes) 
    #tophtmltag = top_node.to_html()

    return top_node
            






            





