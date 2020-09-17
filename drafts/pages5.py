from k3 import *
from urllib.parse import unquote
from k3.drafts.htmltemp import *

# http://localhost:9000/k3/drafts/pages4.py?a=b&c=d

Arguments = get_Arguments(
    Defaults={
        'url':None,
    }
)


if __name__ == '__main__':
    main(**Arguments)



#http://localhost:9000/k3/utils/core/paths.py?a=1&b=2&c=3

#EOF
