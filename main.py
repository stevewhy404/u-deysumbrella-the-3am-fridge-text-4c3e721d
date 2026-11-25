import os

LINE = "3am update: the leftovers have formed a union and the freezer is their lawyer. I am staying neutral. Good luck."

out = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
