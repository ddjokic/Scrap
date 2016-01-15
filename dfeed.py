#!/usr/bin/env python
# coding=utf8

""" Shamelesly copied from Dr. Drang's script http://leancrew.com/all-this/2015/12/homemade-rss-aggregator-followup/
Code added by me is ugly, but it works. For me. Paths to resulting file is hardcoded as well as subscriptions.
Deki, 2016"""

import feedparser as fp
import time
from datetime import datetime, timedelta
import pytz
import os
import subprocess

subscriptions = [
  'https://carpeaqua.com/',
  'http://kk.org/',
  'http://statusq.org/',
  'http://hiltmon.com/',
  'http://feedpress.me/512pixels',
  'https://buckwoody.wordpress.com/',
  'http://ozar.me/',
  'http://shallowsky.com/blog/',
  'http://www.leancrew.com/all-this/feed/',
  'http://www.hanselman.com/blog/',
  'http://ihnatko.com/feed/',
  'http://kieranhealy.org/blog/index.xml',
  'http://blueplaid.net/news?format=rss',
  'http://brett.trpstra.net/brettterpstra',
  'http://feeds.feedburner.com/NerdGap',
  'http://www.libertypages.com/clarktech/?feed=rss2',
  'http://feeds.feedburner.com/CommonplaceCartography',
  'http://kk.org/cooltools/feed',
  'http://daringfireball.net/feeds/main',
  'http://feeds.feedburner.com/drbunsenblog',
  'http://www.gnuplotting.org/feed/',
  'http://feeds.feedburner.com/IgnoreTheCode',
  'http://indiestack.com/feed/',
  'http://feeds.feedburner.com/JamesFallows',
  'http://feeds.feedburner.com/theendeavour',
  'http://feed.katiefloyd.me/',
  'http://feeds.feedburner.com/KevinDrum',
  'http://www.kungfugrippe.com/rss',
  'http://www.caseyliss.com/rss',
  'http://www.macdrifter.com/feeds/all.atom.xml',
  'http://mackenab.com/feed',
  'http://hints.macworld.com/backend/osxhints.rss',
  'http://macsparky.com/blog?format=rss',
  'http://www.macstories.net/feed/',
  'http://www.marco.org/rss',
  'http://mjtsai.com/blog/feed/',
  'http://nathangrigg.net/feed.rss',
  'http://onethingwell.org/rss',
  'http://feeds.feedburner.com/PracticallyEfficient',
  'http://feedpress.me/sixcolors',
  'http://joe-steel.com/feed',
  'http://feeds.veritrope.com/',
  'http://doingthatwrong.com/?format=rss']

# Date and time setup. I want only posts from "today," 
# where the day lasts until 2 AM.
utc = pytz.utc
homeTZ = pytz.timezone('US/Central')
dt = datetime.now(homeTZ)
if dt.hour < 2:
  dt = dt - timedelta(hours=24)
start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
start = start.astimezone(utc)

# Collect all of today's posts and put them in a list of tuples.
posts = []
for s in subscriptions:
  f = fp.parse(s)
  try:
    blog = f['feed']['title']
  except KeyError:
    continue
  for e in f['entries']:
    try:
      when = e['published_parsed']
    except KeyError:
      when = e['updated_parsed']
    when =  utc.localize(datetime.fromtimestamp(time.mktime(when)))
    if when > start:
      title = e['title']
      try:
        body = e['content'][0]['value']
      except KeyError:
        body = e['summary']
      link = e['link']
      posts.append((when, blog, title, link, body))

# Sort the posts in reverse chronological order.
posts.sort()
posts.reverse()
## create html file here?
# Turn them into an HTML list.
listTemplate = '''<li>
  <p class="title"><a href="{3}">{2}</a></p>
  <p class="info">{1}<br />{0}</p>
  <p>{4}</p>\n</li>'''
litems = []
for p in posts:
  q = [ x.encode('utf8') for x in p[1:] ]
  timestamp = p[0].astimezone(homeTZ)
  q.insert(0, timestamp.strftime('%b %d, %Y %I:%M %p'))
  litems.append(listTemplate.format(*q))
ul = '\n<hr />\n'.join(litems)
fname = "daily"+".html"
fn=open(fname, 'w')
# Print the HTMl.
page = '''<html>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width" />
<head>
<style>
body {{
  background-color: #555;
  width: 750px;
  margin-top: 0;
  margin-left: auto;
  margin-right: auto;
  padding-top: 0;
}}
h1 {{
  font-family: Helvetica, Sans-serif;
}}
.rss {{
  list-style-type: none;
  margin: 0;
  padding: .5em 1em 1em 1.5em;
  background-color: white;
}}
.rss li {{
  margin-left: -.5em;
  line-height: 1.4;
}}
.rss li pre {{
  overflow: auto;
}}
.rss li p {{
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
  -webkit-hyphens: auto;
  hyphens: auto;
}}
.title {{
  font-weight: bold;
  font-family: Helvetica, Sans-serif;
  font-size: 110%;
  margin-bottom: .25em;
}}
.title a {{
  text-decoration: none;
  color: black;
}}
.info {{
  font-size: 85%;
  margin-top: 0;
  margin-left: .5em;
}}
img {{
  max-width: 700px;
}}
@media screen and (max-width:667px) {{
  body {{
    font-size: 200%;
    width: 650px;
    background-color: white;
  }}
  .rss li {{
    line-height: normal;
  }}
  img {{
    max-width: 600px;
  }}
}}
</style>
<title>Today’s Blog-Feed</title>
<body>
<ul class="rss">
{}
</ul>
</body>
</html>
'''.format(ul)
fn.write(page)
fn.close()


if os.sys.platform.startswith('darwin'):
	#source = "/Users/Deki/Dropbox/daily.html"
    subprocess.call(('open', "/Users/Deki/Dropbox/daily.html"))
elif os.name == 'nt':
    os.startfile("C:\Users\Deki\Dropbox\daily.html")
elif os.name == 'posix':
    subprocess.call(('xdg-open', source))

