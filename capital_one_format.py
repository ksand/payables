#
# capital_one_stage1.py
#
# Raw data downloaded from Capital One in PDF format.
# File is opened in Adobe Reader and saved as text
# Text must be manually edited in a text editor to show only charges
#
import re

def readfile(filename):
	infile = open(filename, "r")
	print "Open ", infile.name
	for buf in infile:
		outbuf = ''
		tmpbuf = ''
		buf = buf.rstrip()
		m = re.match('[1-9][0-9]', buf)
		if m is not None:
			outbuf = buf[:2] + '\t' + buf[3:5] + '\t' + buf[6:10]
			tmpbuf = buf[10:]
		else:
			m = re.match('[1-9][ ]', buf)
			if m is not None:
				outbuf = buf[:1] + '\t' + buf[2:4] + '\t' + buf[5:8]
				tmpbuf = buf[9:]
		try:
			index = tmpbuf.rindex('$')
			outbuf = outbuf + '\t' + tmpbuf[:index] + '\t' + tmpbuf[index:].strip('$ ')
		except ValueError:
			pass
		print outbuf
		outfile.write(outbuf + '\n');
	infile.close()

print "Capital One Raw Data"
datadir = "C:\\Users\\Karl\\Documents\\Expenses\\Raw Data\\"
print datadir 
outfile = open("capital-one.txt", "wb")
readfile(datadir + "Stmnt_012014_9881.txt")
readfile(datadir + "Stmnt_022014_9881.txt")
readfile(datadir + "Stmnt_032014_9881.txt")
readfile(datadir + "Stmnt_042014_9881.txt")
readfile(datadir + "Stmnt_052014_9881.txt")
readfile(datadir + "Stmnt_062014_9881.txt")
readfile(datadir + "Stmnt_072014_9881.txt")
readfile(datadir + "Stmnt_082014_9881.txt")
outfile.close()

