from .tumblr import Tumblr

EXAMPLE_SPAMMER = "makarinab88"
EXAMPLE_TAG = "hamilton"

class Findr:
    def __init__(self, api_key):
        self.api_key = api_key
        self.link_urls = []
        self.popular_tags = []
        self.spam_blogs = [EXAMPLE_SPAMMER]
        self.tumblr = Tumblr(self.api_key)

    def find_targets(self):
        print "Initial seed"
        self.find_spam_blogs_in_tag(EXAMPLE_TAG)
        print "Will attempt to get targets"
        self.get_popular_tags()
        for tag in self.popular_tags:
            self.find_spam_blogs_in_tag(tag)

    def find_spam_blogs_in_tag(self, popular_tag):
        self.get_common_link_urls()
        print "Let's find some spam blogs in %s" % popular_tag
        results = self.tumblr.tagged(popular_tag)
        for blog in results:
            print ".",
            if "link_url" in blog.keys():
                if self.link_baseurl(blog["link_url"]) in self.link_urls:
                    self.spam_blogs.append(blog["blog_name"])

        self.trim_spam_blogs()
        print "Found: %d spammers!" % (len(self.spam_blogs))

    def get_common_link_urls(self):
        for spammer_username in self.spam_blogs:
            for post_data in self.tumblr.posts(spammer_username):
                self.link_urls.append(self.link_baseurl(post_data["link_url"]))

        self.link_urls = list(set(self.link_urls))

    def get_popular_tags(self):
        print "Finding popular tags"
        for spammer_username in self.spam_blogs:
            for post in self.tumblr.posts(spammer_username):
                self.popular_tags.extend(post["tags"])
        self.trim_popular_tags()
        print "Found %d popular tags" % len(self.popular_tags)

    def link_baseurl(self, link_url):
        return link_url.split("/")[2]

    def trim_spam_blogs(self):
        self.spam_blogs = list(set(self.spam_blogs))

    def trim_popular_tags(self):
        self.popular_tags = list(set(self.popular_tags))

