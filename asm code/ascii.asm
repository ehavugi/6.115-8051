.org 00h
mov p1,#10101101b
ljmp start

.org 100h



start:
	lcall init 
	;mov R1,#0fh
	lcall printall
	loop:
		lcall getchr
		mov p1,a ; make the leds light up as value of the character received
		lcall crlf
		sjmp loop
		
	
init:
	mov tmod,#20h ; set time one for auto-reload mod 2
	mov tcon,#40h; run timer 1
	mov th1,#0fdh; 253 
	mov scon,#70h; set serial control reg for 8bit data and mode 1
	ret
	

getchr:
  jnb ri,getchr
  mov a,sbuf
  anl a,#7fh;
  clr ri
  
  ret
  
sndchr:
	clr scon.1 ; clear ti complete flag
	mov sbuf,a ; move a character from acc to the sbuf
txloop:
	jnb scon.1,txloop; wait until chr is sent
	ret
	
crlf:
	
	djnz R1,sndchr
	;mov sbuf,#0ch; send a new line character
    ;mov sbuf,#0dh; go back to beginning of line
	lcall sndchr;
	mov a,#0dh
	lcall sndchr
	mov a, #0ah;
	lcall sndchr 
	mov R1,#03fh
	ret
	
printall:
	mov R2,#00h;
	print:
	   INC R2
	   mov a,R2
	   DEC a
	  ; mov R1,#0fh; make the print line length equal to 16
	   lcall crlf
	   ;djnz R2,print
	   cjne R2, #80h,print;
	   ret 
	   