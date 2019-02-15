# 	A script to help a person trying to 
# 	print out :
# 		some of special function registers used
# 		a structure containing as much information as possible to write assembly code
# 	
# 	additional features that can be added
# 		+ help on writing jmps, but adding information about offsets need
# 			+ currently, I had to relay on reading data sheet while writing the assambly form the data returned
# 		+ embedd help about assembly language into the program so that I can be called and used
# 		+ include comments??
# 		+ suggest  some stuff??? like code optimization or labeling???
# 	what can be cooler??
# 		+ write assembler for arbitary assembly language??
# 			+ nope?? intel 8051 one
# 			+
# 		+ how does it resolve labeling???

from asm_def import *
PC=0
memory=dict()
specialx=[]
def intrepretline(line):
	"""
		read intelhex file line and store hex numbers in their respective locations in memory
		indexed as string of the hex value of the location in memory(length 4, padded with zeros infront)
	
	"""
	starter=line[0]
	record_length=line[1:3]
	start_address=line[3:7]
	record_type=line[7:9]
	checksum=line[-3:]
	data=line[9:-3]
	start_address_hex="0x"+start_address
	if record_length=="01":
		return 0
	def address(n):
		start_address_hex_n=hex(int(start_address_hex,16)+n)[2:]
		if len(start_address_hex_n)==3:
			start_address_hex_n="0"+start_address_hex_n
		if len(start_address_hex_n)==2:
			start_address_hex_n="00"+start_address_hex_n
		if len(start_address_hex_n)==1:
			start_address_hex_n="000"+start_address_hex_n
		return start_address_hex_n

	for i in range(int(record_length,16)):
		memory[address(i).upper()]=data[i*2:i*2+2]

def start():
	"""
		monitor program
			+ receive intel hex file name
			+ print out information that can be of help while reverse engineering it
	"""
	f=input("enter the name of file without .hex: ")
	R=open(f+".hex","r")
	for line in R.readlines():
		intrepretline(line)
	data=[]
	for i,j in memory.items():
		data.append(j)
	pc=0
	program=[]
	while pc<len(data):
		data_i=data[int(pc)]
		data[pc]
		opcode_part=opcodes[data[pc]]
		# size=byte_size[data_i]
		size=len(data_i)
		if size==2:
			data1=data[int(pc)+1]
			program.append([pc,data_i,opcode_part,data1])
		if size==3:
			data1=data[int(pc)+1]
			data2=data[int(pc)+2]
			program.append([pc,data_i,opcode_part,data1,data2])
		if size==1:
			program.append([pc,data_i,opcode_part])
		pc=pc+size
	for i in program:
		if i[-1] in SFR_name:	
			specialx.append([i[-1],SFR_name[i[-1]]])
			i[-1]=SFR_name[i[-1]]
			pass
	if len(specialx)>=1:
		print("special function registers used")
		for i in specialx:
			print(i)
	print("a summary of the assembler code [[pc,opcode,mnemonic,operand1,operand2]]")
	print("currently only operand 2 can be replace with special fx name if it is ")
	for line in program:
		print(str(line)[:])
	R.close()
	start()


if __name__=="__main__":
	print("Dessamble helps extract more information to help you dessamble intrepret INTEL .hex into .ASM")
	print("Input a file and get a summary about the intel hex that can help you write assembly equivalence of the hex\n")
	start()

# :0B0010006E20696E20362E3131352144

# :00000001FF
# {'0000': '74', '0001': '00', '0002': '85', '0003': 'E0', '0004': '90', '0005': 'D2', '0006': '92', '0007': '80', '0008': 'F7', '0009': '50', '000A': '61', '000B': '72', '000C': '74', '000D': '79', '000E': '20', '000F': '6F', '0010': '6E', '0011': '20', '0012': '69', '0013': '6E', '0014': '20', '0015': '36', '0016': '2E', '0017': '31', '0018': '31', '0019': '35', '001A': '21'}
# [[0, '74', 'MOV', '00'], [2, '85', 'MOV', 'E0', '90'], [5, 'D2', 'SETB', '92'], [7, '80', 'SJMP', 'F7'], [9, '50', 'JNC', '61'], [11, '72', 'ORL', '74'], [13, '79', 'MOV', '20'], [15, '6F', 'XRL'], [16, '6E', 'XRL'], [17, '20', 'JB', '69', '6E'], [20, '20', 'JB', '36', '2E'], [23, '31', 'ACALL', '31'], [25, '35', 'ADDC', '21']]
# # [Finished in 0.5s]