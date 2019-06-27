from redis import Redis

rd = Redis(host='localhost',
           port=6379, db=3)

if __name__ == '__main__':
    print(rd.keys("*"))
    rd.flushall()