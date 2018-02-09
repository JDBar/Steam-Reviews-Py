import requests

  """Request reviews from the Steam Web API and return them as a list.\n
  **appid** -- The Steam App ID obtained from the game's stoe page URL
  """

  def makeRequest(appid, params):
    """Sends a request to the Steam Web API and return the response object.\n
    **appid** -- The Steam App ID obtained from the game's Store page URL\n
    **params** -- An object used to build the Steam API query. (https://partner.steamgames.com/doc/store/getreviews)
    """
    response = requests.get(url = ENDPOINT + appid, params = params) # get the data from the endpoint
    return response.json() # return data extracted from the json response
    
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
    if 'success' in data and data['success'] == 1: # if the query was successful
      if 'reviews' in data and len(data['reviews']) > 0: # if we received reviews
        results += data['reviews'] # add the reviews in this query to our results
        params['start_offset'] += data['query_summary']['num_reviews'] # increase the start offset by the number of reviews received in this response
        data = makeRequest(appid, params) # get the next page of reviews
      else: # there are no more reviews
        done = True
    elif data is None: # Steam Web API returns null if rate limit is reached.
      done = True
      raise ConnectionRefusedError("Steam Web API returned null. Rate limit may be exceeded.")
    else: # unsuccessful API call raises an error
      done = True
      raise ConnectionError("Steam Web API appreviews request was unsuccessful.")
  
  return results

