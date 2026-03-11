"""
export_mission.py
─────────────────────────────────────────────────────────────────
Figure-8 waypoint üretir ve QGroundControl'ün okuyabileceği
.plan formatında diske kaydeder. Araca bağlantı gerekmez.

Kullanım:
    python export_mission.py                        # varsayılan parametreler
    python export_mission.py --output gozlem.plan   # farklı dosya adı

Sonra QGroundControl'de:
    Plan → Sync → Load From File → .plan dosyasını seç → Upload To Vehicle
"""

import json
import math
import argparse

# ──────────────────────────────────────────────────────────────
# PARAMETRELER — buradan düzenle
# ──────────────────────────────────────────────────────────────
DEFAULT_PYLON1      = (39.9334, 32.8597)   # (lat, lon)
DEFAULT_PYLON2      = (39.9340, 32.8597)   # (lat, lon)
DEFAULT_RADIUS_M    = 50.0                 # her lobenin yarıçapı (metre)
DEFAULT_ALTITUDE_M  = 100.0               # irtifa – göreceli AGL (metre)
DEFAULT_POINTS      = 16                   # lobe başına waypoint sayısı
DEFAULT_OUTPUT      = "figure8_mission.plan"


# ──────────────────────────────────────────────────────────────
# FIGURE-8 ÜRETİCİ
# ──────────────────────────────────────────────────────────────

def generate_figure8(pylon1, pylon2, radius, altitude, points_per_lobe):
    def offset(origin_lat, origin_lon, dx_m, dy_m):
        lat = origin_lat + dy_m / 111_320.0
        lon = origin_lon + dx_m / (111_320.0 * math.cos(math.radians(origin_lat)))
        return lat, lon

    waypoints = []
    for pylon in (pylon1, pylon2):
        for i in range(points_per_lobe):
            angle = 2 * math.pi * i / points_per_lobe
            dx =  radius * math.sin(angle)
            dy =  radius * math.cos(angle)
            lat, lon = offset(pylon[0], pylon[1], dx, dy)
            waypoints.append((lat, lon, altitude))
    return waypoints


# ──────────────────────────────────────────────────────────────
# QGC .PLAN EXPORT
# ──────────────────────────────────────────────────────────────

def to_qgc_plan(waypoints, home_lat, home_lon, cruise_speed=15):
    items = []
    for seq, (lat, lon, alt) in enumerate(waypoints):
        items.append({
            "AMSLAltAboveTerrain": None,
            "Altitude":            alt,
            "AltitudeMode":        1,          # 1 = Relative (AGL)
            "autoContinue":        True,
            "command":             16,          # MAV_CMD_NAV_WAYPOINT
            "doJumpId":            seq + 1,
            "frame":               3,           # MAV_FRAME_GLOBAL_RELATIVE_ALT
            "params":              [0, 5, 0, None, lat, lon, alt],
            "type":                "SimpleItem",
        })

    return {
        "fileType":     "Plan",
        "geoFence":     {"circles": [], "polygons": [], "version": 2},
        "groundStation": "QGroundControl",
        "mission": {
            "cruiseSpeed":         cruise_speed,
            "firmwareType":        3,           # ArduPilot
            "globalPlanAltitudeMode": 1,
            "hoverSpeed":          5,
            "items":               items,
            "plannedHomePosition": [home_lat, home_lon, 0],
            "vehicleType":         1,           # Fixed-wing
            "version":             2,
        },
        "rallyPoints":  {"points": [], "version": 2},
        "version":      1,
    }


# ──────────────────────────────────────────────────────────────
# ANA AKIŞ
# ──────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Figure-8 QGC .plan dosyası üret")
    p.add_argument("--p1-lat",  type=float, default=DEFAULT_PYLON1[0])
    p.add_argument("--p1-lon",  type=float, default=DEFAULT_PYLON1[1])
    p.add_argument("--p2-lat",  type=float, default=DEFAULT_PYLON2[0])
    p.add_argument("--p2-lon",  type=float, default=DEFAULT_PYLON2[1])
    p.add_argument("--radius",  type=float, default=DEFAULT_RADIUS_M)
    p.add_argument("--alt",     type=float, default=DEFAULT_ALTITUDE_M)
    p.add_argument("--points",  type=int,   default=DEFAULT_POINTS)
    p.add_argument("--output",  type=str,   default=DEFAULT_OUTPUT)
    args = p.parse_args()

    pylon1 = (args.p1_lat, args.p1_lon)
    pylon2 = (args.p2_lat, args.p2_lon)

    waypoints = generate_figure8(pylon1, pylon2, args.radius, args.alt, args.points)

    plan = to_qgc_plan(waypoints, home_lat=args.p1_lat, home_lon=args.p1_lon)

    with open(args.output, "w") as f:
        json.dump(plan, f, indent=2)

    print(f"[✓] {len(waypoints)} waypoint → '{args.output}' dosyasına yazıldı.")
    print(f"    QGroundControl: Plan → Sync → Load From File")


if __name__ == "__main__":
    main()
