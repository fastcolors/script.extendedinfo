from Utils import *

base_url = "http://www.omdbapi.com/?tomatoes=true&plot=full&r=json&"

def GetOmdbMovieInfo(imdb_id):
    try:
        url = 'i=%s' % (imdb_id)
        results = Get_JSON_response(base_url + url)
    except:
        results = None
        Notify("Error when fetching Omdb data from net")
    count = 1
    if results is not None:
        return results
    else:
        return {}



    return results