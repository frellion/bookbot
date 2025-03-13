def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

#char_freq is a list of "char":"num" dictionaries
def print_report(book_source, word_count, char_freq):
	print("============ BOOKBOT ============")
	print(f"Analysing book found at {book_source}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for char in char_freq:
		if char["char"].isalpha():
			print(f"{char["char"]}: {char["num"]}")

	print("============= END ===============")

def main():
	import sys

	from stats import count_words
	from stats import char_stats
	from stats import dict_to_list_conversion
	from stats import get_char_freq

	if (len(sys.argv)!=2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_source = sys.argv[1]
	book_text = get_book_text(book_source)
	word_count = count_words(book_text)
	#print(f"{word_count} words found in the document")
	#print(char_stats(book_text))
	#get_char_freq(dict_to_list_conversion(char_stats(book_text)))
	print_report(book_source, word_count, get_char_freq(dict_to_list_conversion(char_stats(book_text))))

main()
