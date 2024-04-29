# simple_report(__file__, logpath=True)# -*- encoding=utf8 -*-
__author__ = "frandy"


from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

dev = device()
# poco = iosPoco()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("im.shaberi.app.uat")

expand_bt = Template(r"A_add_icon.png", record_pos=(-0.424, 0.389), resolution=(720, 1600))
average_bt = Template(r"tpl1713952503782.png", record_pos=(0.235, -0.818), resolution=(720, 1600))
red_packet_amount_textbox = Template(r"tpl1714024931803.png", record_pos=(-0.242, -0.56), resolution=(720, 1600))
frandy_narrow = Template(r"tpl1714030111403.png", record_pos=(-0.212, 0.465), resolution=(720, 1600))
information_message = Template(r"tpl1714029558125.png", record_pos=(-0.318, -0.447), resolution=(720, 1600))

poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").wait_for_appearance()
poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").click()




# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)