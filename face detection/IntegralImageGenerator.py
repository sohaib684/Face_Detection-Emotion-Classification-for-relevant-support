import numpy as np

class IntegralImageGenerator :

    #def __init__(self):
    #    self.integral_image = self.generate_integral_image()

    def generate_integral_image(self, image):
        height, width = image.shape
        integral_image = np.zeros((height, width), dtype=np.int32)
        integral_image[0, 0] = self.image[0, 0]
        for i in range(1, height):
            integral_image[i, 0] = integral_image[i - 1, 0] + self.image[i, 0]
        for j in range(1, width):
            integral_image[0, j] = integral_image[0, j - 1] + self.image[0, j]
        for i in range(1, height):
            for j in range(1, width):
                integral_image[i, j] = integral_image[i - 1, j] + integral_image[i, j - 1] - integral_image[i - 1, j - 1] + self.image[i, j]
        return integral_image

    def get_sum(self, x, y, w, h):
        x1 = x
        y1 = y
        x2 = x + w - 1
        y2 = y + h - 1
        sum = self.integral_image[y2, x2]
        if x1 > 0:
            sum -= self.integral_image[y2, x1 - 1]
        if y1 > 0:
            sum -= self.integral_image[y1 - 1, x2]
        if x1 > 0 and y1 > 0:
            sum += self.integral_image[y1 - 1, x1 - 1]
        return sum