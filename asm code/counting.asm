;============================================
;=     counting in binary
;=   starts at zero and increases and the overflows to start again
;============================================

clr A
mov P1, A

; select 7-segment display number 2
;========
clr p3.3 
setb P3.4
;=======
loop: 	
	INC A
	lcall delay
	mov p1,A
	;lcall delay
	sjmp loop
       

delay:
	mov R0,#0ffh ; 
	mov R1,#0ffh ; 
	mov R2,#008h ; number of 256*256 loops? * time to execute each loop ~= time of the delay; currently estimated to be 1second
	loop1:
		djnz R1,loop1
	mov R1, #0ffh
	djnz R0,loop1
	djnz R2,loop1
	ret
	


