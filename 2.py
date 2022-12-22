class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        res = []
        
        def helper(node, vals, minn):
		    # Если мы найдем мин сравнения 1, мы можем вернуть (с учетом свойств по британскому летнему времени + АБС дифференциал)
            # мы знаем, что это самый низкий результат, который мы можем найти.
            if minn == 1:
                return True
            if not node:
			    # Если у нас закончатся узлы, добавьте минимальное различие, которое мы нашли на этом пути
                # и возвращаем False, потому что мы не нашли 1.
                res.append(minn)
                return False
			# В противном случае мы увидим, есть ли меньшая разница между текущим узлом и тем, что мы видели до сих пор.
            if vals:
                for i in vals:
                    if abs(node.val - i) < minn:
                        minn = abs(node.val - i)
			# Рекурсируем поддеревья и возвращаем, если мы нашли 1 в любом поддереве.
            return helper(node.left, vals + [node.val], minn) or \
            helper(node.right, vals + [node.val], minn)
         
		# Мы знаем, что нашли 1, если наша функция. возвращает истину, иначе мы заберем разум того разума, который мы нашли.
        return 1 if helper(root, [], float('inf')) else min(res)