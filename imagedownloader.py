import requests
import os.path

save_path = 'D:\\Pictures\\Wallpapers'
fileName = 'C:\\Users\\erick\\Documents\\pythonRead\\wallpapers.txt'

print(fileName);

with open(fileName) as txt:
    for line in txt:
        line = line.rstrip('\n')
        r = requests.get(line, stream=True);
        picName = line.rsplit("/", 1)[1]
        print(picName);
        picName = os.path.join(save_path, picName)

        with open(picName, 'wb') as f:
            f.write(r.content);
