import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

url = "https://finance.naver.com/search/searchList.nhn?query="

def get_request(name):
    # Search input & incode to euc-kr
    encode_euc_kr = name.encode('euc-kr')
    to_string = str(encode_euc_kr)
    # to_string has escape codes, cleaning up
    replace_text = to_string.replace(r"\x", "%").strip("b").split("'")
    search_url = url+replace_text[1]
    return search_url

def save_stock(stock):
  name = stock.find("a").text
  find_href = stock.find("a")["href"].strip(" ")
  href = "https://finance.naver.com"+find_href
  return {
    'name': name,
    'link' : href
  }

def find_name_link(search_url):
  stocks = []
  # get the page and find names of the stock
  response = requests.get(search_url, headers=headers)
  response.encoding = 'euc-kr'
  soup = BeautifulSoup(response.text, "html.parser")
  find_table = soup.find("table", {"class": "tbl_search"})
  href_list = find_table.find_all("td", {"class": "tit"})
  for item in href_list:
    stock = save_stock(item)
    stocks.append(stock)
  return stocks