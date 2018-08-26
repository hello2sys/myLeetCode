class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic={}
        for pay in bills:
            if pay==5:
                dic[5]=dic.get(5,0)+1
            if pay==10:
                if dic.get(5,0)<1:
                    return False
                else:
                    dic[5]-=1
                    dic[10]=dic.get(10,0)+1
            if pay==20:
                if dic.get(10,0)==0:
                    if dic.get(5,0)<3:
                        return False
                    else:
                        dic[5]-=3
                else:
                    dic[10]-=1
                    if dic.get(5,0)<1:
                        return False
                    else:
                        dic[5]-=1
        return True