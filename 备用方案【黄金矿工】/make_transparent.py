#!/usr/bin/env python3
"""
把猫图的黑色背景、鱼图的白色背景变成透明。
需要先安装 Pillow：pip3 install Pillow 或 python3 -m pip install --user Pillow
运行：python3 make_transparent.py
"""
import os

try:
    from PIL import Image
except ImportError:
    print("请先安装 Pillow：")
    print("  pip3 install Pillow")
    print("或：python3 -m pip install --user Pillow")
    exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)


def black_to_transparent(img):
    """把接近黑色的像素变成透明（用于猫图）"""
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        r, g, b, a = item
        # 很黑的像素（例如 R,G,B 都小于 30）视为背景
        if r < 40 and g < 40 and b < 40:
            new_data.append((r, g, b, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img


def white_to_transparent(img):
    """把接近白色的像素变成透明（用于鱼图）"""
    img = img.convert("RGBA")
    data = img.getdata()
    new_data = []
    for item in data:
        r, g, b, a = item
        # 很白的像素（例如 R,G,B 都大于 240）视为背景，或稍微放宽
        if r > 235 and g > 235 and b > 235:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img


def main():
    cat_path = "cat_miner.png"
    fish_files = ["fish_a.png", "fish_b.png", "fish_c.png", "fish_d.png", "fish_e.png"]

    if os.path.isfile(cat_path):
        im = Image.open(cat_path).convert("RGBA")
        im = black_to_transparent(im)
        im.save(cat_path, "PNG")
        print("已处理（黑→透明）:", cat_path)
    else:
        print("未找到:", cat_path)

    for path in fish_files:
        if os.path.isfile(path):
            im = Image.open(path).convert("RGBA")
            im = white_to_transparent(im)
            im.save(path, "PNG")
            print("已处理（白→透明）:", path)
        else:
            print("未找到:", path)

    print("完成。")


if __name__ == "__main__":
    main()
