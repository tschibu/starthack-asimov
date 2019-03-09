import cv2
import helper.log_helper as logger

class Drawer:
    def __init__(self, x, y, radius, angle, off_set_in_milliseconds=None):
        self.image = cv2.imread("image/car_big.png")
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.off_set_in_milliseconds = off_set_in_milliseconds
        self.log = logger.get(True, "Drawer")
        self.log.info(
            "Param x=" + str(self.x) + "; y=" + str(self.y) + "; radius=" + str(self.radius) + "; angle=" + str(
                self.angle))
        self.log.debug("Image-shape = " + str(self.image.shape))

    def __draw(self):
        if self.off_set_in_milliseconds is not None:
            self.__add_text(123)

    def __draw_arrow(self):
        cv2.arrowedLine(self.image, (1457, 652), (self.x, self.y), (0, 0, 255), 4)

    def __draw_circle(self):
        cv2.circle(self.image, (self.x, self.y), self.radius, (0, 0, 255), 2)

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
        self.log.info("add off_set" + str(off_set_in_milliseconds))

    def get_image(self):
        """Retrun a image with the a circle and an arrow.
        """
        self.__draw()

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
    drawer = Drawer(1300, 550, 60, 180)
    drawer.show_image()
