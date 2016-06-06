import requests, json

API_BASEURL = "https://api.tumblr.com/v2"

class Tumblr:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_endpoints = {
            "blog": "/blog/%s/%s?api_key=%s",
            "tagged": "/tagged?tag=%s"
        }

    def posts(self, blog_identifier):
        return self.get_request(blog_identifier, "blog", "posts")["response"]["posts"]

    def get_request(self, blog_identifier, endpoint, option):
        r = requests.get(self.api_url(blog_identifier, endpoint, option))
        return r.json()

    def api_url(self, blog_identifier, endpoint, option):
        return API_BASEURL + self.api_endpoints[endpoint] % (blog_identifier,
                                                             option,
                                                             self.api_key)
