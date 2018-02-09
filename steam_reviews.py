import requests

def getSteamReviews(appid, printProgress=False):
    '''Request reviews from the Steam Web API and return them as a list. This is a blocking call that may take some time, depending on how many reviews there are.\n
    **appid** -- The Steam App ID as a string obtained from the game's store page URL\n
    **progress** -- Set to true to print the progress of each request.
    '''
    assert type(appid) is str

    def _makeRequest(appid, params):
        '''Helper function that sends a request to the Steam Web API and returns the response object.\n
        **appid** -- The Steam App ID obtained from the game's Store page URL\n
        **params** -- An object used to build the Steam API query. (https://partner.steamgames.com/doc/store/getreviews)
        '''
        response = requests.get(url=ENDPOINT+appid, params=params) # get the data from the endpoint
        return response.json() # return data extracted from the json response

    ENDPOINT = 'https://store.steampowered.com/appreviews/' # https://partner.steamgames.com/doc/store/getreviews
    results = []
    params = {
        'json': 1,
        'filter': 'recent', # sort by: recent, update
        'language': 'english', # languages at https://partner.steamgames.com/doc/store/localization
        'start_offset': 0, # for pagination
        'review_type': 'all', # all, positive, negative
        'purchase_type': 'all' # all, non_steam_purchase, steam
    }

    data = _makeRequest(appid, params)
    done = False

    while not done:
        if 'success' in data and data['success'] == 1: # if the query was successful
            if 'reviews' in data and len(data['reviews']) > 0: # if we received reviews
                results += data['reviews'] # add the reviews in this query to our results
                params['start_offset'] += data['query_summary']['num_reviews'] # increase the start offset by the number of reviews received in this response
                if printProgress:
                    print('{amount} reviews found...'.format(amount=params['start_offset']))
                data = _makeRequest(appid, params) # get the next page of reviews
            else: # there are no more reviews
                done = True
        elif data is None: # Steam Web API returns null if rate limit is reached.
            done = True
            raise ConnectionRefusedError('Steam Web API returned null. Rate limit may be exceeded.')
        else: # unsuccessful API call raises an error
            done = True
            raise ConnectionError('Steam Web API appreviews request was unsuccessful.')
    
    if printProgress:
        print("Found all reviews.")
    return results