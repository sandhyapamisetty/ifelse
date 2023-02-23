a=int(input(" entet the age "))
b=int(input("enter the age"))
c=int(input(" enter the age"))
if (a>b and a>c):
         if (b<a and b<c):
               print(" a is oldest",a)
               print(" b is youngest",b)
         else:
             	print (" b  youngest")
             	prinr(" c youngest")
             	print(" a youngest")
elif (b>a and b>c):
	    if ( c<a and c<b):
	             print(" b is oldest",b)
	             print(" c is youngest",c)
	    else:
	       	  print(" a  youngest")
	       	  print(" c youngest")
	       	  print(" b youngest")
elif  (c>a and c>b):
	    if (a<b and a<c):
	             print(" c is oldest",c)
	             print(" a is youngest",a)
	    else:
	    	     print(" c youngest")
	    	     print(" b youngest")
	    	     print(" a youngest")
else:
	print(" nothing")