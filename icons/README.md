# Icons

Favicon and app-icon set for any 4th Try Tech site. Copy this folder's files to the site root and add:

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#46607A">
```

| File | What it is |
| --- | --- |
| `favicon.svg` | Small roundel; switches to the dark palette with the browser theme |
| `favicon.ico` | 16, 24, 32 and 48 px in one file, for older browsers |
| `favicon-16.png`, `-24` | From `icon-micro.svg`: sun disc, a wider rocket and a porthole. The roundel does not survive below 32 px |
| `favicon-32.png`, `-48` | From `logo/logo-roundel-small.svg` |
| `apple-touch-icon.png` | 180 px, square and opaque; iOS rounds the corners |
| `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` | Android and PWA icons, listed in `site.webmanifest` |
| `app-icon-light.svg`, `app-icon-dark.svg` | Masters for the square icons. Full-bleed sun and stripes, no ring; the rocket stays inside the central 80% so any mask shape is safe |
| `icon-micro.svg` | Master for 16 and 24 px |

Regenerate with `scripts/build_elements.py`, then `scripts/export_icons.py`.
