"""
多现场生成图片的缩略图

Version: 0.1
Author:鲁成

"""
import os
import glob
import threading

from PIL import Image

PREFIX = 'thumbnails'

def generate_thumbnail(infile, size):
    """生成缩略图"""
    filename, ext = os.path.splitext(infile)
    filename = filename[filename.rfind('/') + 1:]
    outfilename = f'{PREFIX}/{filename}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfilename, 'PNG')
    

def main():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('images/*.png'):
        for size in (32, 64, 128):
            thumbnail_thread = threading.Thread(target=generate_thumbnail, args=(infile, (size, size)))
            thumbnail_thread.start()


if __name__ == '__main__':
    main()
