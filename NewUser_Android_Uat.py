# -*- encoding=utf8 -*-
__author__ = "frandy"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])



from poco.drivers.cocosjs import CocosJsPoco

dev = device()

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# script content
# script content
# prod: jp.primetheory.talktalk
# uat: im.shaberi.app.uat
# china: im.shaberi.app.china

start_app("im.shaberi.app.uat")

def login_and_verify(phone_number, verification_code):
    # 國碼
    poco("+1").click()
    touch(Template(r"A_search_bt.png", record_pos=(-0.391, -0.697), resolution=(1080, 2220)))
    text("886")
    sleep(1)
    touch(Template(r"A_taiwan_bt.png", record_pos=(-0.163, -0.524), resolution=(1080, 2220)))

    # 輸入電話號碼
    poco("android.widget.EditText").click()
    text(phone_number)

    # 點擊下一步
    poco("Next").click()

    # 輸入驗證碼
    text(verification_code)
    sleep(5)
login_and_verify("975916099", "888888")



# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)