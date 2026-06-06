class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # we want to find the parent of each email so each email should link to
        # the index of account
        # then we want to link accounts together
        # after that we want to build our result
        n = len(accounts)
        par = { i:i for i in range(n)}
        rank = { i:0 for i in range(n)}

        def find(n1):
            p = par[n1]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True

        email_to_acc = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    union(email_to_acc[email],i)
                else:
                    email_to_acc[email] = i
        print(email_to_acc)
        print(par)
        # {'neet@gmail.com': 0, 'neet_dsa@gmail.com': 0, 'alice@gmail.com': 1, 'bob@gmail.com': 2, 'neetcode@gmail.com': 3}
        # {0: 0, 1: 1, 2: 0, 3: 3}
        index_to_emails = defaultdict(list)
        for email, acc in email_to_acc.items():
            parent = find(acc)
            index_to_emails[parent].append(email)
        print(index_to_emails)
        
        res = []
        for acc_index, email_list in index_to_emails.items():
            temp = [accounts[acc_index][0]]
            temp += sorted(email_list)
            res.append(temp)            
        


        return res
