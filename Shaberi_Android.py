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
prod = "jp.primetheory.talktalk"
uat =  "im.shaberi.app.uat"
china = "im.shaberi.app.china"
env = prod

start_app(env)

#object declare
if env == uat:
    phone_number = "0975916011"
elif env == prod:
    phone_number = "0975916010"

privacy_bt = Template(r"A_privacy_bt.png", record_pos=(0.301, 0.828), resolution=(720, 1600))
search_bt = Template(r"A_search_bt.png", record_pos=(-0.391, -0.697), resolution=(1080, 2220))
country = Template(r"tpl1713953960839.png", record_pos=(-0.246, -0.582), resolution=(720, 1600))
friend_page_bt = Template(r"tpl1713842755846.png", record_pos=(-0.006, 0.878), resolution=(720, 1600))
setting_page_bt = Template(r"tpl1713842764991.png", record_pos=(0.332, 0.878), resolution=(720, 1600))
chat_page_bt = Template(r"A_conversation_page.png", record_pos=(-0.332, 0.946), resolution=(720, 1600))
frandy_wide = Template(r"tpl1713842877006.png", record_pos=(-0.196, 0.281), resolution=(720, 1600))
frandy_narrow = Template(r"tpl1714030111403.png", record_pos=(-0.212, 0.465), resolution=(720, 1600))
frandy_contacts_search = Template(r"tpl1714033185445.png", record_pos=(-0.233, -0.269), resolution=(720, 1600))
send_bt = Template(r"A_send_bt.png", record_pos=(0.415, 0.872), resolution=(1080, 2220))
recording_icon = Template(r"A_recording_icon.png", record_pos=(0.414, 0.201), resolution=(720, 1600))
recording_bt = Template(r"tpl1694589160762.png", record_pos=(-0.006, 0.771), resolution=(1080, 2220))
recording_cancel_bt = Template(r"A_delete_bt.png", record_pos=(-0.422, 0.876), resolution=(1080, 2220))
expand_bt = Template(r"A_add_icon.png", record_pos=(-0.424, 0.389), resolution=(720, 1600))
download_bt  = Template(r"A_download_bt.png", record_pos=(-0.401, -0.329), resolution=(720, 1600))
pdf_bt = Template(r"tpl1694595130533.png", record_pos=(-0.239, 0.34), resolution=(720, 1600))
recent_bt = Template(r"A_recent_icon.png", record_pos=(-0.408, -0.526), resolution=(720, 1600))
camera_bt = Template(r"A_camera_icon.png", record_pos=(0.339, 0.657), resolution=(720, 1600))
call_bt = Template(r"tpl1713843734172.png", record_pos=(0.404, -0.958), resolution=(720, 1600))
vedio_call_bt = Template(r"tpl1714011264335.png", record_pos=(0.228, -0.833), resolution=(720, 1600))
voice_call_bt = Template(r"tpl1714011273588.png", record_pos=(-0.229, -0.835), resolution=(720, 1600))
hang_up = Template(r"tpl1714011710832.png", record_pos=(-0.001, 0.635), resolution=(720, 1600))
group = Template(r"tpl1713844310388.png", record_pos=(-0.151, -0.583), resolution=(720, 1600))
information_message = Template(r"tpl1714029558125.png", record_pos=(-0.318, -0.447), resolution=(720, 1600))
information_vedio_call = Template(r"tpl1714029566355.png", record_pos=(-0.003, -0.456), resolution=(720, 1600))
information_voice_call = Template(r"tpl1714029573000.png", record_pos=(0.315, -0.454), resolution=(720, 1600))
profile_bt = Template(r"tpl1695022053222.png", record_pos=(0.403, -0.744), resolution=(720, 1600))
nick_name_bt = Template(r"tpl1694756966534.png", record_pos=(-0.333, -0.547), resolution=(720, 1600))
delete_bt = Template(r"tpl1695015796864.png", record_pos=(0.421, 0.758), resolution=(720, 1600))
menu_bt = Template(r"tpl1695022944014.png", record_pos=(0.421, -0.974), resolution=(720, 1600))
average_bt = Template(r"tpl1713952503782.png", record_pos=(0.235, -0.818), resolution=(720, 1600))
red_packet_amount_textbox = Template(r"tpl1714031672328.png", record_pos=(-0.158, -0.551), resolution=(720, 1600))
qa_group = Template(r"tpl1714030583848.png", record_pos=(-0.161, -0.369), resolution=(720, 1600))


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
# Navigation_popup()

