import binascii
import codecs
import binhex
#def writefile():
	#with open("")

def readfile(res_f): 
	with open("0A32eTdBKayjCWhZqDOQ.bytes", 'r') as init_file:
		for f in init_file:
    			#data = f.readline()
			arr = f.split()
			for i in range(len(arr)):
				if(i != 0):
					res_f.write("%s" % codecs.decode(arr[i],"hex"))
			res_f.write("\n")
	return res_f

if __name__ == "__main__":
      file = open("result.txt", 'w+')
      file = readfile(file)
      file.close()
