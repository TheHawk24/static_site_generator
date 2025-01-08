import os
from split_blocks import markdown_to_blocks, block_to_block_type
from block_to_html import markdown_to_html_node
from copydir import recurse_dir, create_directories

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if "heading 1" == block_to_block_type(block):
            return block[2:]

    raise Exception("No h1 tag found")



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""
    with open(from_path) as src:
        markdown = src.read()

    with open(template_path) as tmp:
        template = tmp.read()
    
    htmlnode = markdown_to_html_node(markdown)
    html = htmlnode.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    with open(dest_path, 'w') as dst:
        dst.write(template)

    src.close()
    tmp.close()
    dst.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    md_files = recurse_dir(dir_path_content)
    for md in md_files:
        print(md)
        join = "/".join(md.split("/")[2:-1])
        new_destination = os.path.join(dest_dir_path,join)
        print(f"Create directory: {new_destination}")
        created_destination = create_directories(new_destination)
        print(f"Created directory: {created_destination}")
        generate_file_to = created_destination + md.split("/")[-1][:-3] + ".html"
        generate_page(md,template_path,generate_file_to)

