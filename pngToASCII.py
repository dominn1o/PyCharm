import os
from PIL import Image

chars = " .:-=+*#%@"

def to_ascii(img, width=80):
    img = img.convert("L")  # grayscale
    aspect = img.height / img.width
    img = img.resize((width, int(width * aspect * 0.5)))
    pixels = list(img.getdata())

    return "\n".join(
        "".join(chars[int(p / 255 * (len(chars) - 1))] for p in pixels[i:i+width])
        for i in range(0, len(pixels), width)
    )


frames_dir = r"C:\Users\dmadyavanhu\Desktop\Visuals\MCHMalrboro\frames"
ascii_dir = r"C:\Users\dmadyavanhu\Desktop\Visuals\MCHMalrboro\ascii"
os.makedirs(ascii_dir, exist_ok=True)

for fname in sorted(os.listdir(frames_dir)):
    if fname.endswith(".png"):
        img = Image.open(os.path.join(frames_dir, fname))
        ascii_art = to_ascii(img, width=80)
        with open(os.path.join(ascii_dir, fname.replace(".png", ".txt")), "w") as f:
            f.write(ascii_art)
