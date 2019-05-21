import cv2
import base64
import numpy as np
import time

from aip import AipBodyAnalysis

# 在百度云中申请，每天各接口有 500 次调用限制.
startTime = time.time()
APP_ID = '16308811'
API_KEY = 'pW14G1oDOtDpG3puUiL8a7YB'
SECRET_KEY = 'a5nnuRxFgIuKua5KADaclavTwkZbLvxc'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

imgfile = './333.jpg'
ori_img = cv2.imread(imgfile)
height, width, _ = ori_img.shape

with open(imgfile, 'rb') as fp:
    img_info = fp.read()

seg_res = client.bodySeg(img_info)
labelmap = base64.b64decode(seg_res['labelmap'])
nparr = np.fromstring(labelmap, np.uint8)
labelimg = cv2.imdecode(nparr, 1)
labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
new_img = np.where(labelimg == 1, 255, labelimg)
maskfile = imgfile.replace('.jpg', '_mask.png')
cv2.imwrite(maskfile, new_img)

res_imgfile = imgfile.replace('.jpg', '_res.jpg')
result = cv2.bitwise_and(ori_img, new_img)
cv2.imwrite(res_imgfile, result)
endTime = time.time()
print("useTime: ", endTime - startTime)
print('Done.')