####################################################################
#  Given an m x n integer grid accounts where accounts[i][j]
#  is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
#  Returns the wealth that the richest customer has.
#  Note: A customer's wealth is the amount of money they have in all 
#  their bank accounts. The richest customer is the customer that has 
#  the maximum wealth.
#  LeetCode #1672
####################################################################

### Solution 1 (Good) ###
# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         accTotals = [0] * len(accounts)
#         for customer in range(len(accounts)):
#             for bank in range(len(accounts[customer])):
#                 accTotals[customer] += accounts[customer][bank]

#         return max(accTotals)


### Solution 2 (Better) ###
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(customer) for customer in accounts)

accounts = [[7,1,3],[2,8,7],[1,9,5]]
sol = Solution()
print(sol.maximumWealth(accounts))