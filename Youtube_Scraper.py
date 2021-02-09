from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

url = "https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos"

req = session.get(url)
req.html.render(sleep=1, scrolldown=10)

videos = req.html.find("#video-title")
visualizations = req.html.find("#style-scope ytd-grid-video-renderer")

title = []
link = []
vis = []
for item in videos:
    title.append(item.text)
    link.append(item.absolute_links)

for ite in visualizations:
    vis.append(ite)
    print(vis)
