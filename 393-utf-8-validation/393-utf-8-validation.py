class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        
        for d in data:           
            bin_d = bin(d)[2:]
            
            if len(bin_d) != 8:
                bin_d = bin_d.zfill(8)
                
            print(bin_d)
            
            if count == 0:
                if bin_d[0] == '1' and bin_d[1] == '1':
                    count = 1
                
                    for i in range(2, 5):
                        if bin_d[i] == '1':
                            count = count + 1
                        else:
                            break
                    if bin_d[i] != '0':
                        return False   
                elif bin_d[0] == '1' and bin_d[1] == '0':
                    return False     
            else:
                if bin_d[0] != '1' or bin_d[1] != '0':
                    return False          
                count = count - 1
        
        if count == 0:
            return True
        else:
            return False