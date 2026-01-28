@echo off
REM Build Weather Forecast App as Windows .exe
REM Run this on Windows, from the project root.

echo Installing build dependencies...
pip install -r requirements-build.txt

echo.
echo Building exe...
pyinstaller --noconfirm weather_app.spec

echo.
if exist "dist\WeatherForecastApp.exe" (
    echo Done. Exe: dist\WeatherForecastApp.exe
) else (
    echo Build may have failed. Check output above.
)
