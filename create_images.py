#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Define images with appropriate colors for a grocery market
images_config = [
    ('hero-01.jpg', (1920, 1080), '#c62828', 'Hilltop Market Storefront'),
    ('hero-02.jpg', (1920, 1080), '#1565c0', 'Hilltop Market Exterior'),
    ('hero-03.jpg', (1920, 1080), '#2e7d32', 'Hilltop Market Location'),
    ('store-01.jpg', (1920, 1080), '#6a1b9a', 'Inside Hilltop Market'),
    ('meat-01.jpg', (1920, 1080), '#b71c1c', 'Fresh Meat Selection'),
    ('meat-02.jpg', (1920, 1080), '#e65100', 'Tortillas & Specialty'),
    ('produce-01.jpg', (1920, 1080), '#388e3c', 'Fresh Produce'),
    ('aisle-01.jpg', (1920, 1080), '#0277bd', 'Market Aisle'),
    ('liquor-01.jpg', (1920, 1080), '#4a148c', 'Wine & Spirits'),
    ('gas-01.jpg', (1920, 1080), '#01579b', 'Exxon Mobil'),
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

for filename, size, color, text in images_config:
    # Create image with solid color
    img = Image.new('RGB', size, hex_to_rgb(color))
    draw = ImageDraw.Draw(img)
    
    # Try to add text (will use default font if custom font not available)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position for center
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)
    
    # Draw semi-transparent overlay
    overlay = Image.new('RGBA', size, (0, 0, 0, 128))
    img_rgba = img.convert('RGBA')
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert('RGB')
    
    draw = ImageDraw.Draw(img)
    draw.text(position, text, fill='white', font=font)
    
    # Save as JPEG
    img.save(f'images/{filename}', 'JPEG', quality=85)
    print(f'Created: images/{filename}')

print('All images created successfully!')
