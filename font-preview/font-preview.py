from PIL import Image, ImageDraw, ImageFont
import fontconfig
import ntpath


# # HEBREW LETTER ALEF U + 05

def find_fonts(c):
    """Finds fonts containing  the (Unicode) character c."""
    fonts = fontconfig.query()
    for path in sorted(fonts):
        font = fontconfig.FcFont(path)
        if font.has_char(c):
            yield path


def generate_text(text='אבגדהוזחטיכלמנסעפצקרשת', font_size=40):
    search = 'א'
    char = search.decode('utf-8') if isinstance(search, bytes) else search

    for i, font in enumerate(find_fonts(char)):
        fnt = ImageFont.truetype(font, font_size)
        print(font)
        img = Image.new('RGB', (700, 50), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        sentence = text
        offset_xy = (2, 2)
        d.text(offset_xy, sentence[::-1], font=fnt, fill=(0, 0, 0))
        img.save(str(i) + "-" + ntpath.basename(font)[:-4] + '.png')


if __name__ == '__main__':
    generate_text()
