import os.path
import random

from PIL import Image, ImageFilter, ImageFont, ImageDraw


def get_target_image_dir(image_filename=None):
    target_file = os.path.join(".", "image")
    target_file = os.path.join(target_file, image_filename)
    return target_file


def generate_verification_code_image():
    # 生成随机颜色

    # 图片验证码尺寸
    width = 50 * 4
    height = 50
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # font 字体对象
    font = ImageFont.truetype('Arial.ttf', 36)

    # draw 对象
    draw = ImageDraw.Draw(image)

    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color1())
    # 输出文字
    for t in range(4):
        draw.text((50 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())

    # image = image.filter(ImageFilter.BLUR)
    image.save(get_target_image_dir('code.jpg'), 'jpeg')


# 随机字母:
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色1
def rnd_color1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def pic_thumbnail():
    im = Image.open('image/original.jpg')
    print('')
    w, h = im.size
    print('Original Image size: width --> {}, height --> {}'.format(w, h))
    new_pic = im.thumbnail((w // 2, h // 2))
    print('Resize Image size: width --> {}, height --> {}'.format(w // 2, h // 2))
    new_pic.save(get_target_image_dir('thumbnail.jpg'), 'jpeg')


def pic_filter():
    img = Image.open('image/original.jpg')
    new_pic = img.filter(ImageFilter.BLUR)
    new_pic.save(get_target_image_dir('filtered.jpg'), 'jpeg')


if __name__ == '__main__':
    # 获取 .py 文件执行的当前路径，确认要加载图片的存放路径
    print('pwd --> ', os.path.abspath(__file__))
    # 图片缩放
    # pic_thumbnail()

    # 模糊滤镜
    # pic_filter()

    # 生成字母验证码图片
    generate_verification_code_image()
