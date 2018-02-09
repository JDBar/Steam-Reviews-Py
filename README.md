# Steam-Reviews-Py
Get reviews from the Steam Web API.

## Usage
Place `steam_reviews.py` in your project.

Make sure to install **Requests** using `pipenv install request` or `pip install request`.
```Python
import steam_reviews
reviews = steam_reviews.get('748600') # warning! this is a blocking operation!
```

### steam_reviews.get(appid)
> Accepts a Steam App ID as a string, and returns a list of reviews, each with the following structure:
```Python
{
    'recommendationid': str # The unique id of the recommendation
    'author': {
        'steamid': str # the user’s SteamID
        'num_games_owned': int # number of games owned by the user
        'num_reviews': int #n umber of reviews written by the user
        'playtime_forever': int # lifetime playtime tracked in this app
        'playtime_last_two_weeks': int # playtime tracked in the past two weeks for this app
        'last_played': int # time for when the user last played
    }
    'language': str # language the user indicated when authoring the review
    'review': str # text of written review
    'timestamp_created': int # date the review was created (unix timestamp)
    'timestamp_updated': int # date the review was last updated (unix timestamp)
    'voted_up': bool # true means it was a positive recommendation
    'votes_up': int # the number of users that found this review helpful
    'votes_funny': int # the number of users that found this review funny
    'weighted_vote_score': int # (beta) value not used
    'comment_count': int # number of comments posted on this review
    'steam_purchase': bool # true if the user purchased the game on Steam
    'received_for_free': bool # true if the user checked a box saying they got the app for free
    'written_during_early_access': bool # true if the user posted this review while the game was in Early Access
}
```

## :heavy_plus_sign: Dependencies
This script uses **[Requests](http://docs.python-requests.org/en/latest/user/install/#install)**.

To install dependencies with **[pipenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)**, use `pipenv install requests` in your project directory.

If you don't want to use pipenv, you can just use `pip install requests`.

## :children_crossing: Warning!
This script, in its primitive state, is blocking. The Steam Web API only allows 20 reviews to be returned at a time, so multiple blocking requests are made until all reviews have been received. For real-time applications, this will require transitioning the script to a http request library with support for concurrent asynchronous requests.
