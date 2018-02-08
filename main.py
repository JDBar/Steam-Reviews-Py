import requests

ENDPOINT = "https://store.steampowered.com/appreviews/"

def getAllReviews(appid="404200"):
  """Request reviews from the Steam Web API and return them as a list.
  \n**appid** -- The Steam App ID obtained from the game's stoe page URL
  """

  def makeRequest(appid, params):
    """Sends a request to the Steam Web API and return the response object.
    \n**appid** -- The Steam App ID obtained from the game's Store page URL
    \n**params** -- A dictionary used to build the Steam API query. (https://partner.steamgames.com/doc/store/getreviews)
    """
    # get the data from the endpoint
    response = requests.get(url = ENDPOINT + appid, params = params)
    # return data from the json response
    return response.json()
    
  results = []
  params = {
    'json': 1,
    'filter': 'recent',
    'language': 'english', # languages at https://partner.steamgames.com/doc/store/localization
    'start_offset': 0, # for pagination
    'review_type': 'all', # all, positive, negative
    'purchase_type': 'all' # all, non_steam_purchase, steam
  }

  data = makeRequest(appid, params)

  done = False
  while not done:
    if hasattr(data, 'success') and data.success == 1:
      if hasattr(data, 'total_reviews'):
        # there are more pages of reviews to request
        # increase the start offset by the number of reviews received in this response
        params['start_offset'] += data.num_reviews
        # add the reviews in this query to our results
        results += data.reviews
        # get more reviews
        data = makeRequest(appid, params)
      else:
        # this is the last page of reviews
        done = True
    else:
      # unsuccessful API call raises an error
      raise ConnectionRefusedError("Steam Web API appreviews request was unsuccessful.")
  
  return results