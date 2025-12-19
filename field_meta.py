# field_meta.py
"""
FILE: field_meta.py
"""
# Format: (Unit, Device Class, Icon, Friendly Name)

FIELD_META = {
    # --- System Diagnostics (NEW: Configuration) ---
    # "sys_cfg_blacklist":    ("", "none", "mdi:playlist-remove", "Blacklist"),
    # "sys_cfg_whitelist":    ("", "none", "mdi:playlist-check", "Whitelist"),
    # "sys_cfg_sensors":      ("", "none", "mdi:eye-settings", "Main Sensors"),

    # --- System Diagnostics (Existing) ---
    "sys_device_count":     ("dev", "none", "mdi:counter", "Active Devices","sensor"),
    # "sys_device_list":      ("", "none", "mdi:format-list-bulleted", "Device List"),

    "sys_ip":               ("", "none", "mdi:ip-network", "IP Address","sensor"),
    "sys_os_version":       ("", "none", "mdi:linux", "Linux Kernel","sensor"),
    "sys_model":            ("", "none", "mdi:chip", "Device Model","sensor"),
    "sys_script_mem":       ("MB", "data_size", "mdi:memory", "Script RAM Usage","sensor"),
    "sys_cpu":              ("%", "none", "mdi:cpu-64-bit", "CPU Load","sensor"),
    "sys_mem":              ("%", "none", "mdi:memory", "RAM Usage","sensor"),
    "sys_disk":             ("%", "none", "mdi:harddisk", "Disk Usage","sensor"),
    "sys_temp":             ("°C", "temperature", "mdi:thermometer-lines", "CPU Temp","sensor"),
    "sys_uptime":           ("s", "duration", "mdi:clock-start", "System Uptime","sensor"),

    # --- Magnetometer ---
    "mag_uT":               ("uT", "none", "mdi:magnet", "Mag Field Strength","sensor"),
    "geomag_index":         ("idx", "none", "mdi:waveform", "Mag Disturbance","sensor"),
    "status":               ("", "enum", "mdi:list-status", "Device Status","sensor"),

    # --- Temperature ---
    "temperature":          ("°F", "temperature", "mdi:thermometer", "Temperature","sensor"),
    "temperature_C":        ("°C", "temperature", "mdi:thermometer", "Temperature (C)","sensor"),
    "temperature_F":        ("°F", "temperature", "mdi:thermometer", "Temperature","sensor"),
    "dew_point":            ("°F", "temperature", "mdi:weather-fog", "Dew Point","sensor"),

    # --- Humidity ---
    "humidity":             ("%", "humidity", "mdi:water-percent", "Humidity","sensor"),

    # --- Air Quality ---
    "co2":                  ("ppm", "carbon_dioxide", "mdi:molecule-co2", "CO2 Level","sensor"),

    # --- Pressure ---
    "pressure_hpa":         ("hPa", "pressure", "mdi:gauge", "Pressure","sensor"),
    "pressure_inhg":        ("inHg", "pressure", "mdi:gauge", "Pressure","sensor"),
    "pressure_PSI":         ("psi", "pressure", "mdi:gauge", "Pressure","sensor"),

    # --- Wind ---
    "wind_avg_km_h":        ("km/h", "wind_speed", "mdi:weather-windy", "Wind Speed","sensor"),
    "wind_avg_mi_h":        ("mph", "wind_speed", "mdi:weather-windy", "Wind Speed","sensor"),
    "wind_gust_km_h":       ("km/h", "wind_speed", "mdi:weather-windy-variant", "Wind Gust","sensor"),
    "wind_gust_mi_h":       ("mph", "wind_speed", "mdi:weather-windy-variant", "Wind Gust","sensor"),
    "wind_dir_deg":         ("°", "wind_direction", "mdi:compass", "Wind Direction","sensor"),
    "wind_dir":             ("°", "wind_direction", "mdi:compass", "Wind Direction","sensor"),

    # --- Rain ---
    "rain_mm":              ("mm", "precipitation", "mdi:weather-rainy", "Rain Total","sensor"),
    "rain_in":              ("in", "precipitation", "mdi:weather-rainy", "Rain Total","sensor"),
    "rain_rate_mm_h":       ("mm/h", "precipitation_intensity", "mdi:weather-pouring", "Rain Rate","sensor"),
    "rain_rate_in_h":       ("in/h", "precipitation_intensity", "mdi:weather-pouring", "Rain Rate","sensor"),

    # --- Light ---
    "lux":                  ("lx", "illuminance", "mdi:brightness-5", "Light Level","sensor"),
    "full_lux":             ("cnt", "none", "mdi:brightness-7", "Raw Full Spectrum","sensor"),
    "ir_lux":               ("cnt", "none", "mdi:cctv", "Raw IR","sensor"),
    "uv":                   ("UV Index", "none", "mdi:sunglasses", "UV Index","sensor"),

    # --- Lightning ---
    "strikes":              ("count", "none", "mdi:flash", "Lightning Strikes","sensor"),
    "strike_distance":      ("km", "distance", "mdi:flash-alert", "Storm Distance","sensor"),
    "storm_dist":           ("km", "distance", "mdi:flash-alert", "Storm Distance","sensor"),

    # --- Battery ---
    "battery_mV":           ("mV", "voltage", "mdi:gauge", "Battery Voltage","sensor"),
    "battery_ok":           ("","battery","","Battery","binary_sensor"),

    # --- Soil Moisture ---
    "moisture":            ("%", "moisture", "mdi:water-percent", "Soil Moisture"),
    

    # --- Radio Diagnostics ---
    "freq":                 ("MHz", "frequency", "mdi:sine-wave", "Frequency","sensor"),
    "freq1":                ("MHz", "frequency", "mdi:sine-wave", "Frequency","sensor"),
    "freq2":                ("MHz", "frequency", "mdi:sine-wave", "Frequency","sensor"),
    "mod":                  ("", "none", "mdi:waveform", "Modulation","sensor"),
    "modulation":           ("", "none", "mdi:waveform", "Modulation","sensor"),
    "rssi":                 ("dB", "signal_strength", "mdi:wifi", "Signal (RSSI)","sensor"),
    "snr":                  ("dB", "signal_strength", "mdi:signal-distance-variant", "Signal (SNR)","sensor"),
    "noise":                ("dB", "signal_strength", "mdi:volume-high", "Noise Floor","sensor"),
    "id":                   ("", "none", "mdi:identifier", "Device ID","sensor"),
    "channel":              ("", "none", "mdi:radio-tower", "Channel","sensor"),
    "mic":                  ("", "none", "mdi:check-network", "Integrity Check","sensor"),
    "radio_status":         ("", "none", "mdi:usb-port", "Radio Status","sensor"),

    # --- Utility Meters ---
    "Consumption":          ("ft³", "gas", "mdi:fire", "Gas Usage","sensor"),
    "consumption":          ("ft³", "gas", "mdi:fire", "Gas Usage","sensor"),
    "meter_reading":        ("ft³", "water", "mdi:water-pump", "Water Reading","sensor"),

}