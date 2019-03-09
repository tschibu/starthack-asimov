import cv2
import helper.log_helper as logger
import numpy as np
import os

class Drawer:
    def __init__(self, angle_impact, max_force, damage_id, crash_time, max_force_offset=None):
        self.log = logger.get(True, "Drawer")
        self.image = cv2.imread("images/car_big.png")
        self.image_grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.damage_id = damage_id
        self.crash_time = crash_time
        self.x = 1300
        self.y = 550
        self.max_force = max_force
        self.angle_impact = angle_impact
        self.off_set_in_milliseconds = max_force_offset

        self.image_path = "images/car_rendered_at_" + str(self.off_set_in_milliseconds) + "_ms.png"
        self.log.info(
            "Param x=" + str(self.x) + "; y=" + str(self.y) + "; radius=" + str(self.max_force) + "; angle=" + str(
                self.angle_impact))
        self.log.debug("Image-shape = " + str(self.image.shape))

    def __cut_car(self):
        ret, thresh = cv2.threshold(self.image_grey, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.image, contours, 1, (0, 255, 0), 2)

    def __draw(self):
        if self.off_set_in_milliseconds is not None:
            self.__add_text(self.off_set_in_milliseconds)

        self.__cut_car()

        # add arrow and circle
        self.__draw_arrow()
        self.__draw_circle()

    def __draw_arrow(self):
        # TODO: calculate source from angle

        cv2.arrowedLine(self.image, (1457, 1208), (self.x, self.y), (0, 0, 255), 4)

    def __draw_circle(self):
        radius = self.__dynamic_damage_calc(self.max_force)
        cv2.circle(self.image, (self.x, self.y), radius, (0, 0, 255), 2)
        self.log.debug("radius=" + str(radius))
        cv2.circle(self.image, (self.x, self.y), 5, (0, 0, 0), -1)

    def __add_text(self, off_set_in_milliseconds):
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottom_left_corner_of_text = (10, 50)
        font_scale = 1
        font_color = (0, 0, 0)
        line_type = 2

        cv2.putText(self.image, "Rendered crash image after " + str(off_set_in_milliseconds) + "[ms]",
                    bottom_left_corner_of_text,
                    font,
                    font_scale,
                    font_color,
                    line_type)
        self.log.info("add off_set=" + str(off_set_in_milliseconds) + " to the image.")

        bottom_left_corner_of_text = (10, 100)
        cv2.putText(self.image, "crash identifier = " + str(self.damage_id) + " - damage time = " + str(self.crash_time),
                    bottom_left_corner_of_text,
                    font,
                    font_scale,
                    font_color,
                    line_type)
        self.log.info("crash identifier = " + str(self.damage_id) + " - damage time = " + str(self.crash_time))

    def __dynamic_damage_calc(self, damage):
        max_damage = 60000
        min_damage = 8000

        if damage >= max_damage:
            damage = max_damage - 1

        if damage <= min_damage:
            damage = min_damage

        return int((damage / max_damage) * 150)

    def __write_image(self):
        cv2.imwrite(self.image_path, self.image)

    def get_image(self):
        """Retrun a image with the a circle and an arrow.
        """
        self.__draw()
        self.__write_image()
        return self.image_path

    def remove_image(self):
        os.remove(self.image_path)

    def show_image(self):
        """show the image with the right circle and arrow with opencv.

        """
        self.__draw()
        window_name = "CrashImage"
        cv2.namedWindow(window_name)
        cv2.moveWindow(window_name, 666, 123)

        cv2.imshow(window_name, self.image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    drawer = Drawer(132.19008793270834, 21380.161292511744, 35, "2018-12-25 10:47:39", 5339896)
    drawer.show_image()
    #print(drawer.get_image())
    # drawer.remove_image()

