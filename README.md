# Setup

``` shell
docker build -t blockr/dev .
docker run --rm -v "$PWD":/usr/src/app -it blockr/dev ipython
```

# In IPython:

```
%load_ext autoreload
%autoreload 2
from tumblr_spam_assassin import Findr 
findr = Findr(YOUR_API_KEY)
findr.find_spam_blogs("jessica jones")
```

