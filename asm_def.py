# instructions x byte

## related works  : https://github.com/mboyd/8051Boy  retried or view on 9th march.
## it looks like I can learn something from past works
instructions={"00":1,"01":2,"03":3}
one_byte=["00","04","07","08","09","0A","0B","0C","0D","0E","0E","0F","13","14","16","17","18","19","1A","1B","1C","1D","1E","1F","22","23","26","27","28",
		  "29","2A","2B","2C","2D","2E","2F","32","33","36","37","39","3A","3B","3C","3D","3E","3F","46","47","48","49","4A","4B","4C","4D","4E","4F","56","57",
		  "58","59","5A","5B","5C","5D","5E","5F","66","67","68","69","6A","6B","6C","6D","6E","6F","73","83","84","93","96","97","98","99","9A","9B","9C","9D","9E","9F",
		  "A3","A4","B3","C3","C4","C6","C7","C8","C9","CA","CB","CC","CD","CE","CF","D3","D6","D7","E0","E2","E3","E4","E6","E7","E8","E8","E9","EA","EB","EC","ED","EE","EF","F0",
		  "F2","F3","F4","F6","F7","F8","F9","FA","FB","FC","FD","FE","FF"]
two_byte=["01","11","21","24","25","31","34","35","40","41","42","44","45","50","51","52","54","55","60","61","62","64","65","70","71","72","74",
			"76","77","78","79","7A","7B","7B","7C","7D","7E","7F","80","81","82","86","87","88","89","8A","8B","8C","8D","8E","8F","91","92",
			"94","95","A0","A1","A2","A6","A7","A8","A9","AA","AB","AC","AD","AE","AF","B0","B1","B2","C0","C1","C2","C5","D0","D1","D2","D8","D9","DA","DB",
			"DC","DD","DE","DF","E1","E5","F1","F5"]
three_byte=["02","10","12","20","30","43","53","63","75","85","90","B3","B4","B5","B6","B7","B8","B9","BA","BC","BD","BE","BF","D5"]
byte_size={}
for i in one_byte:	byte_size[i]=1
for i in two_byte:	byte_size[i]=2
for i in three_byte: byte_size[i]=3

