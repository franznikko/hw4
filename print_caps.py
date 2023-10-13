def allcaps(func):
	def wrapper():
		results = func()
		return result.upper()
	return wrapper

