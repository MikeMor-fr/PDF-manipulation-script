import PyPDF2

# Solution

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)

# Explanation

#with open('super.pdf', "rb") as file:
	# read the content of the pdf file
#	reader = PyPDF2.PdfFileReader(file)
	# instance of the writer
#	writer = PyPDF2.PdfFileWriter()

#	with open('wtr.pdf', 'rb') as wtr:
		# read the content of the watermark file
#		mark = PyPDF2.PdfFileReader(wtr)
		# acces to the page with the watermark
#		watermark = mark.getPage(0)

#		for i in range(reader.numPages):
			# acces to the page n° i
#			page = reader.getPage(i)
			# merge the page with the watermark page
#			page.mergePage(watermark)
			# add the page to the writer
#			writer.addPage(page)

#		with open('super_merged.pdf', 'wb') as new_pdf:
			# write the content of the writer into the new_pdf file
#			writer.write(new_pdf)

