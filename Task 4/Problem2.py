from Problem1 import students

outfile=open('busted.txt','w')

for i in range (len(students)):
    data=str(students[i].get('id'))+' '+students[i].get('data').get('name')+'-'+str(students[i].get('data').get('birthday'))
    outfile.write(data+'\n')
