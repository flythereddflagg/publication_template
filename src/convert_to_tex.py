"""
file: convert_to_tex.py
author: Mark Redd
about:
    Converts select markdown files in the current folder to latex files in an
    already-existing folder called 'tex'. Does not search sub folders.
"""
import subprocess
import os
import json

HERE = os.path.dirname(os.path.realpath(__file__))

CONTENT_PATH = '/content'

with open(HERE + "/replace_strings.json") as f:
    REPLACE_STRINGS = json.load(f)


def pdf_exists(line):
    filename = line.split('{')[-1][2:-6] + ".pdf"
    try:
        open(HERE + "/../media/" + filename).close()
        return True
    except FileNotFoundError:
        return False


for root, dirs, files in os.walk("." + CONTENT_PATH):
    for filename in files:
        if filename.endswith(".md") and int(filename[:2]) > 9:
            md_name = f"{root}/{filename}"
            tex_name = f"{root}/../tex/section{filename[:2]}.tex"
            print(f'generating: {tex_name} ...')
            subprocess.call([
                'pandoc', 
                '-r', 
                'markdown',
                # 'markdown-auto_identifiers',
                md_name,
                '--filter',
                'pandoc-xnos',
<<<<<<< HEAD
                # '--filter',
                # 'pandoc-fignos',
                # '--filter',
                # 'pandoc-secnos',
                # '--filter',
                # 'pandoc-tablenos',
=======
>>>>>>> 415733ad9489446dfce2eefae683aa434584c21a
                '-o',
                tex_name])
            
            print(f"Making minor edits to {tex_name} ...")
            with open(tex_name, 'r') as f:
                filestring = f.read()
            
            for str_pair in REPLACE_STRINGS:
                filestring = filestring.replace(*str_pair)
            
            with open(tex_name, 'w') as f:
                f.write(filestring)
            
            with open(tex_name, 'r') as f:
                lines = f.readlines()
            
            for i in range(len(lines)):
                line = lines[i]
                if 'includegraphics' in line and pdf_exists(line):
                    lines[i] = line.replace(".png", ".pdf")
            
            filestring = "".join(lines)
            with open(tex_name, 'w') as f:
                f.write(filestring)
                
    break
    
#input("press ENTER to end...")