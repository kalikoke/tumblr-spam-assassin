from .tumblr import Tumblr

EXAMPLE_SPAMMER = "makarinab88"

class Findr:
    def __init__(self, api_key):
        self.api_key = api_key
        self.link_urls = []
        self.spam_blogs = []
        self.tumblr = Tumblr(self.api_key)

    def find_spam_blogs(self, popular_tag, spammer_username=EXAMPLE_SPAMMER):
        print "Finding spammers in %s" % popular_tag
        self.get_common_link_urls(spammer_username)
        results = self.tumblr.tagged(popular_tag)
        for blog in results:
            print ".",
            if "link_url" in blog.keys():
                if self.link_baseurl(blog["link_url"]) in self.link_urls:
                    self.spam_blogs.append(blog["blog_name"])

        self.trim_spam_blogs()
        print "Found: %d spammers!" % (len(self.spam_blogs))
        return self.spam_blogs

    def get_common_link_urls(self, spammer_username=EXAMPLE_SPAMMER):
        for post_data in self.tumblr.posts(spammer_username):
            self.link_urls.append(self.link_baseurl(post_data["link_url"]))

        list(set(self.link_urls))

    def link_baseurl(self, link_url):
        return link_url.split("/")[2]

    def trim_spam_blogs(self):
        self.spam_blogs = list(set(self.spam_blogs))


