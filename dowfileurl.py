import os
import urllib.request

folder = "downloads"
if not os.path.exists(folder):
    os.makedirs(folder)

for i in range(1, 32):

    new = str(i)
    if i < 10:
        new = "0" + str(i)

    file_name = "202302"+ str(new) +"_user_photo.csv"
    url = "https://mycloset.aeon.com.vn/storage/photo/log/" + file_name
    try:
        urllib.request.urlretrieve(url, folder + "/" + file_name)
        print('done downloading '+file_name)
    except urllib.error.HTTPError as e:
        print("Error:",file_name, "File not found")



print('done downloading')