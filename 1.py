# Компания планирует провести собеседование с 2n людьми. 
#Учитывая массив затрат, где затраты[i] = [acosti, bcosti], стоимость перелета i-го человека в город a равна Acosti,
#  а стоимость перелета i-го человека в город b равна Bcosti.
# Верните минимальную стоимость перелета каждого человека в город таким образом, чтобы в каждый город прибыло ровно n человек.

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = n // 2
        
        def dfs(cur, a):
			# cur - это текущий пользовательский индекс
            # a - это количество людей, путешествующих в город a            
			
            if cur == n:
                return 0
            
			# люди в городе b
            b = cur - a
            ans = float('inf')
            
			# количество людей в городском номере а не достигло предела,
            # затем текущий пользователь может отправиться в город а
			
            if a < m:
                ans = min(dfs(cur+1, a+1)+costs[cur][0], ans)
            
			# количество людей в городском номере b не достигло предела
            # затем текущий пользователь может отправиться в город b    
            if b < m:
                ans = min(dfs(cur+1, a)+costs[cur][1], ans)
            return ans
    
        return dfs(0, 0)