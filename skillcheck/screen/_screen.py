import logging as log

import mss


class Screen:
    """Screen class for monitor/screenshot handling"""

    def __init__(self, number=1):
        self.sct = mss.mss()
        self.number = number
        self.info = self.sct.monitors[number]
        if self.info['height'] != 1080:
            log.error("Unsupported monitor resolution! (Supports only 1080p)")
            raise ("UnsupportedScreenResolution")
        if self.info['width'] == 1920:
            self.type = "WIDE"
        elif self.info['width'] == 2560:
            self.type = "ULTRA"
        else:
            log.error("Unsupported monitor type! (Supports only widescreen/ultrawide")
            raise ("UnsupportedScreenType")

    def shot(self, top: int, left: int, width: int, height: int):
        """Returns screenshot of selected area"""
        return self.sct.grab({
            "top": self.info["top"] + top,
            "left": self.info["left"] + left,
            "width": width,
            "height": height,
            "mon": self.number
        })
