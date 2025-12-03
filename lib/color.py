from lib.progress import Progress
from lib.easing import no_easing
from lib.util import maximum,minimum

class TransferColor:
    def __init__(self,red:int,green:int,blue:int,target_red:int,target_green:int,target_blue:int) -> None:
        self.__r = red
        self.__g = green
        self.__b = blue
        self.__tr = target_red
        self.__tg = target_green
        self.__tb = target_blue
    def get(self,normalize:float,easeing=no_easing):
        vr = self.__tr - self.__r
        vg = self.__tg - self.__g
        vb = self.__tb - self.__b
        rr = self.__r + easeing(normalize) * vr
        rg = self.__g + easeing(normalize) * vg
        rb = self.__b + easeing(normalize) * vb
        return (minimum(maximum(rr,255),0),minimum(maximum(rg,255),0),minimum(maximum(rb,255),0))

