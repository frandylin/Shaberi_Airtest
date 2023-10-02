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

start_app("im.shaberi.app.uat")

#服務協議＆隱私權政策
poco("Terms and Conditions of Use").click()
exists(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
touch(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))

sleep(1)

poco("Privacy Policy").click()
exists(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
touch(Template(r"tpl1695031008707.png", record_pos=(-0.416, -0.797), resolution=(1242, 2208)))
sleep(1)
 
#國碼
poco("+886").click() 
touch(Template(r"tpl1695031205216.png", record_pos=(-0.399, -0.589), resolution=(1242, 2208)))

text("886")
sleep(1)
touch(Template(r"tpl1695031569511.png", record_pos=(-0.281, -0.413), resolution=(1242, 2208)))

#電話號碼欄位
poco("Enter mobile phone number").click()
text("975916012")

#登入
poco("Next").click()

#驗證碼認證
text("888888")
sleep(5)

#Bottom Bar 切換

touch(Template(r"tpl1695031730554.png", record_pos=(-0.002, 0.795), resolution=(1242, 2208)))


poco("Invite").wait_for_appearance()

touch(Template(r"tpl1695031743067.png", record_pos=(0.326, 0.793), resolution=(1242, 2208)))


touch(Template(r"tpl1695031765748.png", record_pos=(-0.337, 0.846), resolution=(1242, 2208)))

touch(Template(r"tpl1695032038652.png", record_pos=(-0.246, -0.248), resolution=(1242, 2208)))

#Send Message
poco("Write a message…").click()
text("Automatic")
touch(Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208)))



#錄音
touch(Template(r"tpl1695032132298.png", record_pos=(0.445, 0.268), resolution=(1242, 2208)))


exists(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)))

swipe(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)), vector=[0, 0], duration=4)

exists(Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208)))
touch(Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208)))

swipe(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)), vector=[0, 0], duration=4)

touch(Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208)))

#Send File

touch(Template(r"tpl1695032236261.png", record_pos=(-0.432, 0.37), resolution=(1242, 2208)))

poco("file").click()
poco("f6423e27-f2c1-457b-8818-4eb64f460607").wait_for_appearance()
poco("f6423e27-f2c1-457b-8818-4eb64f460607").click()
touch(Template(r"tpl1695087272130.png", record_pos=(0.396, -0.722), resolution=(1242, 2208)))


poco("Send").wait_for_appearance()
poco("Send").click()


#Send image

poco("image").click()
poco("Photo, September 07, 10:33 AM").click()
poco("Add").click()
poco("Send").wait_for_appearance()
poco("Send").click()

#Open Camera
poco("Open camera").click()
poco("Open camera").click()
poco("PhotoCapture").wait_for_appearance()
poco("PhotoCapture").click()
poco("Use Photo").wait_for_appearance
poco("Use Photo").click()
poco("Send").wait_for_appearance()
poco("Send").click()

#Open Camera for video
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

#Video Call
sleep(5)

touch(Template(r"tpl1695088260519.png", record_pos=(0.3, -0.776), resolution=(1242, 2208)))
sleep(6)
poco("Hangup").click()


#Voice Call
touch(Template(r"tpl1695088291177.png", record_pos=(0.423, -0.775), resolution=(1242, 2208)))
sleep(6)
poco("Hangup").click()

touch(Template(r"tpl1695088334527.png", record_pos=(-0.442, -0.775), resolution=(1242, 2208)))


#Group test ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
touch(Template(r"tpl1695088387315.png", record_pos=(-0.195, -0.237), resolution=(1242, 2208)))
poco("Write a message…").click()
text("Automatic")
touch(Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208)))



#錄音
touch(Template(r"tpl1695032132298.png", record_pos=(0.445, 0.268), resolution=(1242, 2208)))


exists(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)))

swipe(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)), vector=[0, 0], duration=4)

exists(Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208)))
touch(Template(r"tpl1695032183598.png", record_pos=(-0.429, 0.804), resolution=(1242, 2208)))

swipe(Template(r"tpl1695032147242.png", record_pos=(-0.009, 0.709), resolution=(1242, 2208)), vector=[0, 0], duration=4)

