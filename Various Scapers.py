from requests_html import HTMLSession
import pandas as pd


def site_scraper():

    session = HTMLSession()

    title_list = []
    link_list = []
    time_list = []

    for page in range(1, 3):  # Total of 17

        url = f"https://coreyms.com/page/{page}"

        req = session.get(url)
        req.html.render(sleep=1, timeout=100, keep_page=True)

        articles = req.html.find("main.content")
        for article in articles:
            titles = article.find(".entry-title")
            for title in titles:
                title_list.append(title.text)

            links = article.find("a.entry-title-link")
            for link in links:
                link_list.append(link.attrs["href"])

            times = article.find("time.entry-time")
            for time in times:
                time_list.append(time.text)

    x = len(link_list)

    d_frame = pd.DataFrame({
        "Title": title_list,
        "Link": link_list,
        "Date": time_list,
    }, index=range(1, x+1))

    return print(d_frame)


def bookstore_scraper():

    session = HTMLSession()

    title_list = []
    price_list = []
    stock_list = []
    link_list = []

    for page in range(1, 3):  # Total of 50 pages
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        req = session.get(url)

        req.html.render(sleep=1, timeout=30)

        table = req.html.find("ol.row")

        for book in table:
            for title in book.find("h3"):
                title_list.append(title.text)

            links_list = []
            for link in book.find("a"):
                links_list.append(link.attrs["href"])

            for x in range(0, len(links_list), 2):
                link_list.append(links_list[x])

            for price in book.find(".price_color"):
                price_list.append(price.text)

            for stock in book.find(".instock"):
                stock_list.append(stock.text)
    d_frame = pd.DataFrame({
        "Title": title_list,
        "Price": price_list,
        "Link": link_list,
        "Status": stock_list
    }, index=range(1, len(price_list)+1))

    return print(d_frame)


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


Youtube_Home_Scraper()
