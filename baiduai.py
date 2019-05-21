from aip import AipBodyAnalysis
import numpy as np
from cv2 import cv2
import base64
import os


""" 你的 APPID AK SK """
APP_ID = '16308811'
API_KEY = 'pW14G1oDOtDpG3puUiL8a7YB'
SECRET_KEY = 'a5nnuRxFgIuKua5KADaclavTwkZbLvxc'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('./93.jpg')

# """ 调用手势识别 """
# results = client.gesture(image)
# print(results)

# """ 调用图像分割 """
# options = {}
# options["type"] = 'foreground'
# client.bodySeg(image)
res = client.bodySeg(image)
 
foreground = base64.b64decode(res['foreground'])
labelmap = base64.b64decode(res['labelmap'])
scoremap = base64.b64decode(res['scoremap'])
 
nparr_foreground = np.fromstring(foreground,np.uint8)
foregroundimg = cv2.imdecode(nparr_foreground,1)
foregroundimg = cv2.resize(foregroundimg,(1000,1489),interpolation=cv2.INTER_NEAREST)
im_new_foreground = np.where(foregroundimg==1, 10, foregroundimg)
cv2.imwrite('foreground.png', im_new_foreground)
 
nparr_labelmap = np.fromstring(labelmap,np.uint8)
labelmapimg = cv2.imdecode(nparr_labelmap,1)
labelmapimg = cv2.resize(labelmapimg,(1000, 1489),interpolation=cv2.INTER_NEAREST)
im_new_labelmapimg = np.where(labelmapimg==1, 255, labelmapimg)
cv2.imwrite('labelmap.png', im_new_labelmapimg)
 
nparr_scoremap = np.fromstring(scoremap,np.uint8)
scoremapimg = cv2.imdecode(nparr_scoremap,1)
scoremapimg = cv2.resize(scoremapimg,(1000,1489),interpolation=cv2.INTER_NEAREST)
im_new_scoremapimg = np.where(scoremapimg==1, 255, scoremapimg)
cv2.imwrite('scoremap.png', im_new_scoremapimg)