#Function that returns an array of the averages of all 3*3 arrays

def boxBlur(image):
	height = len(image)
    	width = len(image[0])

	#List Comprehension to create an array of zeroes.
	result = [[0 for i in range(width-2)] for j in range(height-2)]
    	for i in range(1,height-1):
        	for j in range(1,width-1):
			print(i,j, image[i][j])
			
			#Replacing the zeroes with the averages of the 3*3 matrix
	        	result[i-1][j-1] = int((image[i-1][j-1] + image[i-1][j] + image[i-1][j+1] + image[i][j-1] + image[i][j] + image[i][j+1] + image[i+1][j-1] + image[i+1][j] + image[i+1][j+1])/9) 

    	return(result)
