import os
import threading
from functools import partial

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox

from operations import FolderOrganizer

cwd = os.getcwd()

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()

		self.folder_path = None
		self.features = ['Folder Info', 'File Count', 'Organize Files', 'Move Files', 'Delete Files']
		self.current_feature = None
		self.btn_list = []
		self.ext = tk.StringVar()

		self.folder_count = 0
		self.file_count = 0
		self.folder_size = 0
		self.folder_cdate = None

		self.draw_frames()
		self.draw_home_widgets()

	def draw_frames(self):
		self.header = tk.Frame(self, width=400, height=60, bg='#505050')
		self.header.grid(row=0, column=0, columnspan=5)
		self.header.grid_propagate(False)

		self.appname = tk.Label(self.header, text='Folder Organizer', fg='white',
					bg='#505050', font='verdana 22', width=23)
		self.appname.grid(row=0, column=0, pady=5)

		self.body = tk.Frame(self, width=400, height=240, bg='white')
		self.body.grid(row=1, column=0)
		self.body.grid_propagate(False)

		self.folder_fr = tk.Frame(self.body, width=400, height=80, bg='white', relief=tk.RIDGE)
		self.folder_fr.grid(row=0, column=0, columnspan=5)
		self.folder_fr.grid_propagate(False)

		self.buttons_fr = tk.Frame(self.body, width=160, height=160, bg='white')
		self.buttons_fr.grid(row=1, column=0, columnspan=2)
		self.buttons_fr.grid_propagate(False)

		self.info_fr = tk.Frame(self.body, width=240, height=160, bg='white')
		self.info_fr.grid(row=1, column=2, columnspan=3)
		self.info_fr.grid_propagate(False)


	def draw_home_widgets(self):
		self.select_dir = ttk.Button(self.folder_fr, text='Select Folder', command=self.select_folder)
		self.select_dir.grid(row=0, column=2, pady=5, padx=160)

		self.dir_label = tk.Label(self.folder_fr, text='', fg='#E8175D', bg='white', font='verdana 12',
						wraplength=400, height=2)
		self.dir_label.grid(row=1, column=0, columnspan=5)

	def draw_buttons(self):
		rindex = 0
		for text in self.features:
			btn = tk.Button(self.buttons_fr, text=text, width=12,
					relief=tk.RAISED, bg='dodgerblue3', fg='white')
			btn.config(command=partial(self.set_selection, btn, text))
			btn.grid(row=rindex, column=0, padx=30, pady=3)
			self.btn_list.append(btn)
			rindex += 1

	def set_selection(self, widget, text):
		for w in self.buttons_fr.winfo_children():
			w.config(relief=tk.FLAT, bg='dodgerblue3')

		widget.config(relief=tk.RAISED, bg='green')
		self.ext.set('')

		if text == self.features[0]:
			folder_info = self.FOrganizer.get_meta()
			fsize, fcount, filecount, creation_time = folder_info
			self.draw_folder_info_frame(fsize, fcount, filecount, creation_time)
		if text == self.features[1]:
			self.draw_filecount_frame()
		if text == self.features[2]:
			self.draw_organize_file_frame()
		if text == self.features[3]:
			self.draw_move_file_frame()
		if text == self.features[4]:
			self.draw_delete_file_frame()

	def select_folder(self):
		path = filedialog.askdirectory(initialdir=cwd, title='Choose Folder to Organize')
		if path:
			self.folder_path = path
			self.dir_label['text'] = self.folder_path

			self.FOrganizer = FolderOrganizer(self.folder_path)

			if not len(self.buttons_fr.winfo_children()):
				self.draw_buttons()
			self.set_selection(self.btn_list[0], self.features[0])

	def draw_folder_info_frame(self, fsize, fcount, fileCount, creation_time):
		for widget in self.info_fr.winfo_children():
			widget.destroy()

		tk.Label(self.info_fr, text=fsize, width=15, height=2, font='verdana 18',
					bg='white', anchor='w').grid(row=0, column=0, columnspan=5)
		tk.Label(self.info_fr, text='Subfolders', bg='white', width=8).grid(row=1, column=0)
		tk.Label(self.info_fr, text=fcount, bg='white', font='verdana 13').grid(row=1, column=1)
		tk.Label(self.info_fr, text='files', bg='white', width=8, anchor='e').grid(row=1, column=2)
		tk.Label(self.info_fr, text=fileCount, bg='white', font='verdana 13').grid(row=1, column=3)
		tk.Label(self.info_fr, text='Created on', bg='white').grid(row=2, column=0, pady=3)
		tk.Label(self.info_fr, text=creation_time, bg='white').grid(row=2, column=1, columnspan=3, pady=3)

	def draw_filecount_frame(self):
		for widget in self.info_fr.winfo_children():
			widget.destroy()

		tk.Label(self.info_fr, text='Enter Search term to count files', font='verdana 10',
				).grid(row=0,column=0, columnspan=5, pady=(10,7))
		self.entry = ttk.Entry(self.info_fr, textvariable=self.ext, width=14)
		self.entry.grid(row=1, column=0, columnspan=3)
		ttk.Button(self.info_fr, text='Search', command=self.get_file_count).grid(row=1, column=4)
		self.lb1 = tk.Label(self.info_fr, text='', font='verdana 24', anchor='w', bg='white')
		self.lb1.grid(row=3, column=0, pady=14)
		self.lb2 = tk.Label(self.info_fr, text='', anchor='sw', bg='white')
		self.lb2.grid(row=3, column=1, columnspan=3, pady=14)

		self.entry.bind('<Return>', self.get_file_count)

	def draw_organize_file_frame(self):
		for widget in self.info_fr.winfo_children():
			widget.destroy()

		text = 'This feature will sort all files\n and move/organize them\n in new folders. No files\n will be deleted'

		tk.Label(self.info_fr, text=text, font='verdana 10', fg='blue').grid(row=0,column=0, columnspan=5, pady=(10,7))
		ttk.Button(self.info_fr, text='Organize', command=self.organize).grid(row=1, column=0, columnspan=5)

		self.lbl = tk.Label(self.info_fr, text='', font='verdana 12', bg='white', fg='green')
		self.lbl.grid(row=2, column=0, columnspan=5, pady=5)

	def draw_move_file_frame(self):
		for widget in self.info_fr.winfo_children():
			widget.destroy()

		self.filetype = tk.StringVar()
		self.filetype.trace_add('write', self.update_destbtn)

		tk.Label(self.info_fr, text='Enter file extension with . to move files', font='verdana 8',
				).grid(row=0,column=0, columnspan=5, pady=(10,7))
		self.entry = ttk.Entry(self.info_fr, textvariable=self.filetype, width=14)
		self.entry.grid(row=1, column=0, columnspan=3)
		self.btn = ttk.Button(self.info_fr, text='Destination', state=tk.DISABLED,
					command=self.choose_destination)
		self.btn.grid(row=1, column=4)
		self.lbl = tk.Label(self.info_fr, text='', fg='green', bg='white', anchor='w')
		self.lbl.grid(row=3, column=0, columnspan=5)
		self.btn1 = ttk.Button(self.info_fr, text='Move Files', command=self.move_files)
		self.lb1 = tk.Label(self.info_fr, text='', font='verdana 12', anchor='w', bg='white',
						 fg='dodgerblue3')
		self.lb1.grid(row=4, column=0, pady=14, columnspan=5)
		self.lb1.grid_forget()
		self.update_idletasks()

	def draw_delete_file_frame(self):
		for widget in self.info_fr.winfo_children():
			widget.destroy()

		tk.Label(self.info_fr, text='Enter file extension to delete files', font='verdana 10',
				).grid(row=0,column=0, columnspan=5, pady=(10,7))
		self.entry = ttk.Entry(self.info_fr, textvariable=self.ext, width=14)
		self.entry.grid(row=1, column=0, columnspan=3)
		ttk.Button(self.info_fr, text='Delete', command=self.delete_files).grid(row=1, column=4)
		tk.Label(self.info_fr, text='Warning! Doing this will delete\n files with this extension permanently',
					 fg='red', bg='white', anchor='w').grid(row=3, column=0, columnspan=5)
		self.lb1 = tk.Label(self.info_fr, text='', font='verdana 12', anchor='w', bg='white', fg='dodgerblue3')
		self.lb1.grid(row=4, column=0, pady=14, columnspan=5)
		self.update_idletasks()

		self.entry.bind('<Return>', self.delete_files)

	def get_file_count(self, event=None):
		term = self.ext.get()
		if term:
			filecount = self.FOrganizer.get_filecount(term)
			self.lb1['text'] = filecount
			self.lb2['text'] = 'files found'
			self.ext.set('')

	def delete_files(self, event=None):
		extension = self.ext.get()
		if extension:
			print(extension)
			filecount = self.FOrganizer.delete_files(extension)
			self.lb1['text'] = filecount
			self.ext.set('')

	def update_destbtn(self, var, indx, mode):
		extension = self.filetype.get()
		if extension.startswith('.') and len(extension) > 2:
			self.btn['state'] = tk.NORMAL

	def choose_destination(self):
		path = filedialog.askdirectory(initialdir=cwd, title='Choose Destination')
		if path:
			if self.folder_path == path:
				messagebox.showinfo('FolderOrganizer','Cannot move files to same folder \nchoose another')
			else:
				self.dest = path
				folder = os.path.basename(path)
				self.lbl['text'] = f'Doing this will move all files\n with this extension to {folder}'
				self.btn1.grid(row=4, column=0, columnspan=5, pady=5)

	def move_files(self):
		extension = self.filetype.get()
		filecount = self.FOrganizer.move_files(extension, self.dest)
		self.btn1.grid_forget()
		self.lb1['text'] = filecount
		self.lb1.grid(row=4, column=0, pady=14, columnspan=5)
		self.filetype.set('')
		self.btn['state'] = tk.DISABLED

	def organize(self):
		filecount = self.FOrganizer.organize_files()
		self.lbl['text'] = filecount
		

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('400x300+380+200')
	root.title('File Organizer')

	app = Application(master=root)
	app.mainloop()