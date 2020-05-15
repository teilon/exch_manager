from bs4 import BeautifulSoup
import requests
from db import save_data
from test import test_save_to_textfile
from datetime import datetime

def start_parse():
    host = 'https://bai.kz'
    url = '{}/kursy/almaty/'.format(host)
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')
    banks = soup.find('div', class_='subsection').\
        find('table', class_='banks_table')
    tbody = banks.find_all('tr')

    data = []
    for tag in tbody[2:]:
        bank_name = tag.find('div', class_="t_bank_name")
        bank_name = None if bank_name is None else bank_name.text.strip()
        if bank_name is None:
            br = tag.find('br')
            if br is not None:
                bank_name = br.previous_sibling.strip()
            else:
                bank_name = ''

        bank_dir = tag.find('td', class_="bank_dir_table")
        if bank_dir is not None:
            money_type = bank_dir.find('tr', class_="rate-result")
            money_type = '' if money_type is None else money_type.find('strong').text.strip()

            trs = bank_dir.find_all('tr')
            for tr in trs[1:]:
                tds = tr.find_all('td')
                buy = tds[0].text.strip()
                currency_name = tds[1].text.strip()
                sale = tds[2].text.strip()
                sale = 0 if sale == '-' else sale
                bank_data = {
                    'bank': bank_name,
                    'money': money_type,
                    'currency': currency_name,
                    'buy': buy,
                    'sale': sale
                }
                data.append(bank_data)

    # save_to_textfile(data)

    start = datetime.now()
    print(start)
    save_data(data)
    end = datetime.now()
    print('save timer - {}'.format(end - start))


def get_html(url, useragent=None, proxy=None):
    r = requests.get(url, headers=useragent, proxies=proxy, verify=False)
    return r.text
