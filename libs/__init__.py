from redis import Redis

rd = Redis(host='121.199.63.71',
           port=6372, db=1)
if __name__ == '__main__':
    r = rd.keys()
    print(r)
