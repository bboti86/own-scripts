"""
MNB árfolyam puller.

Simple tool for querying the currency exchange rate of the
Hungarian National Bank for one particular day
Currently only EUR is supported
"""
from time import sleep


def MNBArfolyam(date):
    """
    MNB árfolyam puller.

    Simple tool for querying the currency exchange rate of the
    Hungarian National Bank for one particular day
    Currently only EUR is supported
    TODO:
    1) validate parameters
    2) if query response is 1, that means that the date was not a working day
        this has to be checked by the function
    2) implement other currencies
    Input parameters:
        date: the date you are looking for, has to be yyyy.mm.dd. format!
    """
    import requests
    from bs4 import BeautifulSoup

    # potentially implement ither currencies
    url_head = "https://www.mnb.hu/arfolyam-tablazat?"
    url = "deviza=rbCurrencySelect&devizaSelected=EUR&datefrom={}&datetill={}"
    url_tail = "&order=1"
    url = url_head+url+url_tail
    # print(url)

    # validate date

    response = requests.get(url.format(date, date))
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    return float(soup.select("div > span")[-1].contents[0].replace(',', '.'))


dates = ["2018.01.22.", "2018.02.20.", "2018.03.20.", "2018.04.20.",
         "2018.05.22.", "2018.06.20."]

for date in dates:
    print(date + ": ", MNBArfolyam(date))
    sleep(1)
