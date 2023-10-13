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
# prod: jp.primetheory.talktalk
# uat: im.shaberi.app.uat
# china: im.shaberi.app.china

start_app("im.shaberi.app.uat")

#Navigation popup
def Navigation_popup():
    for _ in range(4):
        if poco("Next").exists():
            poco("Next").click()
        else:
            break
    if poco("Let’s go").exists():
        poco("Let’s go").click()
    else:
        pass
Navigation_popup()

# Login Page ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def click_service():
    poco("Terms and Conditions of Use").click()
    sleep(2)
    keyevent("BACK")
    sleep(1)
click_service()

def click_privacy():
    touch(Template(r"tpl1694593562098.png", record_pos=(0.301, 0.828), resolution=(720, 1600)))
    sleep(2)
    keyevent("BACK")
    sleep(1)
click_privacy()

def login_and_verify(phone_number, verification_code):
    # 國碼
    poco("+1").click()
    touch(Template(r"tpl1694573043333.png", record_pos=(-0.391, -0.697), resolution=(1080, 2220)))
    text("886")
    sleep(1)
    touch(Template(r"tpl1694575972670.png", record_pos=(-0.163, -0.524), resolution=(1080, 2220)))

    # 輸入電話號碼
    poco("android.widget.EditText").click()
    text(phone_number)

    # 點擊下一步
    poco("Next").click()

    # 輸入驗證碼
    text(verification_code)
    sleep(5)
login_and_verify("975916011", "888888")

#Bottom Bar Switch

def friend_page():
    touch(Template(r"tpl1694577567966.png", record_pos=(-0.007, 0.86), resolution=(1080, 2220)))
    poco("Invite").wait_for_appearance()
friend_page()

def setting_page():
    touch(Template(r"tpl1694571376374.png", record_pos=(0.332, 0.869), resolution=(1080, 2220)))
setting_page()

def converation_page():
    touch(Template(r"tpl1694596831101.png", record_pos=(-0.332, 0.946), resolution=(720, 1600)))
converation_page()

#one-on-one chat

def click_frandy():
    touch(Template(r"tpl1694584527320.png", record_pos=(-0.23, -0.54), resolution=(1080, 2220)))
click_frandy()

def send_message():
    poco("android.widget.EditText").click()
    text("Automatic")
    touch(Template(r"tpl1694591072193.png", record_pos=(0.415, 0.872), resolution=(1080, 2220)))
send_message()

def recording():
    touch(Template(r"tpl1695349179530.png", record_pos=(0.414, 0.201), resolution=(720, 1600)))
    sleep(1)
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass 
    exists(Template(r"tpl1694589160762.png", record_pos=(-0.006, 0.771), resolution=(1080, 2220)))

    swipe(Template(r"tpl1694589160762.png", record_pos=(-0.006, 0.771), resolution=(1080, 2220)), vector=[0, 0], duration=4)

    exists(Template(r"tpl1694591112563.png", record_pos=(-0.422, 0.876), resolution=(1080, 2220)))
    touch(Template(r"tpl1694591112563.png", record_pos=(-0.422, 0.876), resolution=(1080, 2220)))

    swipe(Template(r"tpl1694589160762.png", record_pos=(-0.006, 0.771), resolution=(1080, 2220)), vector=[0, 0], duration=4)

    touch(Template(r"tpl1694591072193.png", record_pos=(0.415, 0.872), resolution=(1080, 2220)))
recording()

#Send File
def send_file():
    touch(Template(r"tpl1694597015858.png", record_pos=(-0.424, 0.389), resolution=(720, 1600)))
    poco("file").click()
    sleep(1)
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass 
    poco("Show roots").click()
    touch(Template(r"tpl1694594958863.png", record_pos=(-0.401, -0.329), resolution=(720, 1600)))
    touch(Template(r"tpl1694595130533.png", record_pos=(-0.239, 0.34), resolution=(720, 1600)))
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_file()

#Send image
def send_image():
    poco("image").click()
    poco("Show roots").click()
    touch(Template(r"tpl1694595520334.png", record_pos=(-0.408, -0.526), resolution=(720, 1600)))
    poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_image()

#Open Camera
def open_camera():
    touch(Template(r"tpl1694597380196.png", record_pos=(0.339, 0.657), resolution=(720, 1600)))
    poco("Open camera").click()
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass
    poco("com.oppo.camera:id/shutter_button").wait_for_appearance()
    poco("com.oppo.camera:id/shutter_button").click()
    poco("com.oppo.camera:id/done_button").wait_for_appearance()
    poco("com.oppo.camera:id/done_button").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
open_camera()

#Open Camera for video
def open_camera_video():
    touch(Template(r"tpl1694597380196.png", record_pos=(0.339, 0.657), resolution=(720, 1600)))
    poco("Open camera for a video").wait_for_appearance()
    poco("Open camera for a video").click()
    poco("com.oppo.camera:id/shutter_button").wait_for_appearance()
    poco("com.oppo.camera:id/shutter_button").click()
    sleep(5)
    poco("com.oppo.camera:id/shutter_button").click()
    poco("com.oppo.camera:id/done_button").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
    sleep(5)
open_camera_video()
    
#Video Call
def video_call():
    touch(Template(r"tpl1694597620335.png", record_pos=(0.269, -0.963), resolution=(720, 1600)))
    sleep(1)
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass
    sleep(6)
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.widget.Button").child("android.widget.Button").click()
video_call()

