from io import BytesIO

from PIL import Image
import pillow_avif  # noqa: F401


image = Image.new("RGB", (4, 4), (16, 64, 128))
buffer = BytesIO()
image.save(buffer, format="AVIF", lossless=True)
buffer.seek(0)

decoded = Image.open(buffer)
decoded.load()

assert decoded.format == "AVIF"
assert decoded.size == image.size

pixel = decoded.convert("RGB").getpixel((0, 0))
for actual, expected in zip(pixel, (16, 64, 128)):
    assert abs(actual - expected) <= 4, (pixel, expected)
