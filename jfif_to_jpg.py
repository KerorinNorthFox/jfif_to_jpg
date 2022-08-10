import os
import sys
import glob
import shutil
import click

accessable_path = 'D:\\同期\\vcyo'

@click.command()
@click.argument('path', nargs=1)
def main(path):
    if not accessable_path in path:
        print("\n>>Cannot access this directory. try other directory path")
        sys.exit()
    elif not os.path.exists(path):
        print("\n>>Image file path is different. try again")
        sys.exit()

    if path[-1] == '\\':
        path = path[:-1]

    jfif_images = []
    jfif_images = glob.glob(path + '\\*jfif')
    print(jfif_images)

    for file in jfif_images:
        dirname = os.path.dirname(file) # ディレクトリ名
        basename_ext = os.path.basename(file) # ファイル名.拡張子
        basename, _ = os.path.splitext(basename_ext) # ファイル名, .拡張子

        to_path = dirname + '\\' + basename + '.jpg'

        shutil.copyfile(file, to_path)
        os.remove(file)

    print(">>WELL DONE!!")

if __name__ == '__main__':
    main()