#!/usr/bin/env python3
import os
import fire

def generate_index(title="overview page"):
    """
    Scans the current folder for HTML files (except index.html) and creates an index.html
    linking to each file. The page title and header are set by the `title` parameter.
    """
    # Get a list of HTML files in the current directory, excluding the generated index.html
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != "index.html"]
    html_files.sort()

    # Build the HTML content
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <ul>
"""
    for file in html_files:
        # Use the filename (without extension) as the link text
        display_name = os.path.splitext(file)[0]
        html_content += f'        <li><a href="{file}">{display_name}</a></li>\n'

    html_content += """    </ul>
</body>
</html>
"""

    # Write (or overwrite) index.html
    with open("index.html", "w") as f:
        f.write(html_content)
    print("index.html generated successfully.")

if __name__ == "__main__":
    fire.Fire(generate_index)
