from redis import Redis

rd = Redis(host='121.199.63.71',
           port=6372, db=3)

if __name__ == '__main__':
    print(rd.keys("*"))
    rd.flushall()