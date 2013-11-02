import markdown
from markdown import Extension
from markdown.inlinepatterns import Pattern

class MediaExtension(Extension):
    def __init__(self, base_url = ""):
        self.base_url = base_url
        self.config = {}

    def extendMarkdown(self, md, md_globals):
        self.md = md
        MEDIA_RE = r'\[\[media:([\w0-9, _\-\.\/]+)\]\]'
        mediaPattern = MediaPattern(MEDIA_RE, self.getConfigs())
        mediaPattern.setBaseUrl(self.base_url)
        md.inlinePatterns.add("media", mediaPattern, "<not_strong")

class MediaPattern(Pattern):

    def setBaseUrl(self, url):
        self.base_url = url

    def handleMatch(self, m):
        base_url = self.base_url
        if base_url:
            if not base_url.endswith("/"):
                base_url += "/"
        
        s = m.group(2)
        a = s.split(",")
        l = len(a)
        
        if l == 1:
            url = base_url + a[0].strip()
            return self.singleImg(url)
        else:
            div = markdown.util.etree.Element('div')
            div.set("class", "media-group")
            for i in a:
                url = base_url + i.strip()
                div.append(self.singleImg(url))
            return div               

    def singleImg(self, url):
        obj = markdown.util.etree.Element('img')
        obj.set("src", url)
        obj.set("class", "media")
        return obj

