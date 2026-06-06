class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 1.) map each email to an account number
        # 2.) while mapping if we find that an email is already mapped then 
        # we want to union the two accounts together with our Union find
        # 3.) for every connected component take the account and then make 
        # a list of all the emails belonging to that account
        # 4.) sort the account -> emails and then append it to the res
        
        # implementing a union find where the nodes are the indicies of the 
        # account
        par = {}
        rank = {}
        N = len(accounts)
        for i in range(N):
            par[i] = i
            rank[i] = 0
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
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

        email_to_acc = {} # maps emails to account indexes

        for i, account in enumerate(accounts):
            for email in account[1:]: # excluding the first value
                if email in email_to_acc: # union the accounts tgt
                    union(email_to_acc[email], i)
                else:
                    email_to_acc[email] = i
        
        print(email_to_acc)

        email_groups = defaultdict(list) # acc index to list of emails

        for email,acc_index in email_to_acc.items():
            # get the parent of the current group and just add all the stuff
            parent = find(acc_index)
            email_groups[parent].append(email)
        print(email_groups)
        
        res = []
        for acc_index, email_list in email_groups.items():
            temp = [accounts[acc_index][0]]
            sorted_emails = sorted(email_list)
            for email in sorted_emails:
                temp.append(email)
            res.append(temp)
        
        return res
