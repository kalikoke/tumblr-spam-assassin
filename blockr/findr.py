from .tumblr import Tumblr

EXAMPLE_SPAMMER = "makarinab88"

class Findr:
    def __init__(self, api_key, popular_tag):
        self.api_key = api_key
        self.popular_tag = popular_tag
        self.link_urls = []
        self.spam_blogs = []
        self.tumblr = Tumblr(self.api_key)

    def find_spam_blogs(self):
        self.get_common_link_urls()
        results = self.tumblr.tagged(self.popular_tag)
        for blog in results:
            if "link_url" in blog.keys():
                if self.link_baseurl(blog["link_url"]) in self.link_urls:
                    self.spam_blogs.append(blog["blog_name"])

        return self.spam_blogs

    def get_common_link_urls(self, spammer_username=EXAMPLE_SPAMMER):
        for post_data in self.tumblr.posts(spammer_username):
            self.link_urls.append(self.link_baseurl(post_data["link_url"]))

    def link_baseurl(self, link_url):
        return link_url.split("/")[2]