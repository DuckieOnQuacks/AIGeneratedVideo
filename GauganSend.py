import  requests,re, shutil, os, base64, random, string
from datetime import date
import concurrent.futures
import itertools
from more_itertools import grouper

today = date.today()

style = 2
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
    # Prints the name of the image being processed
	print(f'Processing image \'{img}\'')

    # Create a session object
	session = requests.Session()
    # Open the image file and read it
	with open(os.path.join(indir, img), "rb") as f:
        # Encode the image file in base64 format
		imgb64 = 'data:image/png;base64,' + str(base64.b64encode(f.read()))[2:-1]

    # Create a unique name for the image using the current date, random digits
	name = today.strftime("%d/%m/%Y") + "," + ''.join(random.choice(string.digits) for _ in range(13)) + "-" + ''.join(random.choice(string.digits) for _ in range(9))
    # Create a data payload for the POST request
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
    # Send the POST request with the data payload to the specified URL
	session.post(url + 'gaugan2_infer', data = POSTdata)

    # Prepare another data payload for another POST request
	POSTdata = {
		'name': name,
	}
    # Print the URL for the second POST request
	print(url + 'gaugan2_receive_output')

    # Send the POST request and get the response in stream mode
	r = session.post(url + 'gaugan2_receive_output', data = POSTdata, stream = True)

    # Open a new file with the output directory, original filename and jpg extension
	with open(os.path.join(outdir, img.split('.')[0] + '.jpg'),'wb') as f:
        # Copy the response in the new file
		shutil.copyfileobj(r.raw, f)
    # close the session
	session.close()

def main(items):
	for img in items:
		get_image(img)

######################
def execute():
	items = os.listdir(indir)
	executor = concurrent.futures.ProcessPoolExecutor(5)
	groups = grouper(5, items, fillvalue=None)
	futures = [executor.submit(main, group) for group in groups]
	return concurrent.futures.wait(futures, timeout=None)

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

url = getUrl()

if __name__ == "__main__":
	execute()
