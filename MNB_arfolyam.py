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


def tests(wrongFormat=False, nonWorkDay=False,
          multiCurrency=False, moreData=False):
    """
    MFB arfolyam pooler test cases.

    This method is intended to test the MFB arfolyam pooler method.
    Keep in mind that if any parameters are true (except moreData
    and multiCurrency) the function will raise and exception.
    If the function is called without parameters it will not do anything.

    Input parameters:
        wrongFormat: will query badly formated dates
        nonWorkDay: will query a Hungarian holiday
        multiCurrency: will query USD, not the default EUR
        moreData: will add 6 more dates to the query
    """
    dates = []
    print("Running tests with arguments:")
    print("wrong format tester: {}".format(wrongFormat))
    print("non work day tester: {}".format(nonWorkDay))
    print("multi currency tester: {}".format(multiCurrency))
    print("more data added: {}".format(moreData))

    if moreData:
        dates = ["2018.01.22.", "2018.02.20.", "2018.03.20.", "2018.04.20.",
                 "2018.05.22.", "2018.06.20."]

    if wrongFormat:
        dates.append("2012-11-11")

    if nonWorkDay:
        dates.append("2018.01.20")

    if multiCurrency:
        for date in dates:
            print(date + ": ", MNBArfolyam(date, "USD"))
            sleep(1)
    else:
        for date in dates:
            print(date + ": ", MNBArfolyam(date))
            sleep(1)
    print("tests concluded")


"""
tests()
try:
    tests(wrongFormat=True)
except ValueError as e:
    print(e)
tests(multiCurrency=True)
try:
    tests(nonWorkDay=True)
except ValueError as e:
    print(e)
tests(moreData=True)
try:
    tests(wrongFormat=True, multiCurrency=True, nonWorkDay=True, moreData=True)
except ValueError as e:
    print(e)
"""


# change this date to run script
date = "2018.07.20."

print(MNBArfolyam(date))
