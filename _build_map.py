import re

with open(r"C:\Users\13080\markitdown-gui-zh\markitdowngui\utils\translations.py", "r", encoding="utf-8") as f:
    content = f.read()

# Find the en dict
match = re.search(r'"en":\s*\{', content)
start = match.start()
depth = 0
end = start
for i in range(start, len(content)):
    if content[i] == "{":
        depth += 1
    elif content[i] == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break

en_section = content[start:end]
pairs = re.findall(r'"([^"]+)":\s*"([^"]*)"', en_section)

en_to_key = {}
for key, value in pairs:
    if value and len(value) > 2:
        en_to_key[value] = key

sorted_pairs = sorted(en_to_key.items(), key=lambda x: -len(x[0]))

print(f"Total mappable pairs: {len(sorted_pairs)}")
for val, key in sorted_pairs[:30]:
    print(f"  [{key}] = {repr(val[:80])}")
