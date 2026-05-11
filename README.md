# Paint
i made paint in arch linux using python

# ArchPaint 🎨

ArchPaint is a simple Paint application written in Python for Arch Linux.

Features:
- Brush
- Eraser
- Graffiti spray tool
- Line / Rectangle / Oval tools
- Shape preview like Windows Paint
- Brush size preview
- Image importing
- PNG saving
- Smooth drawing

---

# 🐧 Arch Linux Setup

## Install dependencies

Arch Linux blocks some global pip installs (PEP 668), so DO NOT use:

```bash
pip install pillow
```

Use pacman instead:

```bash
sudo pacman -S python python-pillow tk
```

---

# 📂 File Structure

Example:

```text
/home/arch/python/ArchPaint.py
```

---

# ▶ Running ArchPaint

Open terminal:

```bash
cd ~/python
python ArchPaint.py
```

---

# ❌ Common Errors

## ModuleNotFoundError: No module named 'PIL'

### Error
```python
ModuleNotFoundError: No module named 'PIL'
```

### Cause
Pillow is not installed.

### Fix
```bash
sudo pacman -S python-pillow
```

---

# ❌ pip install pillow gives externally-managed-environment

### Error
```bash
error: externally-managed-environment
```

### Cause
Arch Linux protects system Python packages.

### Correct Fix
Use pacman instead:

```bash
sudo pacman -S python-pillow
```

---

# 🖥 Add ArchPaint to KDE Application Launcher

Create desktop entry:

```bash
nano ~/.local/share/applications/archpaint.desktop
```

Paste this:

```ini
[Desktop Entry]
Version=1.0
Name=ArchPaint
Comment=Python Paint App
Exec=python /home/arch/python/ArchPaint.py
Path=/home/arch/python
Icon=accessories-text-editor
Terminal=false
Type=Application
Categories=Graphics;
```

Save file:
- CTRL + O
- ENTER
- CTRL + X

Make executable:

```bash
chmod +x ~/.local/share/applications/archpaint.desktop
```

Refresh KDE launcher:

```bash
kbuildsycoca6
```

Now open KDE launcher and search:

```text
ArchPaint
```

---

# 💾 How to Save in Nano

Save:
```text
CTRL + O
ENTER
```

Exit:
```text
CTRL + X
```

---

# 🎨 Tools

## Brush
Normal smooth drawing tool.

## Eraser
Draws with white color.

## Graffiti
Random spray-paint effect using randomized pixels.

## Line
Straight line tool with preview.

## Rect
Rectangle tool with dashed preview.

## Oval
Ellipse / circle tool with dashed preview.

---

# 👁 Shape Preview

ArchPaint includes:
- Brush size preview
- Shape preview
- Dashed outlines like classic Windows Paint

---

# 📥 Import Images

Supported:
- PNG
- JPG
- JPEG
- BMP

Use:
```text
Import
```

---

# 💾 Save Images

Supported output:
- PNG

Use:
```text
Save
```

---

# 🚀 Future Ideas

Possible upgrades:
- Undo / Redo
- Fill Bucket
- Layers
- Zoom Tool
- Blur Brush
- Selection Tool
- Photoshop-like smoothing

---

# 🔥 Full Install Example

```bash
sudo pacman -S python python-pillow tk

cd ~/python

python ArchPaint.py
```

---

# 📜 License

Free to modify and use.
