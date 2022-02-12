# SFMovieLocations
Visualise the locations of a movie shot in San Franscisco on a map.

This is a backend focused application with necessary frontend code. Using Django and pandas in backend and HTML, CSS, JavaScript for frontend, this application takes a movie name as an input and displays the locations the movie has been shot on a map. For location data, data set from [DataSF](https://data.sfgov.org/Arts-Culture-and-Recreation-/Film-Locations-in-San-Francisco/yitu-d5am)  is being used and to extract geo-coordinates [GeoPy](https://pypi.org/project/geopy/) library is used. For visualization, [folium](https://pypi.org/project/folium/) package is used. 

The application also supports autocomplete for movie search.

### Local setup:
**Prerequisites:**
Python3

**Steps:**
1. Clone repo
2. Create a virtualenv and install requirements
   ```
    pip install requirements.txt
   ```
3. Run server
   ```commandline
    python manage.py runserver
   ```
4. Open the server link on browser and go on and look up any movie! This will return the locations the movie has been shot in San Franscisco.
