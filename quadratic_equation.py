def quad(a,b,c):
    d=(b*b)-(4*a*c);
    return d
e=quad(2,9,1)
if(e>=0):
    print("roots are real")
else:
    print("roots are imaginary")