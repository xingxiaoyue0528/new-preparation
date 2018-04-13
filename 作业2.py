accounts=[];
n=int(raw_input('输入账户个数：'));
i=0;
for i in range(n):
    print '输入第',i+1,'个账户所包含的元素个数：'
    m=int(raw_input());
    print '依次输入该账户的姓名和地址：'
    for j in range(m):
        account=[];
        account.append(raw_input());
    accounts.extend(account);
for a in range(n):
    for b in range(n):
        if b>a:
            for c in range(1,len(accounts[a])):
                for d in range(1,len(accounts[b])):
                    if accounts[a][c]==accounts[b][d]:
                        accounts[a].append(ccounts[b][d]);
    print accounts[a];
 
            
        