touch(Template(r"tpl1695032109773.png", record_pos=(0.431, 0.814), resolution=(1242, 2208)))

#Send File

touch(Template(r"tpl1695032236261.png", record_pos=(-0.432, 0.37), resolution=(1242, 2208)))
poco("file").click()
poco("f6423e27-f2c1-457b-8818-4eb64f460607").wait_for_appearance()
poco("f6423e27-f2c1-457b-8818-4eb64f460607").click()

touch(Template(r"tpl1695087272130.png", record_pos=(0.396, -0.722), resolution=(1242, 2208)))
poco("Send").wait_for_appearance()
poco("Send").click()


#Send image

poco("image").click()
poco("Photo, September 07, 10:33 AM").click()
poco("Add").click()
poco("Send").wait_for_appearance()
poco("Send").click()

#Open Camera
poco("Open camera").click()
poco("Open camera").click()
poco("PhotoCapture").wait_for_appearance()
poco("PhotoCapture").click()
poco("Use Photo").wait_for_appearance
poco("Use Photo").click()
poco("Send").wait_for_appearance()
poco("Send").click()

#Open Camera for video
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
touch(Template(r"tpl1695088334527.png", record_pos=(-0.442, -0.775), resolution=(1242, 2208)))


#Friend Page------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

touch(Template(r"tpl1695089275253.png", record_pos=(-0.007, 0.797), resolution=(1242, 2208)))
touch(Template(r"tpl1695090045513.png", record_pos=(0.421, -0.777), resolution=(1242, 2208)))

poco("Search").click()
text("frandy")
touch(Template(r"tpl1695090110477.png", record_pos=(-0.263, -0.154), resolution=(1242, 2208)))
sleep(2)
touch(Template(r"tpl1695116100394.png", record_pos=(-0.446, -0.775), resolution=(1242, 2208)))

#Contacts- invite friend

touch(Template(r"tpl1695090045513.png", record_pos=(0.421, -0.777), resolution=(1242, 2208)))

touch(Template(r"tpl1695089275253.png", record_pos=(-0.007, 0.797), resolution=(1242, 2208)))
poco("Invite").click()
exists(Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208)))
touch(Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208)))
touch(Template(r"tpl1695090685537.png", record_pos=(0.385, -0.701), resolution=(1242, 2208)))
poco("Close").click()


#Contacts- Contacts

touch(Template(r"tpl1695116188444.png", record_pos=(-0.004, -0.457), resolution=(1242, 2208)))

poco("A friend who is using Shaberi").wait_for_appearance()

touch(Template(r"tpl1695116100394.png", record_pos=(-0.446, -0.775), resolution=(1242, 2208)))

#Contacts- Scan
poco("Scan").click()
poco("Scan").wait_for_appearance()
poco("Close").click()



#Contacts- friend list

touch(Template(r"tpl1695090110477.png", record_pos=(-0.263, -0.154), resolution=(1242, 2208)))
sleep(2)
touch(Template(r"tpl1695116539031.png", record_pos=(-0.472, -0.771), resolution=(1242, 2208)))


#Search
touch(Template(r"tpl1695116721936.png", record_pos=(-0.423, -0.629), resolution=(1242, 2208)))
text("Automatic")
poco("Chat History").wait_for_appearance()
touch(Template(r"tpl1695116100394.png", record_pos=(-0.446, -0.775), resolution=(1242, 2208)))

#invite friend
poco("Invite").wait_for_appearance()
poco("Invite").click()
touch(Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208)))
touch(Template(r"tpl1695090685537.png", record_pos=(0.385, -0.701), resolution=(1242, 2208)))
poco("Close").wait_for_appearance()
poco("Close").click()


#Contacts
poco("Add").click()
poco("Contacts Friends").wait_for_appearance()
touch(Template(r"tpl1695116539031.png", record_pos=(-0.472, -0.771), resolution=(1242, 2208)))

#Friend Information Page

touch(Template(r"tpl1695117338509.png", record_pos=(-0.399, 0.206), resolution=(1242, 2208)))
sleep(2)

