#Test script to read PostgreSQL data into Python

import psycopg2

#Test connection to PostgreSQL, returns PostgreSQL version if connection is estabilished
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname=Amazon user=postgres password=data")

        # create a cursor
        cur = conn.cursor()

 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_book_details():
    """ query data from the Keepa table """
    conn = None
    try:
        conn = psycopg2.connect("dbname=Amazon user=postgres password=data")
        cur = conn.cursor()
        cur.execute("SELECT * FROM public.keepa LIMIT 1")
        print("The number of books: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    connect()
    get_book_details()
