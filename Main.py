postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
operators=["+","-","*","/","^"]
Opand=0
Optor=0
for token in tokens:
    if token in operators:
        Optor+=1
    else:
        Opand+=1
t=""
if Opand==(Optor+1):
    operands=[]
    for token in tokens:
        if token in operators:
            rightOp=operands.pop()
            leftOp=operands.pop()
            result=str(eval(leftOp+token+rightOp))
            if '.' in result:
                i=result.index(".")
                result=result[0:i]
            operands.append(result)
        else:
            if '.' in token:
                i=token.index(".")
                t=token[0:i]
            operands.append(t)
    print(operands.pop())
else:
    print('Invalid postfix expression')
