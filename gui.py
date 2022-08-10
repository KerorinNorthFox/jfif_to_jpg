import dearpygui.dearpygui as dpg
import os
import jfif_to_jpg

# コールバック
def converter(sender, app_data, user_data):
    path_name = dpg.get_value('path_name')
    if not jfif_to_jpg.accessable_path in path_name:
        dpg.set_value(user_data, '!>>Cannot access this directory. try other directory path.!')
    elif not os.path.exists(path_name):
        dpg.set_value(user_data, '!>>Image file path is different. try again.!')
    else:
        try:
            jfif_to_jpg.convert(path_name)
            dpg.set_value(user_data, '>>WELL DONE')
        except:
            dpg.set_value(user_data, '!Something is wrong. Cannot convert!')

# 初期化
dpg.create_context()

# メインウィンドウ設定
with dpg.window(label='main_window', tag='main_window'):
    dpg.add_text(">>Input path the jfif file that you wanna convert exists.")
    dpg.add_input_text(tag='path_name', width=400)
    dpg.add_button(callback=converter, user_data='result_text')
    dpg.add_separator()
    dpg.add_text(tag='result_text')

# 後処理
dpg.create_viewport(title="dear_pygui", width=510, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('main_window', True)
dpg.start_dearpygui()
dpg.destroy_context()
