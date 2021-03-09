import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

url = "https://finance.naver.com/search/searchList.nhn?query="

def get_request()
    # Search input & incode to euc-kr
    search_for = input("Search for: ")
    encode_euc_kr = search_for.encode('euc-kr')
    to_string = str(encode_euc_kr)
    # to_string has escape codes, cleaning up
    replace_text = to_string.replace(r"\x", "%").strip("b").split("'")
    search_url = url+replace_text[1]

def find_name_link(search_url)
    # get the page and find names of the stock
    response = requests.get(search_url, headers=headers)
    response.encoding = 'euc-kr'
    soup = BeautifulSoup(response.text, "html.parser")
    find_table = soup.find("table", {"class": "tbl_search"})
    href_list = find_table.find_all("td", {"class": "tit"})
    # dict for saving stock name and web address
    stock = {}
    # find name and web addresses 
    # for each stock and save them to stock dict
    for items in href_list:
    name = items.find("a").text
    find_href = items.find("a")["href"].strip(" ")
    href = "https://finance.naver.com"+find_href
    stock[name]=href