import math
import fitz
from tkinter import PhotoImage

class PDFMiner:
	def __init__(self, filepath):
		self.filepath = filepath
		self.pdf = fitz.open(self.filepath)
		self.first_page = self.pdf.loadPage(0)
		self.width, self.height = self.first_page.rect.width, self.first_page.rect.height
		print(self.width, self.height)

		zoomdict = {800:0.8, 700:0.6, 600:0.7, 500:0.8}
		width = int(math.floor(self.width / 100.0)) * 100
		print(width)
		self.zoom = zoomdict.get(width, 0)


	def get_metadata(self):
		metadata = self.pdf.metadata
		numPages = self.pdf.pageCount

		return metadata, numPages

	def get_page(self, page_num):
		page = self.pdf.loadPage(page_num)
		if self.zoom:
			mat = fitz.Matrix(self.zoom, self.zoom)
			pix = page.getPixmap(matrix=mat)
		else:
			pix = page.getPixmap()
		px1 = fitz.Pixmap(pix, 0) if pix.alpha else pix
		imgdata = px1.getImageData('ppm')
		return PhotoImage(data=imgdata)

	def get_text(self, page_num):
		page = self.pdf.loadPage(page_num)
		text = page.getText('text')
		return text 