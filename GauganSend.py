
import  requests,re, shutil, os, base64, random, string
from datetime import date
import concurrent.futures
from more_itertools import grouper

today = date.today()

style = 8
indir = "C:\\Users\\jojop\\Desktop\\AI Convert Fast\\GoHArd\\IN"
outdir = "C:\\Users\\jojop\\Desktop\\AI Convert Fast\\GoHArd\\OUT"

def getUrl():
	print('Getting new server address...')
	r = requests.get('http://gaugan.org/gaugan2/demo.js')
	urls = re.findall(r'\'(http.*?://.*?/)\'', re.search(r'urls=.*?;', r.text)[0])
	return urls[0]


def get_image(img):
	print(f'Processing image \'{img}\'')
	with open(indir + "\\" + img, "rb") as f:
		imgb64 = 'data:image/png;base64,' + str(base64.b64encode(f.read()))[2:-1]
	name = today.strftime("%d/%m/%Y") + "," + ''.join(random.choice(string.digits) for _ in range(13)) + "-" + ''.join(random.choice(string.digits) for _ in range(9))
	POSTdata = {
		'name': name,
		'masked_segmap': imgb64,
		'style_name' : str(style),
		'caption' : '',
		'enable_seg' : 'true',
		'enable_edge' : 'false',
		'enable_caption' : 'false',
		'enable_image' : 'false',
		'use_model2' : 'false',
	}

	requests.post(url + 'gaugan2_infer', data = POSTdata)

	POSTdata = {
		'name': name,
	}
	print(url + 'gaugan2_receive_output')
	r = requests.post(url + 'gaugan2_receive_output', data = POSTdata, stream = True)
	with open(outdir + '//' + img.split('.')[0] + '.jpg','wb') as f:
		shutil.copyfileobj(r.raw, f)
		
		

def main(items):
	for img in items:
		get_image(img)

def execute():
	items = os.listdir(indir)
	executor = concurrent.futures.ProcessPoolExecutor(10)
	futures = [executor.submit(main, group) 
		for group in grouper(5, items)]
	concurrent.futures.wait(futures)
	print("done")

url = getUrl()

if __name__ == "__main__":
	execute()
