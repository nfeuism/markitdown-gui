import re

# Read translations and build English→key mapping
with open(r"C:\Users\13080\markitdown-gui-zh\markitdowngui\utils\translations.py", "r", encoding="utf-8") as f:
    content = f.read()

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

# Sort by value length descending
sorted_pairs = sorted(en_to_key.items(), key=lambda x: -len(x[0]))

# Read QML
with open(r"C:\Users\13080\markitdown-gui-zh\markitdowngui\qml\Main.qml", "r", encoding="utf-8") as f:
    qml = f.read()

replacements = 0
for eng_text, key in sorted_pairs:
    # Escape special regex chars in the English text
    escaped = re.escape(eng_text)
    # Replace \\n (literal backslash-n in Python string) with actual newlines for matching
    # The translation file stores \n as \\n, but QML may have literal \n
    # We need to handle both: literal \\n in Python string becomes \n in actual text
    if '\\\\n' in eng_text:
        # The English text has escaped newlines — the QML might have actual newlines
        # Skip multiline strings for now, they're complex
        continue
    
    # Try to find the English text as a double-quoted string in QML
    # Pattern: "<eng_text>" where eng_text doesn't contain "
    if '"' in eng_text:
        continue  # Skip strings with quotes
    
    pattern = f'"({re.escape(eng_text)})"'
    new_text = f'app.t("{key}")'
    
    # Only replace if it matches exactly and the pattern exists
    match_count = len(re.findall(pattern, qml))
    if match_count > 0:
        qml = re.sub(pattern, new_text, qml)
        replacements += match_count
        if replacements <= 20:
            print(f"  [{key}] → {match_count} occurrence(s)")

print(f"\nTotal replacements: {replacements}")

# Write back
with open(r"C:\Users\13080\markitdown-gui-zh\markitdowngui\qml\Main.qml", "w", encoding="utf-8") as f:
    f.write(qml)

print("QML updated.")
