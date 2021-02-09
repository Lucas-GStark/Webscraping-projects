from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options
from requests_html import HTMLSession
import pandas as pd

def Youtube_Home_Scraper():

    session = HTMLSession()

    video_title = []
    video_link = []
    channel_name = []
    channel_link = []

    url = "https://www.youtube.com/"

    req = session.get(url)
    req.html.render(sleep=1, timeout=30, scrolldown=10)

    videos_table = req.html.find("#contents")
    for video_table in videos_table:
        titles = video_table.find("#video-title")
        for element in titles:
            video_title.append(element.text)

        links = video_table.find("#video-title-link")
        for link in links:
            video_link.append(url + link.attrs["href"])

        channels = video_table.find("a.yt-simple-endpoint.style-scope.yt-formatted-string")
        for channel in channels:
            channel_name.append(channel.text)
            channel_link.append(url + channel.attrs["href"])

        d_frame = pd.DataFrame({
            "Title": video_title,
            "Link": video_link,
            "Channel": channel_name,
            "Channel Link": channel_link
        }, index=range(1, len(video_title) + 1))

        return print(d_frame)

    url_input = "google.com"
    def selenium(url_input):
        options=Options()
        path = "c:\\Users\lucas\Chrome_Webdriver\chromedriver.exe"

        urls = []

        for tit in d_frame["Title"]:
            new_url = urls.append("google.com/"+tit)

        driver = webdriver.Chrome(path, options=options)
        driver.get(url.input)


Youtube_Home_Scraper()