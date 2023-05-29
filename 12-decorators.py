import time

def ikiye_katla (func):
    def wrapper (x,y):
        start=time.time()
        func(x*2,y*2)
        print(time.time()-start)
    return wrapper


@ikiye_katla
def topla (x,y):
    print(x+y)
    time.sleep(2)

topla(5,10)