touch(Template(r"tpl1695117530256.png", record_pos=(-0.319, -0.335), resolution=(1242, 2208)))
sleep(2)
touch(Template(r"tpl1695116539031.png", record_pos=(-0.472, -0.771), resolution=(1242, 2208)))
sleep(2)
touch(Template(r"tpl1695117813243.png", record_pos=(-0.001, -0.302), resolution=(1242, 2208)))
sleep(4)
poco("Hangup").click()
sleep(2)
touch(Template(r"tpl1695117062172.png", record_pos=(0.308, -0.348), resolution=(1242, 2208)))

sleep(4)
poco("Hangup").click()
touch(Template(r"tpl1695116539031.png", record_pos=(-0.472, -0.771), resolution=(1242, 2208)))

#Setting Page--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#My Profile
touch(Template(r"tpl1695174540073.png", record_pos=(0.251, 0.093), resolution=(1242, 2208)))

touch(Template(r"tpl1695174598943.png", record_pos=(0.407, -0.595), resolution=(1242, 2208)))
#Setting Avatar from open camera

touch(Template(r"tpl1695174650155.png", record_pos=(0.424, -0.552), resolution=(1242, 2208)))
poco("Open camera").wait_for_appearance()
poco("Open camera").click()
poco("PhotoCapture").wait_for_appearance()
poco("PhotoCapture").click()
poco("Use Photo").wait_for_appearance()
poco("Use Photo").click()
sleep(4)

#Setting Avatar from gallery
touch(Template(r"tpl1695174650155.png", record_pos=(0.424, -0.552), resolution=(1242, 2208)))
poco("Open gallery").wait_for_appearance()
poco("Open gallery").click()
sleep(1)
poco("Screenshot, September 19, 1:16 PM").click()
sleep(2)

#Setting Avatar from System default
touch(Template(r"tpl1695174650155.png", record_pos=(0.424, -0.552), resolution=(1242, 2208)))
poco("System default").wait_for_appearance()
poco("System default").click()
touch(Template(r"tpl1695176125484.png", record_pos=(-0.118, 0.446), resolution=(1242, 2208)))

sleep(2)



#Edit Nick Name
touch(Template(r"tpl1695176168283.png", record_pos=(-0.348, -0.422), resolution=(1242, 2208))) 
text("1")
poco("Save").click()
touch(Template(r"tpl1695176168283.png", record_pos=(-0.348, -0.422), resolution=(1242, 2208))) 
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
text("888888")
sleep(5)

#Multifunction Menu--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#create new group
touch(Template(r"tpl1695181628951.png", record_pos=(0.431, -0.784), resolution=(1242, 2208)))
poco("New Group").click()
text("testgroup")
poco("Topic").click()
text("QA")
poco("Create").click()
sleep(1)
touch(Template(r"tpl1695116539031.png", record_pos=(-0.472, -0.771), resolution=(1242, 2208)))

#Invite
touch(Template(r"tpl1695181628951.png", record_pos=(0.431, -0.784), resolution=(1242, 2208)))
poco("Invite contact").click()
touch(Template(r"tpl1695090634575.png", record_pos=(-0.161, 0.235), resolution=(1242, 2208)))
touch(Template(r"tpl1695090685537.png", record_pos=(0.385, -0.701), resolution=(1242, 2208)))
poco("Close").wait_for_appearance()
poco("Close").click()

#Scan
touch(Template(r"tpl1695181628951.png", record_pos=(0.431, -0.784), resolution=(1242, 2208)))
poco("Scan").click()
poco("Scan").wait_for_appearance()
poco("Close").click()

#Read all
touch(Template(r"tpl1695181628951.png", record_pos=(0.431, -0.784), resolution=(1242, 2208)))
poco("Read all").click()
sleep(3)

#MyQrcode
touch(Template(r"tpl1695181628951.png", record_pos=(0.431, -0.784), resolution=(1242, 2208)))
poco("My QR code").click()
poco("My QR code").wait_for_appearance()
poco("Close").click()


stop_app("im.shaberi.app.uat")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True