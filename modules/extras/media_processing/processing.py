from PIL import Image, ImageDraw, ImageFont
import subprocess
import os

def resize_image(input_path: str, output_path: str, size=(800, 600)):
    img = Image.open(input_path)
    img.thumbnail(size)
    img.save(output_path)
    return output_path

def add_watermark(input_path: str, output_path: str, text="© MyBot"):
    img = Image.open(input_path).convert("RGBA")
    txt = Image.new("RGBA", img.size)
    font = ImageFont.load_default()
    d = ImageDraw.Draw(txt)
    d.text((10, 10), text, font=font, fill=(255,255,255,128))
    watermarked = Image.alpha_composite(img, txt)
    watermarked.convert("RGB").save(output_path)
    return output_path

def convert_video(input_path: str, output_path: str, codec="libx264"):
    cmd = [
        "ffmpeg", "-i", input_path,
        "-vcodec", codec,
        "-acodec", "aac",
        output_path,
        "-y"
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_path
