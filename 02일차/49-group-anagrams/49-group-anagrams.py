class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word) # 데이터를 정렬해서 리스트로 반환하는 sorted(정렬할 데이터) 함수
            
        return anagrams.values() # dictionary의 값들을 리스트 형태로 내보내는 dictionary.values() 함수
        
        
                
        
                