from output import to_textfile
from db import save_data

def test_save_to_textfile(data):
    for el in data:
        to_textfile('all_tbody.txt', '{} [{}] | {} {} {}\n'.format(
            el['bank'],
            el['money'],
            el['currency'],
            el['buy'],
            el['sale'],
        ))
    # to_textfile('all_tbody.txt', '{}'.format(data))

def test_save_to_db():
    data = []
    data.append({
        'bank': 'bank name cxc Аль',
        'money': 'наличные',
        'currency': 'RUR',
        'buy': 350,
        'sale': 349
        })
    data.append({
        'bank': 'bank name cxc Аль',
        'money': 'наличные',
        'currency': 'RUR',
        'buy': 353,
        'sale': 349
    })
    save_data(data)