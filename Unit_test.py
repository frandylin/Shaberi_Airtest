# simple_report(__file__, logpath=True)# -*- encoding=utf8 -*-
__author__ = "frandy"


from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///",])

dev = device()
poco = iosPoco()

if exists(Template(r"tpl1703847332009.png", record_pos=(0.38, -0.009), resolution=(1242, 2208))):
    touch(Template(r"tpl1703847332009.png", record_pos=(0.38, -0.009), resolution=(1242, 2208)))
else:
    pass
swipe(Template(r"tpl1701326417205.png", record_pos=(0.007, 0.378), resolution=(1242, 2208)), vector=[-0.0088, -0.5856])
def click_frandy():
    touch(Template(r"tpl1697180427811.png", record_pos=(-0.198, 0.488), resolution=(1242, 2208)))
click_frandy()
sleep(2)
touch(Template(r"tpl1695117530256.png", record_pos=(-0.319, -0.335), resolution=(1242, 2208)))
sleep(2)
back()
sleep(2)
touch(Template(r"tpl1695117813243.png", record_pos=(-0.001, -0.302), resolution=(1242, 2208)))
sleep(4)
touch(Template(r"tpl1701062972277.png", record_pos=(-0.001, 0.567), resolution=(1242, 2208)))
sleep(2)
touch(Template(r"tpl1695117062172.png", record_pos=(0.308, -0.348), resolution=(1242, 2208)))

sleep(4)
touch(Template(r"tpl1701062972277.png", record_pos=(-0.001, 0.567), resolution=(1242, 2208)))
back()














# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)