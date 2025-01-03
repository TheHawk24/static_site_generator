
def markdown_to_blocks(markdown):
    markdown_strs = markdown.split("\n\n")
    stripped_markdown = list(filter(lambda x: not len(x) == 0,map(lambda x: x.strip(),markdown_strs)))
    return stripped_markdown


def block_to_block_type(markdown_block):

    if markdown_block[0] == "#":
        for i in range(1,7):
            if markdown_block[i] == "#":
                continue
            elif markdown_block[i] == " ":
                return "heading"
            else:
                break
    
    if markdown_block[:3] == "```" and markdown_block[-3:] == "```":
        return "code"

    if markdown_block[0] == ">":
        quote_lines = markdown_block.split("\n")
        true = True
        for line in quote_lines:
            if not line[0] == ">":
                true = False
                break
        if true:
            return "quote"

    if markdown_block[:2] == "* " or markdown_block[:2] == "- ":
        ulist = markdown_block.split("\n")
        true = True
        for line in ulist:
            if not (line[:2] == "* " or line[:2] == "- "):
                true = False 
                break
        if true:
            return "unordered_list"

    if markdown_block[:3] == "1. ":
        olist = markdown_block.split("\n")
        true = True
        for i in range(1,len(olist)):
            if not (f"{i+1}. " == olist[i][:3]):
                true = False
                break
        if true:
            return "ordered_list"

    return "paragraph"


