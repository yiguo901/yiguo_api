from redis import Redis

rd = Redis(host='localhost',
           port=6372, db=1)
if __name__ == '__main__':
    r = rd.keys()
    print(r)