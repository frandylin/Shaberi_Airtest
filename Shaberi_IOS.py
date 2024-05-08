# -*- encoding=utf8 -*-
__author__ = "frandy"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.ios import iosPoco



if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///",])

dev = device()
poco = iosPoco()

# script content
prod = "jp.primetheory.talktalk"
uat =  "im.shaberi.app.uat"
china = "im.shaberi.app.china"
env = china

start_app(env)

#object declare
if env == uat:
    phone_number = "0975916012"
elif env == prod:
    phone_number = "0909317920"
elif env == china:
    phone_number = "0909317920"

allow_bt = Template(r"tpl1713349533990.png", record_pos=(0.158, 0.184), resolution=(1170, 2532))
done_bt = Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208))
search_bt = Template(r"tpl1695031205216.png", record_pos=(-0.399, -0.589), resolution=(1242, 2208))
country_code = Template(r"tpl1702365408156.png", record_pos=(-0.297, -0.422), resolution=(1242, 2208))
ok_bt = Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208))
friend_page_bt = Template(r"tpl1713404685990.png", record_pos=(-0.003, 0.791), resolution=(1242, 2208))
setting_page_bt = Template(r"tpl1713404696126.png", record_pos=(0.33, 0.793), resolution=(1242, 2208))
chat_page_bt = Template(r"tpl1697180012424.png", record_pos=(-0.338, 0.846), resolution=(1242, 2208))
frandy = Template(r"tpl1713517146715.png", record_pos=(-0.275, 0.546), resolution=(1242, 2208))
send_bt = Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208))
recording_icon = Template(r"tpl1695032132298.png", record_pos=(0.445, 0.268), resolution=(1242, 2208))
recording_bt = Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208))
recording_cancel_bt = Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208))
expand_bt = Template(r"tpl1695032236261.png", record_pos=(-0.432, 0.37), resolution=(1242, 2208))
file_bt = Template(r"tpl1713422122913.png", record_pos=(-0.304, -0.366), resolution=(1242, 2208))
open_bt = Template(r"tpl1695087272130.png", record_pos=(0.396, -0.722), resolution=(1242, 2208))
camera_bt = Template(r"tpl1713411639411.png", record_pos=(0.357, 0.812), resolution=(1242, 2208))
call_bt = Template(r"tpl1695088291177.png", record_pos=(0.423, -0.775), resolution=(1242, 2208))
vedio_call_bt = Template(r"tpl1703728524301.png", record_pos=(0.224, -0.671), resolution=(1242, 2208))
voice_call_bt = Template(r"tpl1703728552287.png", record_pos=(-0.233, -0.67), resolution=(1242, 2208))
hangup_bt = Template(r"tpl1713412557080.png", record_pos=(-0.003, 0.567), resolution=(1242, 2208))
back_bt = Template(r"tpl1695088334527.png", record_pos=(-0.442, -0.775), resolution=(1242, 2208))
group = Template(r"tpl1713419073255.png", record_pos=(-0.202, 0.118), resolution=(1242, 2208))
redpacket_average_bt = Template(r"tpl1701677002216.png", record_pos=(0.252, -0.651), resolution=(1242, 2208))
contacts_icon = Template(r"tpl1695090045513.png", record_pos=(0.421, -0.777), resolution=(1242, 2208))
invite_bt = Template(r"tpl1696227441852.png", record_pos=(-0.349, -0.455), resolution=(1242, 2208))
message_app = Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208))
cancel_bt = Template(r"tpl1695090685537.png", record_pos=(0.385, -0.701), resolution=(1242, 2208))
contacts_bt = Template(r"tpl1695116188444.png", record_pos=(-0.004, -0.457), resolution=(1242, 2208))
search_history_bt = Template(r"tpl1695116721936.png", record_pos=(-0.423, -0.629), resolution=(1242, 2208))
hide_bt = Template(r"tpl1703847332009.png", record_pos=(0.38, -0.009), resolution=(1242, 2208))
swipe_point = Template(r"tpl1701326417205.png", record_pos=(0.007, 0.378), resolution=(1242, 2208))
informatopn_message_bt = Template(r"tpl1713428217109.png", record_pos=(-0.316, -0.334), resolution=(1242, 2208))
information_vedio_call = Template(r"tpl1695117813243.png", record_pos=(-0.001, -0.302), resolution=(1242, 2208))
information_voice_call = Template(r"tpl1713428239780.png", record_pos=(0.31, -0.342), resolution=(1242, 2208))
profile_bt = Template(r"tpl1695174598943.png", record_pos=(0.407, -0.595), resolution=(1242, 2208))
avatar_bt = Template(r"tpl1695174650155.png", record_pos=(0.424, -0.552), resolution=(1242, 2208))
avatar = Template(r"tpl1695176125484.png", record_pos=(-0.118, 0.446), resolution=(1242, 2208))
nick_name_bt = Template(r"tpl1695176168283.png", record_pos=(-0.348, -0.422), resolution=(1242, 2208))
delete_btn = Template(r"tpl1695176247609.png", record_pos=(0.437, 0.685), resolution=(1242, 2208))
menu_bt = Template(r"tpl1696228277023.png", record_pos=(0.431, -0.781), resolution=(1242, 2208))
test_group = Template(r"tpl1713406876500.png", record_pos=(-0.143, -0.072), resolution=(1242, 2208))






 
#Navigation popup
def Navigation_popup():
    sleep(2)
    if poco("Notifications may include alerts, sounds, and icon badges. These can be configured in Settings.").exists():
        touch(allow_bt)
    else:
        pass
    sleep(2)
    for _ in range(4):
        if poco("Start").exists():
            poco("Start").click()
        else:
            break
    if poco("Let’s go").exists():
        poco("Let’s go").click()
    else:
        pass
    
