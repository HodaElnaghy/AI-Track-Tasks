
myfile=open("dummy_grades.txt","r")
students=[] 
for line in myfile:
    
    str=line.split()

    if (str[2]=="N/A"):  
        break
    
    students.append({'id':int(str[0]),
                     'data':{
                                'name':str[1],
                                'score':int(str[2]),
                                'birthday':int(str[4]),
                                'sex':str[6]
                                                }})
myfile.close
    
def smallest (students):
    ages=[]
    for i in range(len(students)):
        ages.append(students[i].get('data').get('birthday'))
    l=ages.index(min(ages))
    return(students[l].get('id'))


def avg_score(students):
    scores=[]
    for i in range(len(students)):
        scores.append(students[i].get('data').get('score'))
    avg=sum(scores)/len(scores)

    return(avg)

def sex(students):
    scores=[]
    for i in range(len(students)):
        scores.append(students[i].get('data').get('score'))
    l=scores.index(max(scores))
    return(students[i].get('data').get('sex'))

def main():

    print ("avg_score:",avg_score(students))
    print ("oldest:",smallest(students))
    print ("bestscore:",sex(students))

if __name__ =='__main__':
    main()
