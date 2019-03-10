import numpy as np
import base64
import json

from helper import log_helper
#Definde Logger without Filehandle
logger = log_helper.get(False, "Data Parse")



class DataParser:
    def calculate_damage(self, data_array):
        """Berechnet den schaden und gibt den Winkel, relativ zur Auto Mitte zurück, wo der Impact war.
        
        Arguments:
            data_array {[type]} -- Vorbearbeitet Liste mit Virtuellen x,y,z Werten
            offset_milliseconds -- Optional, zur Crash Image generierung zu einer spezifischen Zeit
        
        Returns:
            Crash_data -- JSON { “impactAngle”: degrees, “offsetMaximumForce”:millisecond }
        """
        if(offset_milliseconds != False):
            ##Do Image calculation (pass to remo)

        return crash_data_json

    def calculate_crash_image(self, data_array, offset_milliseconds):
        crash_data = self.calculate_damage()

        ##pass crash_data to image calculation
        ##pass, angle, forces, offset

        return crash_img

        