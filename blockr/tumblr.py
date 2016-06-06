import requests, json

API_BASEURL = "https://api.tumblr.com/v2"
API_ENDPOINTS = {
    "blog": "/blog/%s/%s?api_key=%s",
    "tagged": "/tagged?tag=%s&api_key=%s"
}

class Tumblr:
    def __init__(self, api_key):
        self.api_key = api_key

    def tagged(self, tag):
        url = self.api_url("tagged") % (tag, self.api_key)
        return self.get_request(url)["response"]

    def posts(self, blog_identifier):
        url = self.api_url("blog") % (blog_identifier,
                                      "posts",
                                      self.api_key)
        return self.get_request(url)["response"]["posts"]

    def get_request(self, url):
        r = requests.get(url)
        return r.json()

    def api_url(self, endpoint):
        return API_BASEURL + API_ENDPOINTS[endpoint]
