"""Regenerate all favicon / app-icon assets from logo-round.png.
Run: python scripts/make_favicons.py
Pure-PIL, no external services. Keeps the new brand mark consistent across
search favicons, browser tabs, iOS home screen, and PWA manifest icons.
"""
import base64
import io
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "logo-round.png")
WHITE = (255, 255, 255, 255)


def load_src():
    return Image.open(SRC).convert("RGBA")


def resize(img, size):
    return img.resize((size, size), Image.LANCZOS)


def on_background(img, size, bg, scale=1.0):
    """Composite the (transparent) logo centered on a solid background.
    scale<1 leaves padding — used for maskable PWA icons' safe zone."""
    canvas = Image.new("RGBA", (size, size), bg)
    inner = int(size * scale)
    logo = resize(img, inner)
    off = (size - inner) // 2
    canvas.alpha_composite(logo, (off, off))
    return canvas


def main():
    src = load_src()

    # Browser/search favicons — transparent circle (UAs mask to a circle anyway)
    resize(src, 96).save(os.path.join(ROOT, "favicon-96x96.png"))

    # Multi-resolution .ico
    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    resize(src, 48).save(os.path.join(ROOT, "favicon.ico"), sizes=ico_sizes)

    # iOS home screen — must be opaque (transparency renders black on iOS)
    on_background(src, 180, WHITE).convert("RGB").save(
        os.path.join(ROOT, "apple-touch-icon.png")
    )

    # PWA maskable icons — opaque bg, logo within ~80% safe zone
    on_background(src, 192, WHITE, scale=0.82).convert("RGB").save(
        os.path.join(ROOT, "web-app-manifest-192x192.png")
    )
    on_background(src, 512, WHITE, scale=0.82).convert("RGB").save(
        os.path.join(ROOT, "web-app-manifest-512x512.png")
    )

    # SVG favicon — wrap a crisp PNG of the new mark as base64
    buf = io.BytesIO()
    resize(src, 256).save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" '
        'width="256" height="256" viewBox="0 0 256 256">'
        f'<image width="256" height="256" xlink:href="data:image/png;base64,{b64}"/>'
        "</svg>"
    )
    with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

    print("Regenerated: favicon-96x96.png, favicon.ico, favicon.svg, "
          "apple-touch-icon.png, web-app-manifest-192x192.png, "
          "web-app-manifest-512x512.png")


if __name__ == "__main__":
    main()
