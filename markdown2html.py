#!/usr/bin/python3
"""
Module to convert Markdown to HTML
"""
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    
    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(md_file, 'r') as f:
        md_content = f.read()
    
    html_content = md_content  # for now, we're just copying the content
    
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
