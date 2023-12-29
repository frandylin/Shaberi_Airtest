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
# prod: jp.primetheory.talktalk
# uat: im.shaberi.app.uat
# china: im.shaberi.app.china

start_app("jp.primetheory.talktalk")
 
#Navigation popup
def Navigation_popup():
    sleep(2)
    if exists(Template(r"tpl1696556947287.png", record_pos=(-0.201, 0.147), resolution=(1242, 2208))):
        touch(Template(r"tpl1696556947287.png", record_pos=(-0.201, 0.147), resolution=(1242, 2208)))
    else:
        pass
    sleep(2)
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

#服務協議＆隱私權政策
def click_service():
    poco("Terms and Conditions of Use").click()
    exists(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
    touch(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
    sleep(1)
click_service()
def click_privacy():
    poco("Privacy Policy").click()
    exists(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
    touch(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
    sleep(1)
click_privacy()

#Login
def login_and_vertify(phone_number):
#國碼
    poco("+886").click() 
    touch(Template(r"tpl1695031205216.png", record_pos=(-0.399, -0.589), resolution=(1242, 2208)))
    text("886")
    sleep(1)
    touch(Template(r"tpl1702365408156.png", record_pos=(-0.297, -0.422), resolution=(1242, 2208)))

#電話號碼欄位
    poco("Enter mobile phone number").click()
    text(phone_number)

#登入
    poco("Next").click()
    
#驗證碼認證
    sleep(20)
login_and_vertify("909317920")
    
#Bottom Bar 切換
def friend_page():
    touch(Template(r"tpl1695031730554.png", record_pos=(-0.002, 0.795), resolution=(1242, 2208)))
    poco("Invite").wait_for_appearance()
friend_page()

def setting_page():
    touch(Template(r"tpl1695031743067.png", record_pos=(0.326, 0.793), resolution=(1242, 2208)))
setting_page()

def conversation_page():
    touch(Template(r"tpl1697180012424.png", record_pos=(-0.338, 0.846), resolution=(1242, 2208)))
conversation_page()

#one-on-one chat
def click_frandy():
    touch(Template(r"tpl1697180427811.png", record_pos=(-0.198, 0.488), resolution=(1242, 2208)))
click_frandy()
    
#Send Message
def send_message():
    poco("Write a message…").click()
    text("Automatic")
    touch(Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208)))
send_message()

#錄音
def recording():
    touch(Template(r"tpl1695032132298.png", record_pos=(0.445, 0.268), resolution=(1242, 2208)))
    sleep(2)
    if exists(Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208))):
        touch(Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208)))
    else:
        pass 
    exists(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)))
    swipe(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)), vector=[0, 0], duration=4)
    exists(Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208)))
    touch(Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208)))
    swipe(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)), vector=[0, 0], duration=4)
    touch(Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208)))
recording()

#Send File
def send_file():
    touch(Template(r"tpl1695032236261.png", record_pos=(-0.432, 0.37), resolution=(1242, 2208)))
    poco("file").click()
    poco("f6423e27-f2c1-457b-8818-4eb64f460607").wait_for_appearance()
    poco("f6423e27-f2c1-457b-8818-4eb64f460607").click()
    touch(Template(r"tpl1695087272130.png", record_pos=(0.396, -0.722), resolution=(1242, 2208)))
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_file()

#Send image
def send_image():
    poco("image").click()
    poco("Photo, September 07, 10:33 AM").click()
    poco("Add").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
send_image()

#Send redpacket
def send_redpacket():
    poco("red packet").click()
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
    poco("Open camera").click()
    poco("Open camera").wait_for_appearance()
    poco("Open camera").click()
    sleep(2)
    if exists(Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208))):
        touch(Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208)))
    else:
        pass 
    poco("PhotoCapture").wait_for_appearance()
    poco("PhotoCapture").click()
    poco("Use Photo").wait_for_appearance
    poco("Use Photo").click()
    poco("Send").wait_for_appearance()
    poco("Send").click()
open_camera()
    
#Open Camera for video
def open_camera_video():
    poco("Open camera").click()
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
    touch(Template(r"tpl1695088291177.png", record_pos=(0.423, -0.775), resolution=(1242, 2208)))
    sleep(1)
    touch(Template(r"tpl1703728524301.png", record_pos=(0.224, -0.671), resolution=(1242, 2208)))
    sleep(6)
    touch(Template(r"tpl1701062972277.png", record_pos=(-0.001, 0.567), resolution=(1242, 2208)))
video_call()

#Voice Call
def voice_call():
    touch(Template(r"tpl1703728552287.png", record_pos=(-0.233, -0.67), resolution=(1242, 2208)))
    sleep(6)
    touch(Template(r"tpl1701062972277.png", record_pos=(-0.001, 0.567), resolution=(1242, 2208)))
voice_call()

def back():
    touch(Template(r"tpl1695088334527.png", record_pos=(-0.442, -0.775), resolution=(1242, 2208)))
back()

#Group test ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
touch(Template(r"tpl1695088387315.png", record_pos=(-0.195, -0.237), resolution=(1242, 2208)))

