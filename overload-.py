class Time:
    def __init__(self, hour, min, sec):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def __add__(self, other):
        t1 = self.__hour*60*60 + self.__min*60 + self.__sec
        t2 = other.__hour*60*60 + other.__min*60 + other.__sec
        t = t1+t2
        h = t//(60*60)
        t = t-h*60*60
        m = t//60
        s = t-m*60
        print(h, " hours ", m, " minutes ",s," seconds ")

t1 = Time(1,1,30)
t2 = Time(4,1,30)
t1+t2