# Steam-Reviews-Py
Get reviews from the Steam Web API.

## Usage
Place `steam_reviews.py` in your project.

Make sure to install **Requests** using `pipenv install request` or `pip install request`.
```Python
import steam_reviews
reviews = steam_reviews.get('748600') # warning! this is a blocking operation!
```

## :heavy_plus_sign: Dependencies
This script uses **[Requests](http://docs.python-requests.org/en/latest/user/install/#install)**.

To install dependencies with **[pipenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)**, use `pipenv install requests` in your project directory.

If you don't want to use pipenv, you can just use `pip install requests`.

## :children_crossing: Warning!
This script, in its primitive state, is blocking. The Steam Web API only allows 20 reviews to be returned at a time, so multiple blocking requests are made until all reviews have been received. For real-time applications, this will require transitioning the script to a http request library with support for concurrent asynchronous requests.