#服務協議＆隱私權政策
def click_service():
    poco("Terms and Conditions of Use").click()
    exists(done_bt)
    touch(done_bt)
    sleep(1)

def click_privacy():
    poco("Privacy Policy").click()
    exists(done_bt)
    touch(done_bt)
    sleep(1)
    

Navigation_popup()
click_service()
click_privacy()

#Login
def login_and_vertify(phone_number):
#國碼
    poco("+886").click() 
    touch(search_bt)
    text("886")
    sleep(1)
    touch(country_code)

#電話號碼欄位
    poco("Enter mobile phone number").click()
    text(phone_number)

#登入
    poco("Next").click()

#驗證碼認證
    if env == uat:
        text("888888")
        sleep(5)
    else:
        sleep(25)
# login_and_vertify(phone_number)

#permission requirement
for i in range(3):
    if exists(ok_bt):
        touch(ok_bt) 
    else:
        pass 

    
#Bottom Bar 切換
def friend_page():
    touch(friend_page_bt)
    poco("Invite").wait_for_appearance()
friend_page()

def setting_page():
    touch(setting_page_bt)
setting_page()

def conversation_page():
    touch(chat_page_bt)
conversation_page()

#one-on-one chat
def click_frandy():
    touch(frandy)
click_frandy()
    
#Send Message
def send_message():
    poco("Message").click()
    text("Automatic")
    touch(send_bt)
send_message()

#錄音
def recording():
    touch(recording_icon)
    sleep(2)
    exists(recording_bt)
    swipe(recording_bt, vector=[0, 0], duration=4)
    exists(recording_cancel_bt)
    touch(recording_cancel_bt)
    swipe(recording_bt, vector=[0, 0], duration=4)
    touch(send_bt)
recording()

#Send File
def send_file():
    touch(expand_bt)
    poco("File").click()
    exists(file_bt)
    touch(file_bt)
    touch(open_bt)
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_file()

#Send image
def send_image():
    poco("Album").click()
    poco("Photo, April 18, 10:03 AM").click() 
    poco("Add").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_image()

#Send redpacket
def send_redpacket():
    poco("Red Packet").click()
    poco("Send Red Packet").click()
    poco("0.010～50.000").click()
    poco("0").click()
    poco(".").click()
    poco("0").click()
    poco("1").click()
    poco("The red packet is coming!").click()
    text("Lets goooooooo")
    poco("Send").click()
    poco("Confirm sending red packet？").wait_for_appearance()
    poco("Send").click()
    poco("Please enter a 6-digit password").click()
    text("888888")
    poco("Done").click()
    sleep(1)
send_redpacket()



#Open Camera
def open_camera():
    touch(camera_bt)
    poco("Open camera").wait_for_appearance()
    poco("Open camera").click()
    sleep(2)
    poco("PhotoCapture").wait_for_appearance()
    poco("PhotoCapture").click()
    poco("Use Photo").wait_for_appearance
    poco("Use Photo").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
open_camera()
    
#Open Camera for video
def open_camera_video():
    touch(camera_bt)
    poco("Open camera for a video").wait_for_appearance()
    poco("Open camera for a video").click()
    poco("VideoCapture").wait_for_appearance()
    poco("VideoCapture").click()
    sleep(5)
    poco("VideoCapture").click()
    poco("Use Video").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
    sleep(5)
open_camera_video()

#Video Call
def video_call():
    touch(call_bt)
    sleep(1)
    touch(vedio_call_bt)
    sleep(6)
    touch(hangup_bt)
video_call()

#Voice Call
def voice_call():
    touch(voice_call_bt)
    sleep(6)
    touch(hangup_bt)
voice_call()

def back():
    touch(back_bt)
back()

#Group test ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
touch(group)

send_message()

#錄音
recording()

#Send File
send_file()

#Send image
send_image()

#Send redpacket
def send_redpacket_random():
    poco("Red Packet").click()
    poco("Send Red Packet").click()
    poco("0.010～50.000").click()
    text("0.01")
    poco("1～4").click()
    poco("1").click()
    poco("The red packet is coming!").click()
    text("Lets goooooooo")
    poco("Send").click()
    poco("Confirm sending red packet？").wait_for_appearance()
    poco("Send").click()
    poco("Please enter a 6-digit password").click()
    text("888888")
    poco("Done").click()
    sleep(2)
