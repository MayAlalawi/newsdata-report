#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def execute_query(query):
    """ Set the connection to the database and execute the query passed
    in query parameter"""
    try:
        db = psycopg2.connect('dbname=' + DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except psycopg2.Error as e:
        print "Unable to connect!"
        print e.pgerror
        print e.diag.message_detail
        sys.exit(1)
    else:
        print "Connected!"


def top_articles_views():
    ''' rreturn sorted list with the most popular article at the top'''
    '''Build top articles views query'''
    query1 = """
         select title, count(*) as views
         from articles, log
         where '/article/' || articles.slug = log.path
         group by(title)
         order by(views) desc
         limit 3;
         """
    ''' Run The Query'''
    articles_list = execute_query(query1)
    # print information from results
    print('\nTOP THREE  MOST POPULAR ARTICLES OF ALL TIME:')
    counter = 1
    for row in articles_list:
        print(
            str(counter) + ": " + str(row[0]) + "\t" + str(row[1]) + " views"
            )
        counter += 1
    print


def get_poupular_authors():
    ''' print sorted list of the most popular authors and their views. '''
    query2 = """
        select authors.name, sum(authorviews.views)as total
        from authors join authorviews
        on authorviews.author= authors.id
        group by(authors.name)
        order by(total) desc;
        """
    authors_list = execute_query(query2)
    print('\nTHE TOP MOST POPULAR ARTICLE AUTHOES OF ALL TIME:')
    counter = 1
    for row in authors_list:
        print(
            str(counter) + ": " + format(row[0], '<25') +
            format(row[1], '>6') + " views"
        )
        counter += 1
    print


def get_days_error():
    ''' rreturn which days did more than 1% of requests lead to errors'''
    query3 = """
        select to_char(dayerrors.date, 'FMMonth FMDD, YYYY') as date,
        round( cast(float8((errors /cast(requests as float))*100)
        as numeric),1)as percentage
        from dayerrors join dayrequests
        on dayerrors.date = dayrequests.date
        where round( cast(float8((errors /cast(requests as float))*100)
        as numeric),1)> 1;
        """
    error_day = execute_query(query3)
    print('\nTHE DAYS THAT HAVE MORE THAN 1% OF REQUESTS LEAD TO ERRORS:')
    # print information from authors_list
    counter = 1
    for row in error_day:
        print(str(counter) + ": " + str(row[0]) + "\t" + str(row[1]) +
              "% errors")
        counter += 1
    print


if __name__ == '__main__':
    print('\nGetting The Report informations...\n')
    top_articles_views()
    get_poupular_authors()
    get_days_error()
