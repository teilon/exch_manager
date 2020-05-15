import postgresql
from config import db_config


def save_to_db(conn, el):
    bank = el['bank']
    money = el['money']
    currency = el['currency']
    buy = el['buy']
    sale = el['sale']

    # bank
    conn.execute("INSERT INTO bank (name) "
                "SELECT '{name}' "
                "WHERE "
                 "NOT EXISTS ("
                  "SELECT name FROM bank WHERE name = '{name}'"
                 ");"
                 .format(name=bank)
                 )
    # currency
    conn.execute("INSERT INTO currency (name) "
                "SELECT '{name}' "
                "WHERE "
                 "NOT EXISTS ("
                 " SELECT name FROM currency WHERE name = '{name}'"
                 ");"
                .format(name=currency)
                 )
    # money
    conn.execute("INSERT INTO money_type (name) "
                 "SELECT '{name}' "
                 "WHERE "
                 "NOT EXISTS ("
                 " SELECT name FROM money_type WHERE name = '{name}'"
                 ");"
                 .format(name=money)
                 )
    saturday
    conn.execute("INSERT INTO saturday (bank_id, money_id, currency_id, buy, sale) "
                 "SELECT "
                 "(select id FROM bank WHERE name='{bank}'), "
                 "(select id FROM money_type WHERE name='{money}'), "
                 "(select id FROM currency WHERE name='{currency}'), "
                 "{buy}, "
                 "{sale};"
                .format(bank=bank,money=money,currency=currency,buy=buy,sale=sale)
                 )


def save_data(data):
    with postgresql.open(db_config()) as conn:
        for el in data:
            save_to_db(conn, el)
        # conn.commit()