send_redpacket_random()

def send_redpacket_regular():
    touch(expand_bt)
    poco("Red Packet").click()
    touch(redpacket_average_bt)
    poco("Send Red Packet").click()
    poco("0.010～50.000").wait_for_appearance()
    poco("0.010～50.000").click()
    text("0.01")
    poco("1～3").click()
    poco("1").click()
    poco("The red packet is coming!").click()
    text("Lets goooooooo")
    poco("Send").click()
    poco("Confirm sending red packet？").wait_for_appearance()
    poco("Send").click()
    poco("Please enter a 6-digit password").click()
    text("888888")
    poco("Done").click()
    sleep(2)
send_redpacket_regular()  

#Open Camera
open_camera()

#Open Camera for video
open_camera_video()

back()

#Friend Page---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

friend_page()

#點擊查找好友
def click_contacts_icon():
    touch(contacts_icon)
click_contacts_icon()
poco("Search").click()
text("frandy")
click_frandy()
sleep(2)
back()

#Contacts- invite friend
click_contacts_icon()
sleep(2)
touch(invite_bt)

#send invite message
def send_invite_message():
    exists(message_app)
    touch(message_app)
    wait(cancel_bt)
    touch(cancel_bt)
    poco("Close").wait_for_appearance()
    poco("Close").click()
send_invite_message()

#Contacts- Contacts

def click_contacts():
    touch(contacts_bt)
click_contacts()
if poco("Open").exists():
    poco("Open").click()
else:
    pass
if exists(ok_bt):
    touch(ok_bt) 
else:
    pass 
poco("Contacts Friends").wait_for_appearance()
back()

#Contacts- Scan
def scan():
    poco("Scan").click()
    poco("Scan").wait_for_appearance()
    poco("Close").click()
scan()

#Contacts- friend list
click_frandy()
sleep(2)
back()


#Search
touch(search_history_bt)
text("Automatic")
poco("Chat History").wait_for_appearance()
back()

#invite friend
poco("Invite").wait_for_appearance()
poco("Invite").click()
send_invite_message()


#Contacts
poco("Add").click()
poco("Contacts Friends").wait_for_appearance()
back()

#Friend Information Page
#如有近期好友列表收起
if exists(hide_bt):
    touch(hide_bt)
else:
    pass
swipe(swipe_point, vector=[-0.0088, -0.5856])
click_frandy()
sleep(2)
touch(informatopn_message_bt)
sleep(2)
back()
sleep(2)
touch(information_vedio_call)
sleep(4)
touch(hangup_bt)
sleep(2)
touch(information_voice_call)
sleep(4)
touch(hangup_bt)
back()

#Setting Page--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#My Profile
touch(setting_page_bt)
touch(profile_bt)
# Setting Avatar from open camera
def click_avatar_camera_icon():
    touch(avatar_bt)
if env == uat:
    click_avatar_camera_icon()
    poco("Open camera").wait_for_appearance()
    poco("Open camera").click()
    poco("PhotoCapture").wait_for_appearance()
    poco("PhotoCapture").click()
    poco("Use Photo").wait_for_appearance()
    poco("Use Photo").click()
    sleep(4)
    poco("Open gallery").wait_for_appearance()
    poco("Open gallery").click()
    if exists(allow_bt):
        touch(allow_bt)
    else:
        pass 
    sleep(1)
    poco("Screenshot, September 19, 1:16 PM").click()
    sleep(3)
    click_avatar_camera_icon()
    poco("System default").wait_for_appearance()
    poco("System default").click()
    touch(avatar)
    sleep(2)
else:
    pass



#Edit Nick Name
def click_nickname():
    touch(nick_name_bt)
click_nickname()
text("1")
poco("Save").click()
click_nickname()
touch(delete_btn , times=1)
poco("Save").click()

#My QR code
poco("My QR code").click()
poco("Close").wait_for_appearance()
poco("Close").click()

# #Logout
# poco("Logout").click()
# poco("Confirm").click()

# #登入
# poco("Next").click()

# #驗證碼認證
# sleep(25)

#Multifunction Menu--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#create new group
def click_menu_button():
    touch(menu_bt)
click_menu_button()
poco("Create group").click()
click_frandy()
poco("Next").click()
poco("Please enter a group name").click()
text("test group")
poco("Create").click()
sleep(1)
back()
sleep(2)

#Invite
click_menu_button()
poco("Invite contact").click()
send_invite_message()
sleep(2)

#Scan
click_menu_button()
poco("Scan").click()
poco("Scan").wait_for_appearance()
poco("Close").click()
sleep(2)
#Read all
click_menu_button()
poco("Read all").click()
sleep(3)

#MyQrcode
click_menu_button()
poco("My QR code").click()
poco("My QR code").wait_for_appearance()
poco("Close").click()

#Clear history
click_menu_button()
poco("Clear history").click()
touch(test_group)
poco("Delete").click()
poco("Are you sure you want to delete chat room?").wait_for_appearance()
poco("Delete").click()


stop_app("im.shaberi.app.uat")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True

