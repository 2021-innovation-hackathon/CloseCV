# Requires "requests" to be installed (see python-requests.org)
import requests
from PIL import Image
import os

filepath = 'AI/yolov5/result/exp'
fname = os.listdir(filepath)

for name in fname:
    imgfile = Image.open('AI/yolov5/result/exp/%s' %name)
    imgw, imgh = imgfile.size
    imgfile = imgfile.crop((0, 0, imgw, imgh-20))
    imgfile.save('AI/yolov5/result/exp/%s' %name)

for name in fname:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('AI/yolov5/result/exp/%s' %name, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'YNfL8ZQsxdrZkcrPJXNCZpps'},
    )
    if response.status_code == requests.codes.ok:
        tf = os.path.isdir('AI/imgconv/process')
        if tf == False:
            os.makedirs('AI/imgconv/process')
        with open('AI/imgconv/process/%s.png' %name[:-4], 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
    os.remove('AI/yolov5/result/exp/%s' %name)

os.rmdir('AI/yolov5/result/exp')