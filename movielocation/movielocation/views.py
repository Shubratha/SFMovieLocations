import logging
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView

from .utils import MoviesData, get_and_plot_locations

logger = logging.getLogger(__name__)


def home(request):
    movies = MoviesData().data["Title"].unique()
    return render(request, "index.html", {"movies": movies})


class Locations(APIView):
    """
    Display locations of movie shoot
    """

    def get(self, request):
        try:
            movie = request.GET.get("movie")
            if not movie:
                return HttpResponse(
                    "<h3>Please provide movie name</h3>",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if movie and not movie.strip():
                return HttpResponse(
                    "<h3>Please provide valid movie name</h3>",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            map_file = get_and_plot_locations(movie)
            if not map_file:
                return HttpResponse(
                    "<h3>No locations found. Please try again</h3>",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return render(request, map_file, status=200)

        except Exception as e:
            logger.critical(
                "Exception in GetLocations %s, Traceback: %s"
                % (str(e), str(traceback.format_exc()))
            )
            return HttpResponse(
                "<h3>Internal server error</h3>",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
