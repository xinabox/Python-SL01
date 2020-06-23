[![GitHub Issues](https://img.shields.io/github/issues/xinabox/Python-SL01.svg)](https://github.com/xinabox/Python-SL01/issues)
![GitHub Commit](https://img.shields.io/github/last-commit/xinabox/Python-SL01)
![Maintained](https://img.shields.io/maintenance/yes/2020)
![Build status badge](https://github.com/xinabox/Python-SL01/workflows/Python/badge.svg)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Python-SL01

The SL01 xChip is a UV radiation and ambient light level sensor. It is based on the VEML6075 and TSL4531. VEML6075 on the SL01 is capable of measuring UVA and UVB radiation, in turn, providing an acccurate UV Index. TSL4531 is a light sensor that is capable of measuring the luminosity (Wide Dynamic Range — 3 lux to 220k lux) (visual brightness).

# Usage

## Mu-editor
Download [Mu-editor](https://github.com/xinabox/mu-editor/releases/tag/v1.1.0a2)

### CW01 and CW02
- Use [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest) and flash MicroPython to the CW01/CW02.
- Download Python packages from the REPL with the following code:
    ```python
    import network
    import upip
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("ssid", "password")
    upip.install("xinabox-SL01")
    ```

### CC03, CS11 and CW03
- Download the .UF2 file for CC03/CS11/CW03 [CircuitPython](https://circuitpython.org/board/xinabox_cs11/) and flash it to the board.
- TO DO

### MicroBit
- TO DO

## Raspberry Pi

Requires Python 3
```
pip3 install xinabox-SL01
```

# Example
```python
from xCore import xCore
from xSL01 import xSL01

SL01 = xSL01()

while True:
    print(SL01.getUVA())
    print(SL01.getUVB())
    print(SL01.getUVIndex())
    print(SL01.getLUX())
    xCore.sleep(1000)
```
