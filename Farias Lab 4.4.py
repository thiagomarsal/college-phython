# IT 280 – Lab #7: IT 280 – Lab #7: Link Verification Lab Instructions

import re
import bs4
import requests
import validators


def checkStatus(res):
    if res.ok:
        print('[' + str(res.status_code) + ' - Good] -', res.url)
    else:
        print('[' + str(res.status_code) + ' - Broken] -', res.url)


def openUrl(url):
    res = requests.get(url)
    checkStatus(res)
    return res


def checkUrl(links):
    try:
        for url in links:
            res = requests.options(url)
            checkStatus(res)
    except BaseException as e:
        # FIXME: Find out how to avoid: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
        print(str(e))


def extractUrl(html):
    links = []
    for link in html.findAll('a', attrs={'href': re.compile("^http.*://")}):
        url = link.get('href')
        if validators.url(url):
            links.append(url)
    return links


def main():
    url = input("Please, inform and URL to check for broken links: ")
    if validators.url(url):
        res = openUrl(url)
        html = bs4.BeautifulSoup(res.text, 'html.parser')
        links = extractUrl(html)
        checkUrl(links)
    else:
        print('URL informed is invalid: ' + url)


main()