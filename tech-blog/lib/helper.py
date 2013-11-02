
def js_tag(url):
    return "<script src=\"%s\"></script>" % url

def css_tag(url):
    return "<link href=\"%s\" rel=\"stylesheet\">" % url



def js_asset_tag(base_url, path):
    return js_tag("%s/static/js/%s" % (base_url, path) )

def css_asset_tag(base_url, path):
    return css_tag("%s/static/css/%s" % (base_url, path) )

def url(base_url, path):
    return "%s/%s" % (base_url, path)


# shortcut
def home_url(base_url):
    return url(base_url, "index.html")

def archives_url(base_url):
    return url(base_url, "archives.html")

# youtube
def youtube_tag(id, width=420, height=315):
    if id.startswith("http"):
        id = _extract_query(id, "v")
    return "<iframe width=\"%s\" height=\"%s\" src=\"http//www.youtube.com/embed/%s\" frameborder=\"0\" allowfullscreen></iframe>" % (width, height, id)


def _extract_query(url, key):
    pos = url.find("?")+1
    qs = url[pos:].split("=")
    print qs
    for k,v in qs:
        if key == k:
            return v
    return ""
    

def string2cls(s):
    return "".join(s.split(" ")).lower()
