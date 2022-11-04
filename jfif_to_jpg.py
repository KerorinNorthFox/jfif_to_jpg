import os
import sys
import glob
import shutil
import click

accessible_path = ''


def window(path: str):
    if accessible_path not in path:
        print("\n>>Cannot access the directory " + path + ". Try using another directory path")
        sys.exit()
    elif not os.path.exists(path):
        print("\n>>Image file path is different. try again")
        sys.exit()

    success: bool = convert(path)
    if not success:
        print(">>There are no jfif image files in the directory.")
    else:
        print(">>Complete!")


def convert(path: str) -> bool:
    if path[-1] == '\\':
        path = path[:-1]

    jfif_images: list[str] = glob.glob(path + '\\*jfif')

    if not jfif_images:
        return False

    for file in jfif_images:
        dirname = os.path.dirname(file)  # ディレクトリ名
        basename_ext = os.path.basename(file)  # ファイル名.拡張子
        basename, _ = os.path.splitext(basename_ext)  # ファイル名, .拡張子

        to_path = dirname + '\\' + basename + '.jpg'

        shutil.copyfile(file, to_path)
        os.remove(file)
        print('Fixed ' + basename + basename_ext)
    return True


@click.command()
@click.argument('path', nargs=1)
def main(path):
    window(path)


if __name__ == '__main__':
    main()
