def merge_list(list1, list2):

	if not (isinstance(list1, list) and isinstance(list2,list)):
		raise TypeError("Both inputs should be lists.")
	
	for num in list1 + list2:
		if not isinstance(num, int):
			raise TypeError("List contains non-interger elements.")
	
	merge = list1 + list2

	return merge

