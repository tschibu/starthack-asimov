import cv2
import helper.log_helper as logger
import numpy as np
import os
import math
import shutil


class DamageImage:
    def __init__(self, angle_impact, max_force, damage_id, crash_time, max_force_offset=None):
        self.log = logger.get(False, "DamageImage")
        self.image = cv2.imread("images/car_big.png")
        self.image_grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.damage_id = damage_id
        self.crash_time = crash_time
        self.null_point_x = 655
        self.null_point_y = 582
        self.car_point_x = 0
        self.car_point_y = 0
        self.x = 0
        self.y = 0
        self.max_force = max_force
        self.angle_impact = angle_impact
        self.off_set_in_milliseconds = max_force_offset

        self.image_rendered_path = "images_rendered/"
        self.image_rendered_file = str(damage_id) + "_car_rendered_at_" + str(self.off_set_in_milliseconds) + "ms.png"

    def __cut_car(self):
        length = 1000
        self.y = int(round(self.null_point_y + length * np.sin(self.angle_impact * np.pi / 180.0)))
        self.x = int(round(self.null_point_x + length * np.cos(self.angle_impact * np.pi / 180.0)))

        ret, thresh = cv2.threshold(self.image_grey, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(self.image, contours, 1, (0, 255, 0), 2)

        # Create mask where white is what we want, black otherwise
        mask = np.zeros_like(self.image)

        # Draw filled contour in mask
        cv2.drawContours(mask, contours, 1, 255, -1)

        # Extract out the object and place into output image
        out = np.zeros_like(self.image)
        out[mask == 255] = self.image[mask == 255]

        blank_image_line = np.zeros(self.image.shape, np.uint8)

        x = int(1500*np.cos(math.radians(self.angle_impact+180))) + self.null_point_x
        y = int(1500*np.sin(math.radians(self.angle_impact+180))) + self.null_point_y

        cv2.line(blank_image_line, (self.null_point_x, self.null_point_y), (self.x, self.y), (0, 0, 255), 2)

        blank_image_contour = np.zeros(self.image.shape, np.uint8)

        cv2.drawContours(blank_image_contour, contours, 1, (255, 255,  255), 2)
        cv2.drawContours(mask, contours, 1, (0, 0, 0), 1)

        one_point = cv2.bitwise_and(blank_image_line, blank_image_contour)

        self.car_point_x = np.nonzero(one_point)[1][0]
        self.car_point_y = np.nonzero(one_point)[0][0]

    def __draw(self):
        # add arrow and circle
        self.__cut_car()

        self.__draw_arrow()
        self.__draw_circle()

        if self.off_set_in_milliseconds is not None:
            self.__add_text(self.off_set_in_milliseconds)


    def __draw_arrow(self):
        cv2.circle(self.image, (self.null_point_x, self.null_point_y), 35, (91, 187, 155), -1) # Nullpunkt
        cv2.arrowedLine(self.image, (self.x, self.y), (self.car_point_x, self.car_point_y), (0, 0, 255), 4)

    def __draw_circle(self):
        radius = self.__dynamic_damage_calc(self.max_force)
        cv2.circle(self.image, (self.car_point_x, self.car_point_y), radius, (0, 0, 255), 2)
        cv2.circle(self.image, (self.car_point_x, self.car_point_y), 10, (91, 187, 155), -1)

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

        bottom_left_corner_of_text = (10, 100)
        cv2.putText(self.image, "crash identifier = " + str(self.damage_id) + " - damage time = " + str(self.crash_time),
                    bottom_left_corner_of_text,
                    font,
                    font_scale,
                    font_color,
                    line_type)

    def __dynamic_damage_calc(self, damage):
        """
        create the radius for the damage value.
        """
        max_damage = 15
        min_damage = 2

        if damage >= max_damage:
            damage = max_damage - 1

        if damage <= min_damage:
            damage = min_damage

        return int((damage / max_damage) * 300)

    def __write_image(self):
        """
        write the generated image to the rendered file folder.
        """
        cv2.imwrite("images/"+self.image_rendered_file, self.image)

    def get_image(self):
        """
        Retrun a image with the a circle and an arrow.
        """
        self.__draw()
        self.__write_image()
        return "images/"+self.image_rendered_file

    def remove_all_rendered_image(self):
        """
        delete all rendered files on the system.
        """
        files_rendered = os.listdir(self.image_rendered_path)

        shutil.rmtree(self.image_rendered_path, ignore_errors=True)

    def show_image(self):
        """
        show the image with the right circle and arrow with opencv.
        """
        self.__draw()
        window_name = "CrashImage"
        cv2.namedWindow(window_name)
        cv2.moveWindow(window_name, 666, 123)

        cv2.imshow(window_name, self.image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
