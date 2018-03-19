import glob, json
from random import randint
import shutil


already = json.load(open('already_uploaded.json'))
all = []



letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','punct']

for letter in letters:

	for filename in glob.iglob('/Volumes/Byeeee/littlebooklists/' + letter + '/*'):

		if filename not in already:
			all.append(filename)
	
	print(len(all))



this_run = []

for x in range(1,1001):

	useKey = all[randint(0,len(all)-1)]

	if useKey not in this_run:

		this_run.append(useKey)
		already.append(useKey)

		key = useKey.split('/')[len(useKey.split('/'))-1]
		shutil.copytree(useKey, 'upload/'+key)



json.dump(already,open('already_uploaded.json','w'))



