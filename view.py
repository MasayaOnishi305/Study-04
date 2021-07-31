from os import system
import eel
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
#index.html 小計処理
def get_main(order_menu,quantity,total):
    result = pos_system.main(order_menu,quantity,total)
    eel.view_log_js(result)

@ eel.expose
#calc.html 会計処理
def get_calc(total,payment):
    result = pos_system.calc(total,payment)
    eel.view_calc_js(result)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)