import os
from node_funcs import extract_title
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for filename in os.listdir(dir_path_content):
        filename_split = filename.split(".")
        extension = filename_split[-1]
        file = filename_split[0]
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isfile(from_path):
            if extension != "md":
                continue
            dest_path = os.path.join(dest_dir_path, file + ".html")
            print(f" * {from_path} -> {dest_path}")
            generate_page(from_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, filename)
            print(f" * {from_path} -> {dest_path}")
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)