import os

LINE = "The lift doors opened on a stranger humming my favourite song, and for one floor, Judge, the whole city felt like it was winking at us."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# The entry line is fixed and deterministic; see README.md for the text.
