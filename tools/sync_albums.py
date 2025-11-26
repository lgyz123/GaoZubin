# tools/sync_albums.py
import os
import shutil

# 源目录：content/albums
SRC_DIR = os.path.join("content", "albums")
# 目标目录：static/uploads/albums
DST_DIR = os.path.join("static", "uploads", "albums")

# 支持的图片后缀
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

os.makedirs(DST_DIR, exist_ok=True)

for name in os.listdir(SRC_DIR):
    src_path = os.path.join(SRC_DIR, name)
    if not os.path.isfile(src_path):
        continue

    _, ext = os.path.splitext(name)
    if ext.lower() not in IMAGE_EXTS:
        continue

    dst_path = os.path.join(DST_DIR, name)
    print(f"Copy {src_path} -> {dst_path}")
    shutil.copy2(src_path, dst_path)
