from io import BufferedReader

def fillnull(array:list, length:int) -> None:
	"""ensurses the array is filled with None up till the required length.
		x = [1, 2]
		fillnull(x, 5)
		print(x) # [1, 2, None, None, None]
	"""
	array += [None]*(
		length-len(array)
	)

def normalisematrix(matrix:[list, ...]) -> None:
	"""ensures rows of a matrix have the same length"""
	length = max(*[len(_) for _ in matrix])
	for i in matrix:
		fillnull(i, length)

def readcsv(file:BufferedReader) -> list:
	content = file.read()
	result = list(
		map(
			lambda line: list(
				map(
					lambda item: item.strip(),
					line.strip().split(",")
				)
			),
			content.strip().split("\n")
		)
	)
	normalisematrix(result)
	return result

if __name__ == "__main__":
	with open("data.csv") as  csv:
		data = readcsv(csv)
	print(data)