# Login Page ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def click_service():
    poco("Terms and Conditions of Use").click()
    sleep(2)
    keyevent("BACK")
    sleep(1)
# click_service()

def click_privacy():
    touch(privacy_bt)
    sleep(2)
    keyevent("BACK")
    sleep(1)
# click_privacy()

def login_and_verify(phone_number):
    # 國碼
    poco("+1").click()
    touch(search_bt)
    text("886")
    sleep(1)
    touch(country)

    # 輸入電話號碼
    poco("android.widget.EditText").click()
    text(phone_number)

    # 點擊下一步
    poco("Next").click()

    # 輸入驗證碼
    if env == uat:
        text("888888")
        sleep(5)
    else:
        sleep(25)
# login_and_verify(phone_number)

#permission requirement
for i in range(3):
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass 

#Bottom Bar Switch

def friend_page():
    touch(friend_page_bt)
    poco("Invite").wait_for_appearance()
# friend_page()

def setting_page():
    touch(setting_page_bt)
# setting_page()

def converation_page():
    touch(chat_page_bt)
# converation_page()

#one-on-one chat

def click_frandy():
    touch(frandy_wide)
click_frandy()

def send_message():
    poco("android.widget.EditText").click()
    text("Automatic")
    touch(send_bt)
send_message()

def recording():
    touch(recording_icon)
    sleep(1)
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass 
    wait(recording_bt)

    swipe(recording_bt, vector=[0, 0], duration=4)

    wait(recording_cancel_bt)
    touch(recording_cancel_bt)

    swipe(recording_bt, vector=[0, 0], duration=4)

    touch(send_bt)
recording()


#Send File
def send_file():
    touch(expand_bt)
    poco("File").click()
    sleep(1)
    if poco("com.android.packageinstaller:id/permission_allow_button").exists():
        poco("com.android.packageinstaller:id/permission_allow_button").click()
    else:
        pass 
    poco("Show roots").click()
    touch(download_bt)
    touch(pdf_bt)
    poco("com.android.documentsui:id/option_menu_grid").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_file()

#Send image
def send_image():
    poco("Album").click()
    poco("Show roots").click()
    touch(recent_bt)
    poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_image()

#send_red_packet
def send_redpacket():
    poco("Red Packet").click()
    sleep(2)
    poco("Send Red Packet").wait_for_appearance()
    poco("Send Red Packet").click()
    for i in range(5):
        touch(red_packet_amount_textbox)
    sleep(1)
    text("0.01")
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.widget.EditText")[1].click()
    text("Lets go")
    poco("Send").click()
    poco("Confirm sending red packet？").wait_for_appearance()
    poco("Send").click()
    poco("android.widget.EditText").click()
    text("888888")
    poco("Done").click()
    sleep(1)
send_redpacket()

#Open Camera
def open_camera():
    wait(camera_bt)
    touch(camera_bt)
    poco("Open camera").click()
    sleep(1)
    poco("com.oppo.camera:id/shutter_button").wait_for_appearance()
    poco("com.oppo.camera:id/shutter_button").click()
    poco("com.oppo.camera:id/done_button").wait_for_appearance()
    poco("com.oppo.camera:id/done_button").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
open_camera()

#Open Camera for video
def open_camera_video():
    sleep(1)
    wait(camera_bt)
    touch(camera_bt)
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
    sleep(1)
    touch(call_bt)
    touch(vedio_call_bt)
    sleep(6)
    touch(hang_up)
video_call()

#Voice Call
def voice_call():
    touch(voice_call_bt)
    sleep(6)
    touch(hang_up)
voice_call()

keyevent("BACK")

#Group test ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
touch(group)

send_message()

recording()

send_file()

send_image()

