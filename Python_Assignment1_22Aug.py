class Assignment:

    def find_subsets(self,arr):
        ans=[]
        for bi in range(0,int("1"*len(arr),2)):
            bi=(len(arr)-len(bin(bi)[2:]))*"0"+bin(bi)[2:]
            temp=[]
            for j in range(0,len(arr)):
                if int(bi[j]):
                    temp.append(arr[j])
            ans.append(temp)
        return ans
    
   
    def number_to_roman(self,num):
        table={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        tab2=[1,5,10,50,100,500,1000]
        ans=""
        ind=6
        while num>0:
            print(num)
            if num-tab2[ind]<0:
                ind-=1
            else:
                num-=tab2[ind]
                ans+=table[tab2[ind]]
        return ans



class Student:
    def __init__(self,student_name,student_id):
        self.student_name=student_name
        self.student_id=student_id
    
    def display_attr(self):
        print(self.__dict__)
        
    
    def add_attr(self,attr_name,attr_value):
        setattr(self,attr_name,attr_value)
        
    def del_attr(self,attr_name):
        delattr(self,attr_name)

st1=Student("ram",1001)
st1.display_attr()

print("added student_class")
st1.add_attr("student_class",4)

st1.display_attr()

print("removed student_name")
st1.del_attr("student_name")




