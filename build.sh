#!/bin/bash
# Build Weather Forecast App for macOS (.app)
# Run from the project root on macOS.

set -e

echo "Installing build dependencies..."
pip install -q -r requirements-build.txt

echo ""
echo "Building app..."
pyinstaller --noconfirm weather_app.spec

echo ""
if [ -d "dist/WeatherForecastApp.app" ]; then
    echo "Done. App: dist/WeatherForecastApp.app"
    echo "Double-click the .app to run, or: open dist/WeatherForecastApp.app"
elif [ -f "dist/WeatherForecastApp" ]; then
    echo "Done. Executable: dist/WeatherForecastApp"
else
    echo "Build may have failed. Check output above."
    exit 1
fi