send_message()

#錄音
recording()

#Send File
send_file()

#Send image
send_image()

#Send redpacket
def send_redpacket_random():
    poco("red packet").click()
    poco("Send Red Packet").click()
    poco("0.010～50.000").click()
    text("0.01")
    poco("1～3").click()
    poco("2").click()
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
    touch(Template(r"tpl1695032236261.png", record_pos=(-0.432, 0.37), resolution=(1242, 2208)))
    poco("red packet").click()
    touch(Template(r"tpl1701677002216.png", record_pos=(0.252, -0.651), resolution=(1242, 2208)))
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
    touch(Template(r"tpl1695090045513.png", record_pos=(0.421, -0.777), resolution=(1242, 2208)))
click_contacts_icon()
poco("Search").click()
text("frandy")
click_frandy()
sleep(2)
back()

#Contacts- invite friend
click_contacts_icon()
sleep(2)
touch(Template(r"tpl1696227441852.png", record_pos=(-0.349, -0.455), resolution=(1242, 2208)))

#send invite message
def send_invite_message():
    exists(Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208)))
    touch(Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208)))
    touch(Template(r"tpl1695090685537.png", record_pos=(0.385, -0.701), resolution=(1242, 2208)))
    poco("Close").wait_for_appearance()
    poco("Close").click()
send_invite_message()

#Contacts- Contacts

def click_contacts():
    touch(Template(r"tpl1695116188444.png", record_pos=(-0.004, -0.457), resolution=(1242, 2208)))
click_contacts()
if poco("Open").exists():
    poco("Open").click()
else:
    pass
if exists(Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208))):
    touch(Template(r"tpl1696498169909.png", record_pos=(0.159, 0.141), resolution=(1242, 2208))) 
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
touch(Template(r"tpl1695116721936.png", record_pos=(-0.423, -0.629), resolution=(1242, 2208)))
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
if exists(Template(r"tpl1703847332009.png", record_pos=(0.38, -0.009), resolution=(1242, 2208))):
    touch(Template(r"tpl1703847332009.png", record_pos=(0.38, -0.009), resolution=(1242, 2208)))
else:
    pass
swipe(Template(r"tpl1701326417205.png", record_pos=(0.007, 0.378), resolution=(1242, 2208)), vector=[-0.0088, -0.5856])
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

#Setting Page--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#My Profile
touch(Template(r"tpl1695174540073.png", record_pos=(0.251, 0.093), resolution=(1242, 2208)))

touch(Template(r"tpl1695174598943.png", record_pos=(0.407, -0.595), resolution=(1242, 2208)))
#Setting Avatar from open camera
# def click_avatar_camera_icon():
#     touch(Template(r"tpl1695174650155.png", record_pos=(0.424, -0.552), resolution=(1242, 2208)))
# click_avatar_camera_icon()
# poco("Open camera").wait_for_appearance()
# poco("Open camera").click()
# poco("PhotoCapture").wait_for_appearance()
# poco("PhotoCapture").click()
# poco("Use Photo").wait_for_appearance()
# poco("Use Photo").click()
# sleep(4)

#Setting Avatar from gallery
# click_avatar_camera_icon()
# poco("Open gallery").wait_for_appearance()
# poco("Open gallery").click()
# if exists(Template(r"tpl1696556947287.png", record_pos=(-0.201, 0.147), resolution=(1242, 2208))):
#     touch(Template(r"tpl1696556947287.png", record_pos=(-0.201, 0.147), resolution=(1242, 2208)))
# else:
#     pass 

# sleep(1)
# poco("Screenshot, September 19, 1:16 PM").click()
# sleep(3)

#Setting Avatar from System default
# click_avatar_camera_icon()
# poco("System default").wait_for_appearance()
# poco("System default").click()
# touch(Template(r"tpl1695176125484.png", record_pos=(-0.118, 0.446), resolution=(1242, 2208)))
# sleep(2)

#Edit Nick Name
def click_nickname():
    touch(Template(r"tpl1695176168283.png", record_pos=(-0.348, -0.422), resolution=(1242, 2208)))
click_nickname()
text("1")
poco("Save").click()
click_nickname()
touch(Template(r"tpl1695176247609.png", record_pos=(0.437, 0.685), resolution=(1242, 2208)) , times=1)
poco("Save").click()

#My QR code
poco("My QR code").click()
poco("Close").wait_for_appearance()
poco("Close").click()

#Logout
poco("Logout").click()
poco("Confirm").click()

#登入
poco("Next").click()

#驗證碼認證
sleep(20)

#Multifunction Menu--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#create new group
def click_menu_button():
    touch(Template(r"tpl1696228277023.png", record_pos=(0.431, -0.781), resolution=(1242, 2208)))
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
touch(Template(r"tpl1703733416351.png", record_pos=(-0.097, -0.634), resolution=(1242, 2208)))
poco("Delete").click()
poco("Are you sure you want to delete chat room?").wait_for_appearance()
poco("Delete").click()


stop_app("im.shaberi.app.uat")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True