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
                'markdown',
                # 'markdown-auto_identifiers',
                md_name,
                '--filter',
                'pandoc-xnos',
                '-o',
                tex_name])
            
            print(f"Making minor edits to {tex_name}...")
            with open(tex_name, 'r') as f:
                filestring = f.read()
                filestring = filestring.replace(
                    r"\includegraphics",
                    r"\includegraphics[width=0.75\textwidth]"
                )
                filestring = filestring.replace(
                    "../media/",
                    "./"
                )
            
            with open(tex_name, 'w') as f:
                f.write(filestring)
                
    break
    
#input("press ENTER to end...")