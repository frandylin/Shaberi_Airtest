# simple_report(__file__, logpath=True)# -*- encoding=utf8 -*-
__author__ = "frandy"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android:///",])


from poco.drivers.cocosjs import CocosJsPoco
from poco.drivers.ios import iosPoco


dev = device()


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content

start_app("im.shaberi.app.uat")

#Logout

# def logout_in():
#     touch(Template(r"tpl1694571376374.png", record_pos=(0.332, 0.869), resolution=(1080, 2220)))
#     touch(Template(r"tpl1695022053222.png", record_pos=(0.403, -0.744), resolution=(720, 1600)))
#     poco("Logout").click()
#     poco("Confirm").click()
#     poco("+1").click() 
#     touch(Template(r"tpl1694573043333.png", record_pos=(-0.391, -0.697), resolution=(1080, 2220)))
#     text("886")
#     sleep(1)
#     touch(Template(r"tpl1694575972670.png", record_pos=(-0.163, -0.524), resolution=(1080, 2220)))
#     poco("Next").click()
#     text("888888")
#     sleep(5)
# repeat_count = 10
# for _ in range(repeat_count):
#     logout_in()
poco("file").click()
sleep(2)
if poco("permission_allow_button").exists():
    poco("permission_allow_button").click()
else:
    pass
    
# stop_app("im.shaberi.app.uat")










    
    





















# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)