import  requests,re, shutil, os, base64, random, string
from datetime import date
import concurrent.futures
import itertools
from more_itertools import grouper

today = date.today()

style = 1
indir = ".\in"
outdir = '.\out'

def getUrl():
    print('Getting new server address...')
    r = requests.get('http://gaugan.org/gaugan2/demo.js')
    # Regular expression to match the specified format
    pattern = re.compile(r'http://ec2-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}\.us-west-2\.compute\.amazonaws\.com:443/')

    match = pattern.search(r.text)
    if match:
        return match.group()
    else:
        return None


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

######################
def execute():
	items = os.listdir(indir)
	main(items)
'''executor = concurrent.futures.ProcessPoolExecutor(5)
    groups = grouper(5, items, fillvalue=None)
    futures = [executor.submit(main, group) for group in groups]
    return concurrent.futures.wait(futures, timeout=None)

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)
'''
url = getUrl()

if __name__ == "__main__":
	execute()
