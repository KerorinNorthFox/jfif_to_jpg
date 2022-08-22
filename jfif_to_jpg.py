import os
import sys
import glob
import shutil
import click

accessable_path = 'D:\\同期\\vcyo'

def window(path, ext_from, ext_to):
    if not accessable_path in path:
        print("\n>>Cannot access this directory. try other directory path")
        sys.exit()
    elif not os.path.exists(path):
        print("\n>>Image file path is different. try again")
        sys.exit()

    success = convert(path, ext_from, ext_to)
    if not success:
        print(f">>There are no {ext_from} image files.")
    else:
        print(">>WELL DONE!!")

def convert(path, ext_from, ext_to):
    if path[-1] == '\\':
        path = path[:-1]

    jfif_images = []
    jfif_images = glob.glob(path + f'\\*{ext_from}')
    print(jfif_images)

    if jfif_images == []:
        return False

    for file in jfif_images:
        dirname = os.path.dirname(file) # ディレクトリ名
        basename_ext = os.path.basename(file) # ファイル名.拡張子
        basename, _ = os.path.splitext(basename_ext) # ファイル名, .拡張子

        to_path = dirname + '\\' + basename + f'.{ext_to}'

        shutil.copyfile(file, to_path)
        os.remove(file)
    
    return True
    

@click.command()
@click.argument('path', nargs=1)
@click.argument('ext_from', nargs=1)
@click.argument('ext_to', nargs=1)
def main(path, ext_from, ext_to):
    window(path, ext_from, ext_to)
    
if __name__ == '__main__':
    main()