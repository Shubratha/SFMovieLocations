from geopy.geocoders import Nominatim
from geopy import Point
import requests
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from .constants import *
import logging

logger = logging.getLogger(__name__)


class MoviesData:
    def __init__(self):
        self.data = pd.read_csv("movielocation/data/Film_Locations_in_San_Francisco.csv")


class GeoCode:
    def __init__(self):
        self.geo_locator = Nominatim(user_agent="sf_movie")

    def get_coordinates_point(self, address):
        point_coordinates = None
        try:
            details = self.geo_locator.geocode(address)
            point_coordinates = details.point
        except Exception as e:
            logger.critical(
                "Exception in get_coordinates_point %s" % str(e)
            )

        return point_coordinates


def get_movie_details(movie):
    response = []
    try:
        url = movie_data_url % movie
        try:
            resp = requests.get(url)
            response = resp.json()
        except Exception as e:
            logger.critical(
                "Exception while calling sfgov data in get_movie_details %s" % str(e)
            )

    except Exception as e:
        logger.critical(
            "Exception in get_movie_details %s" % str(e)
        )

    return response


def get_movie_details_from_df(movie):
    # TOdO: get title, lat, long details from df, use this instead of get_locations
    data = MoviesData().data["Title"].unique()


def get_locations(movie):
    details = get_movie_details(movie)
    locations = []
    geocode = GeoCode()
    for detail in details:
        address = detail["locations"]
        location = geocode.get_coordinates_point(address)
        data = {
            "address": address,
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
        locations.append(data)

    return locations


def plot_map(locations):
    map_plotted = False
    try:
        location_df = pd.DataFrame.from_dict(locations)
        m = folium.Map(location=location_df[["latitude", "longitude"]].mean().to_list())
        marker_cluster = MarkerCluster().add_to(m)
        for i, r in location_df.iterrows():
            location = (r["latitude"], r["longitude"])
            folium.Marker(location=location, popup=r["address"], tooltip=r["address"]).add_to(
                marker_cluster
            )
        m.save(map_filename)
        map_plotted = True
    except Exception as e:
        logger.critical(
            "Exception in plot_map %s" % str(e)
        )

    return map_plotted


def get_and_plot_locations(movie):
    locations = get_locations(movie)
    is_ready = plot_map(locations)
    return map_filename if is_ready else ""

