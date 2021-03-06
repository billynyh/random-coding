#!/usr/bin/python

# Chisel
# David Zhou
# 
# Requires:
# jinja2

import sys, re, time, os, codecs
import jinja2, markdown
from lib import helper
from lib.md_extension import MediaExtension
from config import *

#Settings
SOURCE = "./posts/" #end with slash
TEMPLATE_PATH = "./templates/"
TEMPLATE_OPTIONS = {}
TEMPLATES = {
    'home': "home.html",
    'detail': "detail.html",
    'archive': "archive.html",
}
TIME_FORMAT = "%B %d, %Y"
ENTRY_TIME_FORMAT = "%Y-%m-%d"
#FORMAT should be a callable that takes in text
#and returns formatted text

MEDIA_EXT = MediaExtension(MEDIA_PATH)
FORMAT = lambda text: markdown.markdown(text, ['footnotes', MEDIA_EXT]) 
#########



STEPS = []

def step(func):
    def wrapper(*args, **kwargs):
        print "Starting " + func.__name__ + "...",
        func(*args, **kwargs)
        print "Done."
    STEPS.append(wrapper)
    return wrapper

def get_tree(source):
    files = []
    post_tags = {}
    for root, ds, fs in os.walk(source):
        for name in fs:
            if name[0] == ".": continue
            print name
            path = os.path.join(root, name)
            f = open(path, "rU")
            title = f.readline()
            date = time.strptime(f.readline().strip(), ENTRY_TIME_FORMAT)
            year, month, day = date[:3]
            tags = []

            slug = os.path.splitext(name)[0]
            author = ""

            while True:
                s = f.readline()
                if s.strip() == "":
                    break
                a = s.split(":")
                a[0] = a[0].strip()
                if a[0] == "slug":
                    slug = a[1].strip()
                elif a[0] == "author":
                    author = a[1].strip()
                elif a[0] == "tag" or a[0] == "tags":
                    tmp = [x.strip() for x in a[1].split(",")]
                    s = set()
                    for x in tmp:
                        if not x in s:
                            tags.append(x)
                            s.add(x)
            for t in tags:
                post_tags[t] = post_tags.get(t, 0) + 1
            files.append({
                'title': title,
                'epoch': time.mktime(date),
                'content': FORMAT(''.join(f.readlines()[1:]).decode('UTF-8')),
                'url': '/'.join([str(year), "%.2d" % month, "%.2d" % day, slug + ".html"]),
                'pretty_date': time.strftime(TIME_FORMAT, date),
                'date': date,
                'year': year,
                'month': month,
                'day': day,
                'filename': name,
                'slug' : slug, # added by billynyh
                'author': author, # added by billynyh
                'tags' : tags,
            })
            f.close()
    return files, post_tags

def compare_entries(x, y):
    result = cmp(-x['epoch'], -y['epoch'])
    if result == 0:
        return -cmp(x['filename'], y['filename'])
    return result

def write_file(url, data):
    print "write_file " + url
    path = DESTINATION + url
    dirs = os.path.dirname(path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    file = open(path, "w")
    file.write(data.encode('UTF-8'))
    file.close()

@step
def generate_homepage(f, t, e):
    """Generate homepage"""
    template = e.get_template(TEMPLATES['home'])
    write_file("index.html", template.render(entries=f[:HOME_SHOW], 
        post_tags = t, base_url=ABS_PATH))

@step
def master_archive(f, t, e):
    """Generate master archive list of all entries"""
    template = e.get_template(TEMPLATES['archive'])
    write_file("archives.html", template.render(entries=f, 
        post_tags = t, base_url=ABS_PATH))

@step
def detail_pages(f, t, e):
    """Generate detail pages of individual posts"""
    template = e.get_template(TEMPLATES['detail'])
    for file in f:
        write_file(file['url'], template.render(entry=file, post_tags = t, base_url=ABS_PATH))

def main():
    print "Chiseling..."
    print "\tReading files...",

    files, post_tags = get_tree(SOURCE)
    files = sorted(files, cmp=compare_entries)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)
    env.globals['h'] = helper

    print "Done."
    print "\tRunning steps..."
    for step in STEPS:
        print "\t\t",
        step(files, post_tags, env)
    print "\tDone."
    print "Done."

if __name__ == "__main__":
    sys.exit(main())
