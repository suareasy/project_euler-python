
import math 

def getfactors( n, primefactors = True, testprime = False, countonly = False ):

	m = n
	res = [1,n]
	counter = 2
	
	for i in range( 2, math.floor( math.sqrt( n )) + 1 ):
#		print( i )
		if testprime and res != []:
			return res

		if i == m:
			break
		
		value = i
		while m > i and m % i == 0:
			
			if countonly and False:
				counter += 1
				
				if value != n//value:
					counter += 1
			else:
				
				if value in res:
					break
				res.append( value )
				
				if value != n//value:
					res.append( n//value )
				

			m = m//i
			value *= i
		m = n

#			firstpass = False


	if countonly:
#		counter += counter
		
		return len( res )
	
	else:

		if not primefactors:
			newres = []
			for i in range( len( res )):
				for j in range( i+1, len( res )):
				
					temp = res[i]*res[j]
				
					if temp != n and temp not in newres:
						newres.append( temp )
			res += newres
				
				
		return res
		#return( list( set( res )))