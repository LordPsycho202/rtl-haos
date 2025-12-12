# Changelog

## v1.0.13
- **NEW:** Added `BRIDGE_ID` configuration to keep the Device ID static across reboots.
- **NEW:** Added `BRIDGE_NAME` to allow custom friendly names (ignoring the Docker hostname).
- **FIX:** Fixed issue where Home Assistant created duplicate devices after every restart.
- **FIX:** Improved stability of the RTL-SDR auto-detection.

## v1.0.12
- Initial public release.
- Added support for custom MQTT credentials.
- Added System Monitor for CPU/RAM usage.