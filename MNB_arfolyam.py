"""
MNB árfolyam puller.

Simple tool for querying the currency exchange rate of the
Hungarian National Bank for one particular day
"""
from time import sleep


def MNBArfolyam(date, currency="EUR"):
    """
    MNB árfolyam puller.

    Simple tool for querying the currency exchange rate of the
    Hungarian National Bank for one particular day

    TODO:
    1) if query response is 1, that means that the date was not a working day
        this has to be checked by the function

    Input parameters:
        date: the date you are looking for, has to be yyyy.mm.dd. format!
        currency: a three letter string, eg: "EUR", defaults to "EUR" as Euros
    """
    import requests
    from bs4 import BeautifulSoup
    import datetime

    try:
        datetime.datetime.strptime(date, "%Y.%m.%d.")
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY.mm.dd.")

    url = "https://www.mnb.hu/arfolyam-tablazat?" \
          "deviza=rbCurrencySelect" \
          "&devizaSelected={}" \
          "&datefrom={}" \
          "&datetill={}" \
          "&order=1"
    # print(url)

    response = requests.get(url.format(currency, date, date))
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    return float(soup.select("div > span")[-1].contents[0].replace(',', '.'))


dates = ["2018.01.22.", "2018.02.20.", "2018.03.20.", "2018.04.20.",
         "2018.05.22.", "2018.06.20."]

for date in dates:
    print(date + ": ", MNBArfolyam(date))
    sleep(1)

for date in dates:
    print(date + ": ", MNBArfolyam(date, "USD"))
    sleep(1)