def send_redpacket_random():
    poco("Red Packet").click()  
    poco("Send Red Packet").wait_for_appearance()
    poco("Send Red Packet").click()
    wait(red_packet_amount_textbox)
    touch(red_packet_amount_textbox)
    sleep(1)
    text("0.01")
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.widget.EditText")[1].click()
    text("1")
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.widget.EditText")[2].click()
    text("Lets go")
    poco("Send Red Packet").click()
    poco("Send").click()
    poco("Confirm sending red packet？").wait_for_appearance()
    poco("Send").click()
    poco("android.widget.EditText").click()
    text("888888")
    poco("Done").click()
    sleep(1) 
send_redpacket_random()

def send_redpacket_average():
    touch(expand_bt)
    poco("Red Packet").click()
    touch(average_bt)
    sleep(1)
    poco("Send Red Packet").click()
    wait(red_packet_amount_textbox)
    touch(red_packet_amount_textbox)
    sleep(1)
    text("0.01")
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.widget.EditText")[1].click()
    text("1")
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.widget.EditText")[2].click()
    text("Lets go")
    poco("Send Red Packet").click()
    poco("Send").click()
    poco("Confirm sending red packet？").wait_for_appearance()
    poco("Send").click()
    poco("android.widget.EditText").click()
    text("888888")
    poco("Done").click()
    sleep(1)
send_redpacket_average()

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
touch(frandy_contacts_search)

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
touch(frandy_narrow)
keyevent("BACK")

#Search

#click search icon
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.widget.ImageView").click()
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
touch(frandy_narrow)
wait(information_message)
touch(information_message)
poco("android.widget.EditText").wait_for_appearance()
keyevent("BACK")
wait(information_vedio_call)
touch(information_vedio_call)
sleep(4)
touch(hang_up)
wait(information_voice_call)
touch(information_voice_call)
sleep(4)
touch(hang_up)
keyevent("BACK")

#Setting Page--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#My Profile
setting_page()
touch(profile_bt)


#Setting Avatar from open camera
#click avatar camera icon
def click_avatar_camera_icon():
    poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].offspring("Avatar").child("android.widget.ImageView")[0].click()
click_avatar_camera_icon()
poco("Open camera").click()
poco("com.oppo.camera:id/shutter_button").click()
poco("com.oppo.camera:id/done_button").wait_for_appearance()
poco("com.oppo.camera:id/done_button").click()
sleep(10)

#Setting Avatar from gallery
poco("Avatar").wait_for_appearance()
click_avatar_camera_icon()
poco("Open gallery").click()
sleep(3)
poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").wait_for_appearance()
poco("android.widget.FrameLayout").offspring("com.android.documentsui:id/drawer_layout").offspring("android.widget.FrameLayout").offspring("com.android.documentsui:id/container_directory").offspring("com.android.documentsui:id/dir_list").child("android.widget.LinearLayout")[0].offspring("android.view.View").click()

sleep(2)

#Setting Avatar from System default
poco("Avatar").wait_for_appearance()
click_avatar_camera_icon()
poco("System default").click()
poco("android.widget.FrameLayout").offspring("android.widget.FrameLayout").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View")[1].child("android.view.View").child("android.widget.ImageView")[1].click()
sleep(2)

#Edit Nick Name
poco("Avatar").wait_for_appearance()
def click_nickname():
    touch(nick_name_bt) 
click_nickname()
poco("android.widget.EditText")
text("1")
poco("Save").click()
wait(nick_name_bt)
click_nickname()
touch(delete_bt , times=1)
poco("Save").click()
wait(nick_name_bt)

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
touch(search_bt)
text("886")
sleep(1)
touch(country)

#登入
poco("Next").click()

#驗證碼認證
if env == uat:
    text("888888")
    sleep(5)
else:
    sleep(25)

#Multifunction Menu--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#create new group
def click_menu_button():
    touch(menu_bt)
click_menu_button()
poco("Create group").click()
touch(frandy_narrow)
poco("Next").click()
text("testgroup")
poco("android.widget.EditText").click()
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

#Clear History
click_menu_button()
poco("Clear history").click()
touch(qa_group)
poco("Delete").click()
poco("Are you sure you want to delete chat room?").wait_for_appearance()
poco("Delete").click()




stop_app("im.shaberi.app.uat")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True