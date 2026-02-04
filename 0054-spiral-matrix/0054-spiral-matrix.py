class Solution: 
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        m,n=len(matrix),len(matrix[0]) 
        left,top=0,0 
        right,down=n-1,m-1 
        a=[] 
        while top<=down and left<=right: 
            for i in range(left,right+1): 
                a.append(matrix[top][i]) 
            top+=1 
            for j in range(top,down+1): 
                a.append(matrix[j][right]) 
            right-=1 
            if top<=down: 
                for k in range(right,left-1,-1): 
                    a.append(matrix[down][k]) 
                down-=1 
            if left<=right :
                for l in range(down,top-1,-1): 
                    a.append(matrix[l][left]) 
                left+=1
        return a