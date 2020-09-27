 # 이 파일과 동일한 디렉터리에
 # wget --user huge --password file (사이트 주소 ...... evil1.jpg)로 사진 다운로드 받아야 합니다.

file_des = open("evil2.gfx", 'rb')
byte_arr = bytearray(file_des.read())

img = list()
for i in range(5):
	img.append(byte_arr[i::5])

for i in range(5):
	with open("py" + str(i) + ".jpg", "wb") as write_des:
		write_des.write(img[i])



