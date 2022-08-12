import dearpygui.dearpygui as dpg
import os
import configparser
import jfif_to_jpg


# 初期化
dpg.create_context()
# 設定ファイル読み込み
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


# コールバック
def converter(sender, app_data, user_data):
    base_path = config.get('DEFAULT', 'accessable_path')
    path_name = dpg.get_value('path_name')
    # パスが入力されてない場合
    if path_name == '':
        dpg.set_value(user_data, '!Please enter the path.!')
    # アクセス可能パスじゃない場合
    elif not base_path in path_name:
        dpg.set_value(user_data, '!>>Cannot access this directory. try other directory path.!')
    # ディレクトリが存在しない場合
    elif not os.path.exists(path_name):
        dpg.set_value(user_data, '!>>Image file path is different. try again.!')
    else:
        try:
            jfif_to_jpg.convert(path_name)
            dpg.set_value(user_data, '>>WELL DONE')
        except:
            dpg.set_value(user_data, '!Something is wrong. Cannot convert!')


# メインウィンドウ設定
with dpg.window(label='main_window', tag='main_window'):
    dpg.add_text(">>Input path that the jfif file you wanna convert exists.")
    dpg.add_input_text(label='Path', tag='path_name', width=400)
    dpg.add_button(label='Convert' ,callback=converter, user_data='result_text')
    dpg.add_separator()
    dpg.add_text(tag='result_text')

# 後処理
dpg.create_viewport(title="jfif to jpg", width=500, height=250)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('main_window', True)
dpg.start_dearpygui()
dpg.destroy_context()
