"""
file: convert_to_tex.py
author: Mark Redd
about:
    Converts select markdown files in the current folder to latex files in an
    already-existing folder called 'tex'. Does not search sub folders.
"""
import subprocess
import os

# here = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk('./content'):
    for filename in files:
        if filename.endswith(".md") and int(filename[:2]) > 9:
            md_name = f"{root}/{filename}"
            tex_name = f"{root}/../tex/section{filename[:2]}.tex"
            print(f'generating: {tex_name}...')
            subprocess.call([
                'pandoc', 
                '-r', 
                'markdown-auto_identifiers',
                md_name,
                '-o',
                tex_name])
            
            print(f"Making minor edits to {tex_name}...")
            with open(tex_name, 'r') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                if r"\includegraphics" in line:
                    newline = line.replace(
                        r"\includegraphics",
                        r"\includegraphics[width=0.75\textwidth]")
                    
                    lines[i] = newline
                if "../media" in line:
                    newline = line.replace(
                        "../media",
                        "./media")
                    
                    lines[i] = newline
            
            filestring = ''.join(lines)
            
            with open(tex_name, 'w') as f:
                f.write(filestring)
                
    break
    
#input("press ENTER to end...")