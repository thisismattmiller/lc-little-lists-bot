import json



letters = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','punct']
totals = {}

for letter in letters:

	all_titles = []
	all_titles_split = []
	lookup_title = {}




	with open('data/'+letter+'.txt') as file:


		for line in file:
			line = line.strip()

			all_titles.append(line)

			words = ""
			for idx, word in enumerate(line.split()):
				words = words + ' ' + word
				words = words.strip()
				if idx > 1:
					if words not in lookup_title:
						lookup_title[words] = []

					lookup_title[words].append(line)


			if len(lookup_title) % 10000 == 0:
				print(len(lookup_title))


		good_stuff = []
		for x in lookup_title:
			if len(lookup_title[x]) > 3:

				lookup_title[x] = list(set(lookup_title[x]))
				good_stuff.append({"title":x,"titles":lookup_title[x]})

				print(len(good_stuff))

				# print(x)
				# print(lookup_title[x])


		delete_these = []
		for idx, data in enumerate(good_stuff):

			# print(json.dumps(x,indent=2))

			# see if this title minus the last word is in the list with the same amount of titles
			one_less = " ".join(data['title'].split()[0:len(data['title'].split())-1])
			print(idx,'/',len(good_stuff),'-',len(delete_these))


			totals[letter] = [idx,'/',len(good_stuff),'-',len(delete_these)]
			
			for x in good_stuff:

				if x['title'] == one_less:
					if len(x['titles']) == len(data['titles']):
						delete_these.append(one_less)
						# print(x)
						# print(data)
						# print('---~~~~~')

		output = []
		for x in good_stuff:
			if x['title'] not in delete_these:
				output.append(x)



		json.dump(output,open('data_out/'+letter+'.json','w'),indent=2)
		json.dump(totals,open('totals.json','w'),indent=2)



		# for title in all_titles:

		# 	title_split = title.split()
		# 	max_match = len(title_split)

		# 	for i in reversed(range(max_match)):

		# 		if i > 2:
		# 			words = " ".join(title_split[0:i])

		# 			if words in lookup_title:
		# 				print(title)
		# 				print(lookup_title[words])
		# 				print('------')




	# for title in all_titles_split:

	# 	max_match = len(title)

	# 	for idx, check_against in enumerate(all_titles_split):







