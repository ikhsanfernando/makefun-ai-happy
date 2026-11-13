"""Write the prepared image to the path the grader reads."""
import os
import shutil

SRC = "entry.png"
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


# The grader rejects pictures over one mebibyte.
MAX_BYTES = 1048576


def write_entry():
    """Copy the prepared picture to <OUT_DIR>/entry.png and return its path."""
    os.makedirs(OUT_DIR, exist_ok=True)
    dest = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SRC, dest)
    size = os.path.getsize(dest)
    if size == 0:
        raise RuntimeError("entry.png was not written")
    return dest


if __name__ == "__main__":
    write_entry()