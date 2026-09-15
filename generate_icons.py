from PIL import Image, ImageDraw

def create_icon(size, radius_ratio=0.168):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    r = int(size * radius_ratio)
    bg_color = (79, 70, 229, 255)  # #4f46e5
    white = (255, 255, 255, 255)

    # 圆角背景
    draw.rounded_rectangle((0, 0, size, size), radius=r, fill=bg_color)

    # 中心白色圆形
    cx, cy = size // 2, size // 2
    circle_r = int(size * 0.32)
    draw.ellipse((cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r), fill=white)

    # 绘制 ¥ 符号（紫色）
    y_color = bg_color
    line_w = max(2, int(size * 0.035))

    y_top = int(cy - size * 0.16)
    y_mid = int(cy - size * 0.02)
    y_bottom = int(cy + size * 0.18)
    x_offset = int(size * 0.10)

    # 左斜线
    draw.line([(cx - x_offset, y_top), (cx, y_mid)], fill=y_color, width=line_w)
    # 右斜线
    draw.line([(cx + x_offset, y_top), (cx, y_mid)], fill=y_color, width=line_w)
    # 中间横线
    h_line_y = int(cy + size * 0.02)
    h_line_half = int(size * 0.10)
    draw.line([(cx - h_line_half, h_line_y), (cx + h_line_half, h_line_y)], fill=y_color, width=line_w)
    # 底部竖线
    draw.line([(cx, y_mid), (cx, y_bottom)], fill=y_color, width=line_w)

    return img

create_icon(512).save('icon512.png')
create_icon(192).save('icon192.png')
print('Icons created')
