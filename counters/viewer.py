import redis
import click
import time
import random

PAGES = ["/home", "/post/1", "/post/2", "/post/3"]
REGIONS = ["US", "EU", "MiddleEast", "China"]


@click.command()
@click.option('--host', default="localhost", help='redis host.')
@click.option('--port', type=click.INT, default=6379, help='redis port.')
def main(host, port):
    r = redis.Redis(host=host, port=port)

    while True:
        page = random.choice(PAGES)
        region = random.choice(REGIONS)
        r.execute_command('TS.INCRBY', 'view:%s:%s' % (page, region), 1, 
                          'LABELS',
                          'page', page,
                          'region', region,
                          '__name__', 'page_views'
                          )


if __name__ == '__main__':
    main()
