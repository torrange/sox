#!/usr/bin/env python2

from subprocess import call
from glob import glob
from sys import exit
from os import mkdir, getcwd
from datetime import date, datetime


class Sox(object):

	def __init__(self, samplerate="44100"):
		self.today = date.strftime(datetime.now(), "%Y%m%d")
		self.samplerate = samplerate
		self.filetypes = ("wav", "aif", "aiff") 
		self.cwd = getcwd()


	def inputFiles(self):
		self.input_files=[]

		for filetype in self.filetypes:
		    intemp=glob(self.cwd+"/*.%s" % (filetype))
		    
		    if intemp >=1:
			for filename in intemp:
			    self.input_files.append(filename)


	def convertFiles(self):

		if len(self.input_files) >=1:
		    
		    global converted_count	
		    converted_count = 0
		    
		    try:
			mkdir(self.cwd+"/converted")
		    except OSError:
			exit("'converted' directory already exists")
		
		    for input_file in self.input_files:
			destination_samplerate = self.samplerate

			_rawfilename=input_file.split("/")
			self.rawfilename =_rawfilename[len(_rawfilename)-1]

			destination_filename = "%s_%s__%s" % (destination_samplerate[0:2], self.today, self.rawfilename )

			call(["sox", input_file, "--rate", destination_samplerate, self.cwd+"/converted/"+destination_filename])

			converted_count += 1  
		    		    
		else:
		    exit("No files to process")


if __name__ == "__main__":
	s=Sox() 
	s.inputFiles()
	s.convertFiles()
	exit("Converted %d files" % converted_count)




