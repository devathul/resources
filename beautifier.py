'''
keeps my programming resources markdown neat

references:
https://meta.stackexchange.com/questions/189749/
'''

import re
from sys import argv


def md_link(desc, url):
   return "[" + desc + "](" + url.replace("_", "\_") + ")"
    

input_filename = argv[1] if len(argv) > 1 else "programming-resources.md"
output_filename = argv[2] if len(argv) > 2 else input_filename.split(".")[0] + "-pretty.md"

with open(input_filename) as f:
    text = [x.rstrip() for x in f.readlines()]
    
result = []
toc = []

for line in text:
    m = re.compile("^## (.+)$").search(line)

    if m:
        link = "#" + m.group(1).lower().replace(" ", "-")
        toc.append("{0}. [{1}]({2})".format(len(toc), m.group(1), link))
        result.append(line)
    else:    
        m = re.compile("^( *\+ +)([^:]+): *(https?://[^ ]+)(.*)$").search(line)
        
        if m: 
            result.append(m.group(1) + md_link(m.group(2), m.group(3)))

            if m.group(4):
                result[-1] += " " + m.group(4)
        else:
            m = re.compile("^( *\+ +) *(https?://[^ ]+)(.*)$").search(line)
        
            if m:
                result.append(m.group(1) + md_link(m.group(2), m.group(2)))

                if m.group(3):
                    result[-1] += " " + m.group(3)
            else:
                result.append(line)

with open(output_filename, "w") as f:
    [f.write(x + "\n") for x in result[:4]]
    [f.write(x + "\n") for x in toc[1:]]
    [f.write(x + "\n") for x in result[4:]]