import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, "templates")

map_filename = os.path.join(MEDIA_ROOT, "maps", "locations_map.html")

movie_data_url = "https://data.sfgov.org/resource/yitu-d5am.json?title=%s"

geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"
