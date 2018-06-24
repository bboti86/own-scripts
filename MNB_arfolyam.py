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
    exchangeRate = float(soup.select("div > span")[-1].contents[0].
                         replace(',', '.'))
    if exchangeRate == 1.0:
        raise ValueError("The date requested:"
                         " {} was a holiday in Hungary".format(date))
    else:
        return exchangeRate


dates = ["2018.01.22.", "2018.02.20.", "2018.03.20.", "2018.04.20.",
         "2018.05.20.", "2018.06.20."]

for date in dates:
    print(date + ": ", MNBArfolyam(date))
    sleep(1)

for date in dates:
    print(date + ": ", MNBArfolyam(date, "USD"))
    sleep(1)
