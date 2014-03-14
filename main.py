# -*- coding: utf-8 -*-
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import string


class code:

    def main(self):
        letter_list = [x for x in string.letters]
        letter_list.extend([x for x in string.punctuation])
        det_list = []
        true_type_font = "Courier_New.ttf"
        for each in letter_list:
            letter_picture = self.letter_image(each, true_type_font)
            proportion = self.prop(letter_picture[0], letter_picture[1], each)
            det_list.append(proportion)
        sorted_by_second = sorted(det_list, key=lambda tup: tup[1])
        sorted_by_second.reverse()
        f = open('proportions.txt', 'w')
        for each in sorted_by_second:
            data = "{}: {}\n".format(each[0], each[1])
            f.write(data)
        f.close()

    def letter_image(self, letter, true_type_font):
        font = ImageFont.truetype(true_type_font, 14)
        img = Image.new("RGBA", (18, 18), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), letter, (0, 0, 0), font=font)
        draw = ImageDraw.Draw(img)
        amg = img.load()
        return (amg, img)

    def prop(self, amg, im, letter):
        width, height = im.size[0], im.size[1]
        total = width * height
        non_white = 0
        i, c, x, y = 0, 0, 0, 0
        while i < total:
            if x == width:
                y += 1
                x = 0
            colour = amg[x, y]
            colours = list(colour)
            for each in colours:
                if each == 255:
                    pass
                else:
                    non_white += 1
                    break
            x += 1
            i += 1
        frac = (float(float(non_white) / float(total))) * 100
        detail = (letter, frac)
        return detail

if __name__ == "__main__":
    code().main()
