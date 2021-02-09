from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests_html import HTMLSession
import string

def scrape_Meditations():
    url = "https://www.amazon.com/Meditacoes-Em-Portugues-do-Brasil/dp/8552100916"
    path = "c:\\Users\lucas\Chrome_Webdriver\chromedriver.exe"

    title_id = "productTitle"
    price_xpath = '//*[@id="a-autoid-3-announce"]/span[2]/span'

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(path, options=options)
    driver.get(url)

    product_title = driver.find_element_by_id(title_id).text
    product_price = driver.find_element_by_xpath(price_xpath).text

    print(product_title)
    print(product_price)

    driver.quit()

def getPrice(amaz_url):
    s = HTMLSession()
    req = s.get(amaz_url)
    req.html.render(sleep=1)
    Product = req.html.xpath('//*[@id="productTitle"]', first=True).text
    Price = req.html.xpath('//*[@id="a-autoid-3-announce"]/span[2]/span', first=True).text
    print(Product)
    print(Price)

getPrice("https://www.amazon.com/Meditacoes-Em-Portugues-do-Brasil/dp/8552100916/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=1609035766&sr=8-6")

#scrape_Meditations()
