import dearpygui.dearpygui as dpg  # This is a PIP package. If your edit doesn't have it use: pip install dearpygui
import os
import configparser
import jfif_to_jpg

# 初期化
dpg.create_context()
# 設定ファイル読み込み
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


# コールバック
def converter(sender, app_data, user_data):  # TODO: These don't show up for me. But the converting works anyway.
    base_path = config.get('DEFAULT', 'accessible_path')
    path_name = dpg.get_value('path_name')
    # パスが入力されてない場合
    if path_name == '':
        dpg.set_value(user_data, '!No path was specified, please enter a valid path!')
    # アクセス可能パスじゃない場合
    elif base_path not in path_name:
        dpg.set_value(user_data, '!>>Cannot access the directory ' + path_name + '. Try a different directory!')
    # ディレクトリが存在しない場合
    elif not os.path.exists(path_name):
        dpg.set_value(user_data, '!>>Image file path is different. Try again!')
    else:
        try:
            success = jfif_to_jpg.convert(path_name)
            if not success:
                dpg.set_value(user_data, '>>There are no jfif image files in the ' + path_name + 'directory.')
            else:
                dpg.set_value(user_data, '>>Complete!')
        except (NameError, TypeError) as error:
            dpg.set_value(user_data, '!Something is wrong. Cannot convert!\n' + error)


# メインウィンドウ設定
with dpg.window(label='main_window', tag='main_window'):
    dpg.add_text(">>Input the folder path that holds the jfif files you want to convert:")
    dpg.add_input_text(label='Path', tag='path_name', width=400)
    dpg.add_button(label='Convert', callback=converter, user_data='result_text')
    dpg.add_separator()
    dpg.add_text(tag='result_text')

# 後処理
dpg.create_viewport(title="jfif to jpg", width=550, height=250)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('main_window', True)
dpg.start_dearpygui()
dpg.destroy_context()
