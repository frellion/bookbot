# returns number of words
def count_words(content):
        return len(content.split())


# returns character count
def char_stats(content):
	char_dict ={}
	for char in content:
		if char.lower() not in char_dict:
			char_dict[char.lower()] = 1
		else:
			char_dict[char.lower()] +=1
	return char_dict


# creates list of char:num dictionaries
def dict_to_list_conversion(char_dict):
	dict_list = []
	for char in char_dict:
		working_dict = {}
		working_dict["char"] =  char
		working_dict["num"]= char_dict[char]
		dict_list.append(working_dict)
	return(dict_list)

#sort helper
def sort_key(dict):
	return dict["num"]

# sort list of char:num dictionaries (descending)
def get_char_freq(dict_list):
	dict_list.sort(reverse=True, key=sort_key)
	return(dict_list)
