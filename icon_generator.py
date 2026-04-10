from PIL import Image, ImageDraw, ImageFont

def create_icon(size, radius):
    # Create mask for rounded corners
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=255)

    # Create the actual image
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)

    # Red stripe at top, 6% height
    stripe_height = int(size * 0.06)
    draw.rectangle([0, 0, size, stripe_height], fill='#E31937')

    # Font
    try:
        font = ImageFont.truetype("NotoSansKR-Bold.ttf", size//8)  # Adjust size
    except:
        font = ImageFont.load_default()

    # Text 1: 전자랜드
    text1 = "전자랜드"
    bbox1 = draw.textbbox((0, 0), text1, font=font)
    text1_width = bbox1[2] - bbox1[0]
    text1_height = bbox1[3] - bbox1[1]
    y1 = size // 2 - text1_height // 2 - 20  # Slightly above center
    x1 = (size - text1_width) // 2
    draw.text((x1, y1), text1, fill='#111111', font=font)

    # Text 2: 물류 VOC
    text2 = "물류 VOC"
    bbox2 = draw.textbbox((0, 0), text2, font=font)
    text2_width = bbox2[2] - bbox2[0]
    text2_height = bbox2[3] - bbox1[1]
    y2 = y1 + text1_height + 10
    x2 = (size - text2_width) // 2
    draw.text((x2, y2), text2, fill='#111111', font=font)

    # Apply mask
    img.putalpha(mask)
    return img

# Create icons
icon192 = create_icon(192, 28)
icon192.save('icon-192.png')

icon512 = create_icon(512, 36)
icon512.save('icon-512.png')

print("Icons created successfully")