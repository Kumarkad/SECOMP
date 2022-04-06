section .data
	msg1 :db 10,13,"Array elements are : "
	msg1_len : equ $ -msg1
	
	msg2 : db 10,13,"Largest Number is : "
	msg2_len : equ $ -msg2
	
	newline db 10,13
	
	array dw 1234h,6784h,7435h,8764h,7863h
	
	array_count db 5
	
section .bss
	disp_num resb 4
	large resw 1
	
%macro print 2
 mov eax,4
 mov ebx,1
 mov ecx,%1
 mov edx,%2
 int 80h
%endmacro

section .text
	global _start:
	_start:
		
		print msg1,msg1_len
		
		mov ecx,[array_count]
		mov esi,array
		
	up :    mov bx,[esi]
		push ecx
		call disp
		
		print newline,1
		
		pop ecx
		add esi,2
		dec ecx
		jnz up
		
		
		
		mov esi,array
		mov ecx,05
		dec ecx
		up1:add esi,2
		cmp ax,[esi]
		ja skip
		xchg ax,[esi]
		
	skip: dec ecx
		jnz up1
		mov word[large],ax
		print msg2,msg2_len
		mov bx,word[large]
		call disp
		
		mov eax,1
		mov ebx,0
		int 80h

disp:
	mov edi,disp_num
	mov ecx,4
	
	l2: rol bx,4
	mov dl,bl
	and dl,0fh
	cmp dl,09
	jbe l1
	add dl,07
	
	l1: add dl,30h
	mov [edi],dl
	inc edi
	dec ecx
	jnz l2
	print disp_num,4
	ret
