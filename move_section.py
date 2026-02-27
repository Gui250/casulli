import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find "id="sobre"" section boundaries
sobre_start = -1
sobre_end = -1
for i, line in enumerate(lines):
    if '<!-- SOBRE -->' in line:
        sobre_start = i
    if sobre_start != -1 and '</section>' in line and i > sobre_start:
        sobre_end = i
        break

sobre_section = lines[sobre_start:sobre_end+1]
# delete it from original
del lines[sobre_start:sobre_end+1]

# manipulate inside sobre_section
for i, line in enumerate(sobre_section):
    if 'class="sobre-butterfly-big"' in line:
        sobre_section[i] = "" 
    if 'class="sobre-img-frame"' in line:
        sobre_section[i] = line.replace('class="sobre-img-frame"', 'class="sobre-img-frame" style="background-image: url(\'casulli/lizandra/FOTO4145.jpg.jpeg\'); background-size: cover; background-position: center;"')

# find "id="diferenciais"" section boundaries
dif_end = -1
for i, line in enumerate(lines):
    if 'id="diferenciais"' in line:
        for j in range(i, len(lines)):
            if '</section>' in lines[j]:
                dif_end = j
                break
        if dif_end != -1:
            break

# insert sobre_section after dif_end
# also add an extra newline for neatness
lines.insert(dif_end + 1, '\n')
for line in reversed(sobre_section):
    lines.insert(dif_end + 2, line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Section moved successfully!")
