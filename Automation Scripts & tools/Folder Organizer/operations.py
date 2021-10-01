import os
import time
import json
import shutil

with open('filetypes.json') as f:
	FILETYPES = json.load(f)

class FolderOrganizer():
	def __init__(self, path):
		self.path = path

	def get_meta(self):
		folder_list = []
		filecount = 0
		total_size = os.path.getsize(self.path)

		for dirpath, dirname, filenames in os.walk(self.path):
			if dirname not in folder_list:
				folder_list.append(dirname)
			for file in filenames:
				fp = os.path.join(dirpath, file)
				# skip if it is symbolic link
				if not os.path.islink(fp):
					filecount += 1
					total_size += os.path.getsize(fp)

		ts = total_size / (1024*1024)
		if ts < 1000:
			ts = f'{ts:.2f} MB'
		else:
			ts = f'{ts/1024:.2f} GB'

		creation_time = time.ctime(os.stat(self.path).st_ctime)
		creation_time = creation_time[4:10] + ' ' + creation_time[-4:] + ', ' + creation_time[11:16]

		return [ts, len(folder_list), filecount, creation_time]

	def get_filecount(self, term):
		filecount = 0
		for file in os.listdir(self.path):
			if term.lower() in file.lower():
				filecount += 1

		return filecount

	def move_files(self, extension, destination):
		filecount = 0
		for file in os.listdir(self.path):
			name, ext = os.path.splitext(file)
			if extension.lower() == ext:
				src = os.path.join(self.path + '/' + file)
				dst = os.path.join(destination + '/' + file)
				shutil.move(src, dst)
				filecount += 1

		return f'{filecount} files moved' if filecount else "0 files moved"

	def delete_files(self, extension):
		filecount = 0
		for file in os.listdir(self.path):
			name, ext = os.path.splitext(file)
			if extension.lower() == ext:
				try:
					os.remove(os.path.join(self.path, file))
					filecount += 1
				except Exception as e:
					print(e)

		return f'{filecount} files deleted permanently' if filecount else "No files exist"

	def organize_files(self):
		filecount = 0
		for file in os.listdir(self.path):
			name, ext = os.path.splitext(file)
			for key in FILETYPES.keys():
				if ext in FILETYPES[key]:
					if not os.path.exists(self.path + '/' + key):
						os.mkdir(self.path + '/' + key)
					src = os.path.join(self.path,file)
					dst = os.path.join(self.path,key,file)
					shutil.move(src, dst)
					filecount += 1

		return f'{filecount} files moved'