opcodes={"00":"NOP",	"01":"AJMP",	"02":"LJMP","03":"RR",	"04":"INC",	"05":"INC",	"06":"INC",	"07":"INC",
	"08":"INC",	"09":"INC",	"0A":"INC",	"0B":"INC",	"0C":"INC",	"0C":"INC",	"0D":"INC",	"0E":"INC",	"0F":"INC",	"10":"JBC",	"11":"ACALL",	"12":"LCALL",	"13":"DEC",
	"14":"DEC",	"15":"DEC",	"16":"DEC",	"17":"DEC",	"18":"DEC",	"19":"DEC",	"1A":"DEC",	"1B":"DEC",	"1C":"DEC",	"1D":"DEC","1E":"DEC",	"1F":"DEC",
	"20":"JB",	"21":"AJMP",	"22":"RET",	"23":"RL",	"24":"ADD",	"25":"ADD",	"26":"ADD",	"27":"ADD",	"28":"ADD",	"29":"ADD",	"2A":"ADD",	"2B":"ADD",	"2C":"ADD",	"2D":"ADD",
	"2E":"ADD",	"2F":"JNB",	"30":"JNB",	"31":"ACALL",	"32":"RETI",	"33":"RLC",	"34":"ADDC",	"35":"ADDC",	"36":"ADDC",	"37":"ADDC",	"38":"ADDC",	"39":"ADDC","3A":"ADDC",	"3B":"ADDC",	"3C":"ADDC",
	"3D":"ADDC",	"3E":"ADDC",	"3F":"ADDC",	"40":"JC",	"41":"AJMP",	"42":"ORL",	"43":"ORL",	"44":"ORL",
	"45":"ORL",	"46":"ORL",	"47":"ORL",	"48":"ORL",	"49":"ORL",	"4A":"ORL",	"4B":"ORL",	"4C":"ORL",	"4D":"ORL",
	"4E":"ORL",	"4F":"ORL",	"50":"JNC",	"51":"ACALL",	"52":"ANL","53":"ANL",	"54":"ANL",	"55":"ANL",	"56":"ANL",	"57":"ANL",	"58":"ANL",	"59":"ANL",	"5A":"ANL",	"5B":"ANL",	"5C":"ANL",	"5D":"AN;",	"5E":"ANL",	"5F":"ANL",	"60":"JZ",	"61":"AJMP",	"62":"XRL",
	"63":"XRL",	"64":"XRL",	"65":"XRL",	"66":"XRL",	"67":"XRL",	"68":"XRL",	"69":"XRL",	"6A":"XRL",	"6B":"XRL",	"6C":"XRL",
	"6D":"XRL",	"6E":"XRL",	"6F":"XRL",	"70":"JNZ",	"71":"ACALL",	"72":"ORL",	"73":"JMP",	"74":"MOV",	"75":"MOV",	"76":"MOV",	"77":"MOV",	"78":"MOV",	"79":"MOV",	"7A":"MOV",	"7B":"MOV",	"7C":"MOV",	"7D":"MOV",	"1E":"MOV",	"7F":"MOV",
	"80":"SJMP",	"81":"AJMP",	"82":"ANL",	"83":"MOVC",	"84":"DIV",	"85":"MOV",	"86":"MOV",	"87":"MOV",	"88":"MOV",	"89":"MOV",	"8A":"MOV",	"8B":"MOV",	"8C":"MOV",	"8D":"MOV",
	"8E":"MOV",	"8F":"MOV",	"90":"MOV",	"91":"ACALL",	"92":"MOV",	"93":"MOVC",	"94":"SUBB","95":"SUBB",	"96":"SUBB",
	"97":"SUBB",	"98":"SUBB","99":"SUBB","9A":"SUBB","9B":"SUBB",	"9C":"SUBB","9D":"SUBB","9E":"SUBB","9F":"SUBB",	"A0":"ORL",	"A1":"AJMP","A2":"MOV",
	"A3":"INC",	"A4":"MUL",	"A5":"RESERVED ---","A6":"MOV",	"A7":"MOV",	"A8":"MOV",	"A9":"MOV",	"AA":"MOV",	"AB":"MOV",	"AC":"MOV",	"AD":"MOV",	"AE":"MOV",	"AF":"MOV",	"B0":"ANL",
	"B1":"ACALL",	"B2":"CPL",	"B3":"CPL",	"B4":"CNJE","B5":"CNJE",	"B6":"CNJE",	"B7":"CNJE","B8":"CNJE","B9":"CNJE",	"BA":"CNJE",	"BB":"CNJE",	"BC":"CNJE",	"BD":"CNJE",	"BE":"CNJE","BF":"CJNE",	"C0":"PUSH",	"C1":"AJMP",
	"C2":"CLR",	"C3":"CLR",	"C4":"SWAP",	"C5":"XCH",	"C6":"XCH",	"C7":"XCH",	"C8":"XCH",	"C9":"XCH",	"CA":"XCH",	"CB":"XCH",	"CC":"XCH",
	"CD":"XCH",	"CE":"XCH",	"CF":"XCH",	"D0":"POP",	"D1":"ACALL",	"D2":"SETB",	"D3":"SETB",	"D4":"DA",	"D5":"DJNZ","D6":"XCHD","D7":"XCHD","D8":"DJNZ","D9":"DJNZ","DA":"DJNZ","DB":"DJNZ","DC":"DJNZ","DD":"DJNZ","DE":"DJNZ",	"DF":"DJNZ",	"E0":"MOVX",	"E1":"AJMP","E2":"MOVX","E3":"MOVX","E4":"CLR",
	"E5":"MOV",	"E6":"MOV",	"E7":"MOV",	"E8":"MOV",	"E9":"MOV",	"EA":"MOV",	"EB":"MOV",	"EC":"MOV",	"ED":"MOV",	"EE":"MOV",	"EF":"MOV",	"F0":"MOVX",	"F1":"ACALL","F2":"MOVX","F3":"MOVX","F4":"CPL","F5":"MOV","F6":"MOV","F7":"MOV","F8":"MOV","F9":"MOV","FA":"MOV","FB":"MOV","FC":"MOV",	"FD":"MOV",
	"FE":"MOV",
	"FF":"MOV"}

