import re
import sys
import os

def markdown_to_html(markdown):
    # Headers
    markdown = re.sub(r'^#\s(.*?)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s(.*?)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s(.*?)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)

    # Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)

    # Italic
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)

    # Numbered list
    markdown = re.sub(r'^\d+\.\s(.*?)$', r'<li>\1</li>', markdown, flags=re.MULTILINE)
    if re.search(r'^\d+\.\s(.*?)$', markdown, flags=re.MULTILINE):
        markdown = '<ol>\n' + markdown + '</ol>'

    # Link
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    # Image
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

    return markdown

def is_file(path):
    return os.path.isfile(path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 markdown_converter.py <\"MarkdownText\"/MarkdownFile.md>")
        sys.exit(1)
        
    if is_file(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            markdown_text = f.read()
    
        html_text = markdown_to_html(markdown_text)

        input_file_name = os.path.splitext(sys.argv[1])[0]

        output_file_name = "exemplOutput.html"

        with open(output_file_name, 'w') as f:
            f.write(html_text)
        print(f"Arquivo HTML criado com sucesso: {output_file_name}")
    else:
        output = markdown_to_html(sys.argv[1])
        print(output)

if __name__ == "__main__":
    main()
