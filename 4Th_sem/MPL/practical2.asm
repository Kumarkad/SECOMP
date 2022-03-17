;nasm 2.10.09

section .data
 str1 db 10,13,'Enter the string : ' ; 'Hello Dcoder!' plus a linefeed character
 len1: equ $-str1; Length of the 'Hello Dcoder!' string
 str2 db 10,13,"Length of string is : "
 len2 equ $ -str2

section  .bss
string resb 20
length resb 0

section .text
  global _start

_start:
  mov eax,4 ; The system call for write (sys_write)
  mov ebx,1 ; File descriptor 1 - standard output
  mov ecx,str1 ; Put the offset of hello in ecx
  mov edx,len1; helloLen is a constant, so we don't need to say
   ; mov edx,[helloLen] to get it's actual value
  int 80h ; Call the kernel
  
  mov eax,3
  mov ebx,00
  mov ecx,string
  mov edx,20h
  int 80h
  
  dec al
  mov dl,al
  
  cmp dl,09h
  jbe label
  add dl,07h
  
  label:
    add dl,30h
    mov esi,length
    mov [esi],dl
  
  mov eax,4
  mov ebx,1
  mov ecx,str2
  mov edx,len2
  int 80h
  
  mov eax,4
  mov ebx,1
  mov ecx,length
  mov edx,1
  int 80h

  mov eax,1 ; The system call for exit (sys_exit)
  mov ebx,0 ; Exit with return code of 0 (no error)
  int 80h;