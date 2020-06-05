from xCore import xCore
from xSL01 import xSL01

SL01 = xSL01()

while True:
    print(SL01.getUVA())
    print(SL01.getUVB())
    print(SL01.getUVIndex())
    print(SL01.getLUX())
    xCore.sleep(1000)