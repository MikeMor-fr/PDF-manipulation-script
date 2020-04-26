import PyPDF2
import sys


with open('Dummy.pdf', 'rb') as file: # rb : "b" for allowing reading binary files
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	page = reader.getPage(0) # page object, get the fis=rst page
	page.rotateCounterClockwise(90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)

	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)
