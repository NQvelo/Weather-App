# Building the Weather Forecast App

Package the app as a standalone executable using PyInstaller:

- **Windows** → `WeatherForecastApp.exe`
- **macOS** → `WeatherForecastApp.app`

---

## macOS

### Requirements

- macOS with Python 3.8+
- Xcode Command Line Tools: `xcode-select --install` (if needed)

### Quick build

1. **Terminal** in the project folder:

2. Optional – use a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Run the build script:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

4. The app will be at:
   ```
   dist/WeatherForecastApp.app
   ```

5. Run it: double‑click the `.app` or:
   ```bash
   open dist/WeatherForecastApp.app
   ```

### Manual build

```bash
pip install -r requirements-build.txt
pyinstaller --noconfirm weather_app.spec
```

---

## Windows

### Requirements

- Windows with Python 3.8+

### Quick build

1. **Command Prompt** or **PowerShell** in the project folder.

2. Optional – virtual environment:
   ```bat
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Run:
   ```bat
   build.bat
   ```

4. The executable will be at:
   ```
   dist\WeatherForecastApp.exe
   ```

### Manual build

```bat
pip install -r requirements-build.txt
pyinstaller --noconfirm weather_app.spec
```

---

## Shared notes

- **One spec for both:** `weather_app.spec` is used on Windows and macOS. PyInstaller produces an `.exe` on Windows and a `.app` on macOS.
- **No console:** `console=False` in the spec hides the terminal.
- **Internet:** The app needs network access to load weather data.
- **First run:** The first launch can be slower while the app unpacks.

### macOS: “App can’t be opened”

If macOS blocks the app as from an “unidentified developer”:

1. **Right‑click** the `.app` → **Open** → **Open**, or  
2. **System Settings** → **Privacy & Security** → allow the app.

### Windows: antivirus

Some antivirus software may flag new PyInstaller executables. If you trust the build, add an exception.

### Custom icon (optional)

- **macOS:** use a `.icns` file.  
- **Windows:** use a `.ico` file.

Add to the `EXE(...)` block in `weather_app.spec`:

```python
icon='path/to/icon.icns',   # macOS
# or
icon='path/to/icon.ico',    # Windows
```

(Use the one that matches the OS you’re building on.)
