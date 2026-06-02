# Walking Pad

Mobile web app — walk on a 3D treadmill pad using touch.

## Run locally

```bash
python3 -m http.server 5173
```

Open `http://localhost:5173` on your phone (same Wi‑Fi: use your computer’s IP).

> Install requires **HTTPS** or **localhost**. Use localhost on your phone via your machine’s LAN IP only after the server is running.

## Add to home screen

### iPhone (Safari)

1. Open the app URL in Safari.
2. Tap **Share** → **Add to Home Screen**.
3. Tap **Add**.

### Android (Chrome)

1. Open the app URL in Chrome.
2. Tap the menu (⋮) → **Install app** or **Add to Home screen**.

The app opens full-screen without the browser bar (`standalone` mode).

## PWA files

| File | Purpose |
|------|---------|
| `manifest.webmanifest` | App name, icon, theme, standalone display |
| `sw.js` | Offline cache for the app shell and Three.js |
| `icons/` | Home screen icons (192×192, 512×512) |

Regenerate icons: `python3 scripts/generate-icons.py`
