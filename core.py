from jobberman import jobs

jobs_list=[]
for i,j in jobs():
    jobs_list.append(i)
    print(i,j)
    
#print(jobs_list)