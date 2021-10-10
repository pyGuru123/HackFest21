class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        
         
        m,n = len(matrix),len(matrix[0])
        num_idx = defaultdict(set)
        for i in range(m):  
            for j in range(n):
                num_idx[matrix[i][j]].add((i,j))
        #print(num_idx)
        d_row = defaultdict(list) #[num,rank]
        d_column = defaultdict(list)
        ans = [[1]*n for _ in range(m)]
                
        def update(idx,num):
            i,j = idx
            tmp_row = 1
            if(i not in d_row):pass
            elif(d_row[i][0]==num):tmp_row=d_row[i][1]
            else:tmp_row=d_row[i][1]+1
            tmp_column = 1
            if(j not in d_column):pass
            elif(d_column[j][0]==num):tmp_column=d_column[j][1]
            else:tmp_column=d_column[j][1]+1
            ans[i][j] = max(tmp_row,tmp_column)
            d_row[i] = [num,ans[i][j]]
            d_column[j] = [num,ans[i][j]]

        def bfs(new_row,new_column,qs,num):
            seem = set()
            seem_row =  set()
            seem_column =  set()
            
            while(qs):
                rank,idx = heappop(qs)
                if(idx in seem):continue
                i,j = idx
                rank *=-1
                Qs = set([idx])
                while(Qs):
                    next_Qs = set()
                    for Q in Qs:
                        if(Q in seem):continue
                        I,J=Q
                        d_row[I][1] = rank
                        d_column[J][1] = rank
                        ans[I][J]=rank       
                        seem.add(Q)
                        if(I not in seem_row):
                            for j in new_row[I]:
                                if((I,j) in seem or (I,j) in Qs):continue
                                next_Qs.add((I,j))
                            seem_row.add(I)
                            
                        if(J not in seem_column):
                            for i in new_column[J]:
                                if((i,J) in seem  or (i,J) in Qs):continue
                                next_Qs.add((i,J))
                            seem_column.add(J)
                    Qs = next_Qs
                        
                
        
        for num in list(sorted(num_idx.keys())):
            
            qs = []
            new_row = defaultdict(set)
            new_column = defaultdict(set)
            
            for idx in num_idx[num]:
                i,j = idx
                new_row[i].add(j)
                new_column[j].add(i)
                update(idx,num)
                heappush(qs,(-ans[i][j],idx))
            bfs(new_row,new_column,qs,num)        
                
        return ans        
