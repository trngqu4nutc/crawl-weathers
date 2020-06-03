import mysql.connector as mysql
from mysql.connector import Error


def connection():
    try:
        connect = mysql.connect(
            host='localhost',
            user='root',
            password='2110',
            database='crawl-weathers'
        )
        if connect.is_connected():
            return connect
    except Error as e:
        print(e)


def insertWeathers(data, date):
    d = []
    for item in data:
        item['day'] = (item['day'][:-10] + ' (' + item['day'][-10:] + ')').replace('/', '-')
        d.append(
            (date, item['day'], item['img'], item['desc'], item['celsius'], item['high'], item['low'],
             item['updated']))
    print(d)
    conn = connection()
    cursor = conn.cursor()
    sql = 'insert into weathers(`date`,`day`,`img`,`desc`, `celsius`,`high`,`low`,`updated`) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.executemany(sql, d)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insertDayDetails(data):
    conn = connection()
    cursor = conn.cursor()
    sql = 'insert into daydetails(`date`,`day`,`img`,`desc`,`celsius`,`high`,`low`,`updated`) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
        cursor.execute(sql, data)
        conn.commit()
        return True
    except Error as e:
        return False
        print(e)
    finally:
        cursor.close()
        conn.close()


def checkDateExists(data):
    conn = connection()
    cursor = conn.cursor()
    sql = 'select count(*) from weathers where date=%s'
    cursor.execute(sql, [data])
    count = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()
    return count


def findByDate(data):
    conn = connection()
    cursor = conn.cursor()
    sql = 'select `day`, `img`, `desc`, `celsius`, `high`, `low`, `updated` from weathers where date=%s'
    cursor.execute(sql, [data])
    d = []
    for item in cursor.fetchall():
        d.append({'day': item[0], 'img': item[1], 'desc': item[2], 'celsius': item[3], 'high': item[4], 'low': item[5],
                  'updated': item[6]})
    cursor.close()
    conn.close()
    return d


def findDetailsByDate(date):
    conn = connection()
    cursor = conn.cursor()
    sql = 'select `day`, `img`, `desc`, `celsius`, `high`, `low`, `updated` from daydetails where date=%s'
    cursor.execute(sql, [date])
    d = []
    for item in cursor.fetchall():
        d.append(
            {'day': item[0], 'img': (item[1][:4] + ' width="100" ' + item[1][5:]), 'desc': item[2], 'celsius': item[3],
             'high': item[4], 'low': item[5],
             'updated': item[6]})
    cursor.close()
    conn.close()
    return d
