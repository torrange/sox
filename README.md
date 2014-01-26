Sox
===

Batch SRC tool for Sound eXchange (Sox)

Install for Ubuntu systems:


1. Install Sox & Git
	
		sudo apt-get install sox git



2. Clone this repo:

		git clone https://github.com/torrange/sox.git



3. Copy to /usr/local/bin and make executable:

		sudo cp ./sox/sox_batch.py /usr/local/bin/soxcnv
		sudo chmod +x /usr/local/bin/soxcnv


4. Navigate to the directory containing source files for conversion and run:

		soxcnv 


To specify the sample-rate of the output files, just run 'soxcnv' with the desired sample-rate as the first argument, like so:

		soxconv 88200
		
	
A new directory named "converted" will have been created in the current working directory and
all processed files are stored there. 