#Voice Call
def voice_call():
    touch(Template(r"tpl1694596569317.png", record_pos=(0.406, -0.96), resolution=(720, 1600)))
    sleep(6)
    touch(Template(r"tpl1694599938205.png", record_pos=(-0.008, 0.738), resolution=(720, 1600)))
voice_call()

keyevent("BACK")

#Group test ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
touch(Template(r"tpl1694597962061.png", record_pos=(-0.163, -0.567), resolution=(720, 1600)))

send_message()

recording()

send_file()

send_image()

open_camera()

open_camera_video()

keyevent("BACK")


#Friend Page--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

friend_page()

#點擊查找好友

def click_contacts_icon():
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[0].child("android.widget.ImageView").click()
click_contacts_icon()
poco("android.widget.EditText").click()
text("frandy")
touch(Template(r"tpl1695286651621.png", record_pos=(-0.307, -0.243), resolution=(720, 1600)))

keyevent("BACK")

#Contacts- invite friend

click_contacts_icon()
poco("Invite").click()

#send invite message
def send_invite_message():
    poco("Messages").click()
    poco("com.android.mms:id/action_edit").click()
    poco("android:id/button3").click()
send_invite_message()
    
#Contacts- Contacts
def click_contacts():
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View").child("Contacts").child("Contacts").click()
click_contacts()
if poco("Open").exists():
    poco("Open").click()
else:
    pass
if poco("com.android.packageinstaller:id/permission_allow_button").exists():
    poco("com.android.packageinstaller:id/permission_allow_button").click()
else:
    pass
poco("Contacts Friends").wait_for_appearance()
keyevent("BACK")

#Contacts- Scan
def scan():
    poco("Scan").click()
    poco("Scan").wait_for_appearance()
    poco("Close").click()
scan()

#Contacts- friend list
click_frandy()
keyevent("BACK")

#Search

#click search icon
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].click()
text("Automatic")
poco("Chat History").wait_for_appearance()
keyevent("BACK")

#invite friend
poco("Invite").wait_for_appearance()
poco("Invite").click()
send_invite_message()

#Contacts
poco("Add").click()
poco("Contacts Friends").wait_for_appearance()
keyevent("BACK")

#Friend Information Page
click_frandy()
touch(Template(r"tpl1694747705367.png", record_pos=(-0.326, -0.412), resolution=(720, 1600)))
keyevent("BACK")
touch(Template(r"tpl1694747730215.png", record_pos=(-0.006, -0.406), resolution=(720, 1600)))
sleep(4)
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.widget.Button").child("android.widget.Button").click()
touch(Template(r"tpl1694747779655.png", record_pos=(0.315, -0.41), resolution=(720, 1600)))
sleep(4)
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.widget.ImageView").child("android.widget.Button").click()
keyevent("BACK")

#Setting Page--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#My Profile
setting_page()
touch(Template(r"tpl1695022053222.png", record_pos=(0.403, -0.744), resolution=(720, 1600)))


#Setting Avatar from open camera
#click avatar camera icon
def click_avatar_camera_icon():
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].offspring("Avatar").child("android.widget.ImageView")[0].click()
click_avatar_camera_icon()
poco("Open camera").click()
poco("com.oppo.camera:id/shutter_button").click()
poco("com.oppo.camera:id/done_button").wait_for_appearance()
poco("com.oppo.camera:id/done_button").click()
sleep(4)

#Setting Avatar from gallery
click_avatar_camera_icon()
poco("Open gallery").click()
sleep(1)
poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").click()
sleep(2)

#Setting Avatar from System default
click_avatar_camera_icon()
poco("System default").click()
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View").child("android.widget.ImageView")[1].click()
sleep(2)

#Edit Nick Name
def click_nickname():
    touch(Template(r"tpl1694756966534.png", record_pos=(-0.333, -0.547), resolution=(720, 1600))) 
click_nickname()
name = poco("android.widget.EditText")
text("1")
poco("Save").click()
click_nickname()
touch(Template(r"tpl1695015796864.png", record_pos=(0.421, 0.758), resolution=(720, 1600)) , times=1)
poco("Save").click()

#My QR code
def qrcode():
    poco("My QR code").click()
    
    poco("Close").wait_for_appearance()
    poco("Close").click()
qrcode()

#Logout
poco("Logout").click()
poco("Confirm").click()

#國碼
poco("+1").click() 
touch(Template(r"tpl1694573043333.png", record_pos=(-0.391, -0.697), resolution=(1080, 2220)))
text("886")
sleep(1)
touch(Template(r"tpl1694575972670.png", record_pos=(-0.163, -0.524), resolution=(1080, 2220)))

#登入
poco("Next").click()

#驗證碼認證
text("888888")
sleep(5)

#Multifunction Menu--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#create new group
def click_menu_button():
    touch(Template(r"tpl1695022944014.png", record_pos=(0.421, -0.974), resolution=(720, 1600)))
click_menu_button()
poco("New Group").click()
text("testgroup")
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View").child("android.widget.EditText")[1].click()
text("QA")
poco("Create").click()
sleep(1)
keyevent("BACK")

#Invite
sleep(1)
click_menu_button()
poco("Invite contact").click()
send_invite_message()

#Scan
click_menu_button()
scan()

#Read all
click_menu_button()
poco("Read all").click()
sleep(3)

#MyQrcode
click_menu_button()
qrcode()


stop_app("im.shaberi.app.uat")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True