# jfif to jpg batch converter

Converts jfif images to jpg. Useful for fixing images downloaded from Twitter.

*jfifファイルをjpgファイルに変換 twitterからダウンロードした画像を一括変換する*



## Usage Instructions

### Pre-Requisites
1. [Python is installed](https://www.python.org/downloads/)
2. Run this from a command prompt: `pip install DearPyGui click`

#### GUI:

Run `gui.py`, paste a folder path that contains jfif files into it and click `Convert`. Your files will be converted instantly.



#### Command prompt / Terminal:.

Navigate to the directory that holds `jfif_to_jpg.py` in a terminal (Use the cd command on Windows)

Type this, but replace FILEPATH with the path to your folder that contains jfif files.

`python jfif_to_jpg.py FILEPATH`

For example:

`python jfif_to_jpg.py C:\Downloads\MyTwitterDownloads`



## Recommended:

Install the `jpgNOTjfif.reg` file.
Twitter will no longer download jfif files and will instead download jpg. The fix works instantly!
