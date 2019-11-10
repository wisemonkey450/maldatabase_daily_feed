import os
import json
import requests
import time

def main():
	fg = open("./Hashes/latest_hashes_{}".format(time.ctime()), 'w')
	with open("./Feed_Files/feed_file.json", 'r') as fd:
		data = fd.read()
	json_obj = json.loads(data)
	for obj in json_obj:
		#fg.write(str(obj['files']))
		#fg.write(', ')
		fg.write(obj['md5'])
		fg.write(', ')
		fg.write(obj['sha256'])
		fg.write('\n\n')
	

if __name__ == "__main__":
	main()
