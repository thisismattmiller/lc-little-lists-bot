from PIL import Image, ImageDraw, ImageFont
import math, json, sys, os
import uuid
import tqdm
import multiprocessing



def draw_img(d):


	font = ImageFont.truetype('NotoSans-Regular.ttf', 14)


	longest_title = 0
	for t in d['titles']:
		this_size = font.getsize(t)[0]

		longest_title =  this_size if this_size > longest_title else longest_title


	if longest_title > 700:
		longest_title = 700


	height = len(d['titles']) * 18

	height = height + 4
	longest_title = longest_title + 6
	canvas = Image.new('RGBA', (longest_title,height), (255,255,255,255))
	draw = ImageDraw.Draw(canvas)



	for idx, t in enumerate(d['titles']):

		if font.getsize(t)[0] > 700:

			new_t = ""
			for letter in t:
				new_t = new_t + letter
				
				if font.getsize(new_t)[0] >= 690:
					new_t = new_t.strip() + '...'
					break

			t = new_t




		draw.text((3, 18*idx+2), text=t, font=font, fill=(0, 0, 0,200))

	# print(d)
	# print(longest_title)
	# print(height)

	uuidstr = str(uuid.uuid4())

	os.mkdir('/Volumes/Byeeee/littlebooklists/'+list_letter+'/'+uuidstr)

	canvas.save('/Volumes/Byeeee/littlebooklists/'+list_letter+'/'+uuidstr + '/image.png', "PNG")

	json.dump({'title':d['title']},open('/Volumes/Byeeee/littlebooklists/'+list_letter+'/'+uuidstr + '/data.json','w'))

	# print(counter,'/',len(data),'/Volumes/Byeeee/littlebooklists/'+list_letter+'/'+uuidstr)
	return('/Volumes/Byeeee/littlebooklists/'+list_letter+'/'+uuidstr)



letters = ['u','v','w','x','y','z','punct']
for list_letter in letters:

	# list_letter = 'g'

	data = json.load(open('data_out/' +list_letter+'.json'))
	result_count = []

	for result in tqdm.tqdm(multiprocessing.Pool(8).imap_unordered(draw_img, data), total=len(data)):	

		result_count.append(result)
		print(len(result_count),'/',len(data), result)


