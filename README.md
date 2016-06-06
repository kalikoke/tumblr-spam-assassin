# Setup

``` shell
docker build -t blockr/dev .
docker run --rm -v "$PWD":/usr/src/app -it blockr/dev ipython
```

# In IPython:

```
%load_ext autoreload
%autoreload 2
from blockr import Tumblr
tumblr = Tumblr(YOUR_API_KEY)
tumblr.posts("someannoyingspam")
```

