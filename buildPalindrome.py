#Function to check if palindrome or not
def is_palindrome(s):
	if s == s[::-1]:
		return True
	return False

#Function to convert a string into a palindrome
def buildPalindrome(st):
    
	if st == st[::-1]:
	        return st
	s = st[::-1]
	index = 0
    	my_list = []

    	while index < len(s):
        	if is_palindrome(s[0:index]):
        		my_list.append(s[0:index])
        	index += 1
    	max_p =  max(my_list)
    	if len(max_p) > 1:
        	max_p =  max(my_list)
        	print(max_p)
        	n = len(s)-len(max_p)
        	s2 = st[:n]
        	s2 = s2[::-1]
        	return (st + s2)
    	else:
        	a =  st[:-1]
        	r = st + a[::-1]
        	return r

