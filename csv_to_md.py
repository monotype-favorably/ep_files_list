import csv

def escape_markdown(text):
    return str(text).replace("|", r"\|")

with open("files.csv", newline="", encoding="utf-8") as csvfile:
    reader = list(csv.reader(csvfile))

if not reader:
    print("files.csv is empty.")
    exit()

headers = reader[0]
rows = reader[1:]

with open("files.md", "w", encoding="utf-8") as md:
    # Header
    md.write("| " + " | ".join(escape_markdown(h) for h in headers) + " |\n")
    md.write("| " + " | ".join("---" for _ in headers) + " |\n")

    # Rows
    for row in rows:
        md.write("| " + " | ".join(escape_markdown(cell) for cell in row) + " |\n")

print("Created files.md")
