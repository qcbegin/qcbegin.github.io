# Trail GPX files

Drop your `.gpx` track files here, then point to them from `build.py`.

## How to add a real route

1. **Export a GPX track** of the hike from wherever you recorded it:
   - **Strava** → activity → "..." menu → *Export GPX*
   - **Garmin Connect** → activity → gear icon → *Export to GPX*
   - **AllTrails** (with recording / Pro) → activity → *Export route* → GPX
   - **Gaia GPS / Komoot / Outdooractive** → export original GPX

2. **Save it here**, e.g. `assets/gpx/yubeng.gpx`

3. **Register it** in `build.py` → `CONTENT["trails"]`:
   ```python
   {"name": "Yubeng Trek", "region": "Yunnan · Meili Snow Mountain",
    "lat": 28.434, "lon": 98.801, "gpx": "assets/gpx/yubeng.gpx"},
   ```

4. **Rebuild**:
   ```
   python build.py
   ```

The pin stays as a label, and the actual walked line is drawn in accent red on top.
Until a `gpx` file is set (`"gpx": None`), only the pin shows — the map still works.

## No GPX, but want a hand-drawn line?

You can create one quickly at <https://www.gpxgenerator.com/> or
<https://gpx.studio/> (click along the trail, then *Download GPX*), and save it here.
