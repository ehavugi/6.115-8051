# mastercode can be used to put together different hex files together for putting the codes in different location in memory
# 	enter name of master hex file without extension
#	enter name 
		# + first hex file
#		   + second hex file
#			.....
# 			+ enter Y for last file ?
#			downlaod the code and burn it or run it using G8XXX with XXX being the location of code files
#
#
##  6.115 Lab 2 (procastination idea)
# 		Emmanuel HAVUGIMANA
# 		try and first worked week(26 Feb to 3 March)

#  is it possible to simulate 8051 basic stuff?
#  like read and execute Assembly?? do the change that the assembly would to the memory??(???etc..)
#  
def start():
	# print("*",end="",flush=True)
	filex=input('filename without hex: ')
	filex=filex+".hex"
	location=input("start location: ")
	location=int(location,16)
	command=input("Last? Y or N : ")
	filex=open(filex).read()
	filex=filex.split("\n")[:-2]
	# print(filex)
	intelhex=open(f+".hex","a")
	for line in filex:
		# print(line)
		if location==0:
			intelhex.write(line+"\n")
		else:
			start_address=int(line[3:7],16)
			update_start_address=start_address+location
			
			start_address_hex_n=hex(update_start_address)[2:]
			if len(start_address_hex_n)==3:
				start_address_hex_n="0"+start_address_hex_n
			if len(start_address_hex_n)==2:
				start_address_hex_n="00"+start_address_hex_n
			if len(start_address_hex_n)==1:
				start_address_hex_n="000"+start_address_hex_n
			line=line[:3]+start_address_hex_n+line[7:]
			intelhex.write(line+"\n")


	if command.upper()[0]=="Y":
		intelhex.write(":00000001FF"+"\n")
	else:
		pass
		# intelhex.write("\n")

	intelhex.close()
	start()
	



if __name__=="__main__":
	print("Currently supported commands are R and W")
	print("use Rxxxx to read address xxxx and use Wxxxx=yyyy to write data yyyy to address xxxx \n")
	# print(memory)
	f=input("enter name of output file without extension : ")
	intelhex=open("f"+".hex","w")
	intelhex.close()  # to close the thing
	start()