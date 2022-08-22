import os
import sys
import glob
import shutil
import click

accessable_path = 'D:\\同期\\vcyo'

def window(path):
    if not accessable_path in path:
        print("\n>>Cannot access this directory. try other directory path")
        sys.exit()
    elif not os.path.exists(path):
        print("\n>>Image file path is different. try again")
        sys.exit()

    success = convert(path)
    if not success:
        print(">>There are no png image files.")
    else:
        print(">>WELL DONE!!")

def convert(path):
    if path[-1] == '\\':
        path = path[:-1]

    png_images = []
    png_images = glob.glob(path + '\\*png')
    print(png_images)

    if png_images == []:
        return False

    for file in png_images:
        dirname = os.path.dirname(file) # ディレクトリ名
        basename_ext = os.path.basename(file) # ファイル名.拡張子
        basename, _ = os.path.splitext(basename_ext) # ファイル名, .拡張子

        to_path = dirname + '\\' + basename + '.jpg'

        shutil.copyfile(file, to_path)
        os.remove(file)
    
    return True
    

@click.command()
@click.argument('path', nargs=1)
def main(path):
    window(path)
    
if __name__ == '__main__':
    main()