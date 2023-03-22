#!/usr/bin/env python

import pyfiglet
import requests as requests

ascii_banner = pyfiglet.figlet_format("Covid Report", "big")
print(ascii_banner)


def printGlobalSummary(response):
    globalSummary = response['Global']
    print("Global Summary")
    print("\t Date=", globalSummary['Date'])
    print("\t NewConfirmed=", globalSummary['NewConfirmed'])
    print("\t TotalConfirmed=", globalSummary['TotalConfirmed'])
    print("\t NewDeaths=", globalSummary['NewDeaths'])
    print("\t TotalDeaths=", globalSummary['TotalDeaths'])
    print("\t NewRecovered=", globalSummary['NewRecovered'])
    print("\t TotalRecovered=", globalSummary['TotalRecovered'])


def printCountrySummary(response):
    for country_info in response['Countries']:
        print(country_info['Country'])
        print("\t NewConfirmed=", country_info['NewConfirmed'])
        print("\t TotalConfirmed=", country_info['TotalConfirmed'])
        print("\t NewDeaths=", country_info['NewDeaths'])
        print("\t TotalDeaths=", country_info['TotalDeaths'])
        print("\t NewRecovered=", country_info['NewRecovered'])
        print("\t TotalRecovered=", country_info['TotalRecovered'])


try:
    print("Covid-19 Report per Country")
    response = requests.get("https://api.covid19api.com/summary").json()
    printGlobalSummary(response)
    printCountrySummary(response)
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
