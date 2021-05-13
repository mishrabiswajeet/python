# python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        output=[]
        duplicate_score=score.copy()
        score.sort(reverse=True)
        for i in duplicate_score:
             pos=score.index(i)
             if pos+1==1:
                output.append("Gold Medal")
             elif pos+1==2:
                output.append("Silver Medal")
             elif pos+1==3:
                output.append("Bronze Medal")
             else:
                output.append(str(pos+1))
        return output