SFR_address={
	"ACC":"E0",	"B":"F0","PSW":"D0","SP":"81","DPL":"82","DPH":"83","P0":"80","P1":"90","P2":"A0","P3":"B0","IP":"B8",	"IE":"A8",	"TMOD":"89","TCON":"88","T2CON":"C8",	"TH0":"8C",	"TL0":"8A",	"TH1":"8D",	"TL1":"8B",	"TH2":"CD",	"TL2":"CC",	"RCAP2H":"CB",
	"RCAP2L":"CA","SCON":"98","SBUF":"99","PCON":"87"	# "DPTR":"82",
	}
SFR_name={}
for i in SFR_address:
	SFR_name[SFR_address[i]]=i
	# SFR_name[i]
bit_addressable_name={"ACC","B","PSW","P0","P1","P2","P3","IP","IE","TCON","SCON"}
bit_addressable_address=[]
for i in bit_addressable_name:
	bit_addressable_address.append(SFR_address[i])

# for having all bit address names so that can have a better looking assembly output
abit_address_name={}
for i in bit_addressable_name:
	for j in range(8):
		a_address=str((hex(int(SFR_address[i],16)+j)))[2:]
		a_name=i+"."+str(j)
		abit_address_name[a_address]=a_name # have bit readable name indexed by their actual bit location 'b7': 'P3.7'


operand={"00":["codeaddr"],
		  "01":["codeaddr"],
		  "02":["A"],
		  "03":["A"],
		  # "04":
		  # "05":
		  # "06":
		  # "07":
		  # "07":
		  # "08":
		  # "08":
		  "09":[""]

		  }

simple_replacements={
	"00":"NOP",
	"03": "RR A",
	"04": "INC A",
	"06":"INC @R0",
	"07":"INC @R1",
	"08":"INC R0",
	"09":"INC R1",
"0A":"INC R2",
"0B":"INC R3",
"0C":"INC R4",
"0D":"INC R5",
"0E":"INC R6",
"0F":"INC R7",
"16":"DEC @R0",
"17":"DEC @R1",
"26":"ADD A, @R0",
"27":"ADD A, @R1",
"36":"ADDC A,@R0",
"37":"ADDC A, @R1",

"46":"ORL A, @R0",
"47":"ORL A, @R1",
"56":"ANL A, @R0",
"57":"ANL A, @R1",

"66":"XRL A, @R0",
"67":"XRL A, @R1",

"76":" A, @R0",
"57":"ANL A, @R1",

"56":"ANL A, @R0",
"57":"ANL A, @R1",

"56":"ANL A, @R0",
"57":"ANL A, @R1",

"56":"ANL A, @R0",
"57":"ANL A, @R1",
"56":"ANL A, @R0",
"57":"ANL A, @R1",
"56":"ANL A, @R0",
"57":"ANL A, @R1",
"56":"ANL A, @R0",
"57":"ANL A, @R1",



}
# "it appears like  lower byte =8-f in opcode==> R0-R7
#  opcode 00=NOP
#  opcode *1=code address
#   opcode *2=code address 
# opcode *0=bit address, code address
# print(operand)
# print(abit_address_name)
# print(SFR_name)
# print(SFR_address)