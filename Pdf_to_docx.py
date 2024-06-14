from pdf2docx import Converter

pdf_file = 'Anti.pdf'
docx_file = 'Anti.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()