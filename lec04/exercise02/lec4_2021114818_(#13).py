opnd1=int(input('피연산자 1: '))
opnd2=int(input('피연산자 2: '))
print(opnd1,'*',opnd2)
print('=','(',opnd1//100,'+',opnd1//10%10,'+',opnd1%10,')','*',opnd2)
print('=',opnd1//100,'*',opnd2,'+',opnd1//10%10,'*',opnd2,'+',opnd1%10,'*',opnd2)
print('=',(opnd1//100)*opnd2,'+',(opnd1//10%10)*opnd2,'+',opnd1%10*opnd2)
print('=',(opnd1//100)*opnd2*100+(opnd1//10%10)*opnd2*10+opnd1%10*opnd2)
