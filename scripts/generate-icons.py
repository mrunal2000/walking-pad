#!/usr/bin/env python3
"""Generate PWA icons (192 and 512) without external deps."""
import struct
import zlib
from pathlib import Path


def write_png(path: Path, size: int) -> None:
    def pixel(x: int, y: int) -> tuple[int, int, int]:
        cx, cy = size / 2, size / 2
        nx = (x - cx) / size
        ny = (y - cy) / size

        # White background
        r, g, b = 255, 255, 255

        # Vertical pad body
        if abs(nx) < 0.2 and abs(ny) < 0.36:
            r, g, b = 20, 22, 25
            # Tread slats
            if int((y - cy + size * 0.36) / (size * 0.05)) % 2 == 0:
                r, g, b = 32, 35, 42
        elif abs(nx) < 0.22 and abs(ny) < 0.38:
            r, g, b = 45, 48, 55

        # Lit display on top of pad
        if abs(nx) < 0.1 and -0.34 < ny < -0.28:
            r, g, b = 6, 16, 24
            if abs(nx) < 0.06 and -0.33 < ny < -0.29:
                r, g, b = 94, 232, 240

        return r, g, b

    rows = []
    for y in range(size):
        row = b"\x00"
        for x in range(size):
            r, g, b = pixel(x, y)
            row += bytes((r, g, b))
        rows.append(row)

    raw = b"".join(rows)
    compressed = zlib.compress(raw, 9)

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", compressed)
        + chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    icons = root / "icons"
    icons.mkdir(exist_ok=True)
    write_png(icons / "icon-192.png", 192)
    write_png(icons / "icon-512.png", 512)
    print("Wrote icons/icon-192.png and icons/icon-512.png")


if __name__ == "__main__":
    main()
