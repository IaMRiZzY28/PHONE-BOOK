import sys
def initialphonebook():
    rows,cols=int(input("ENTER NUMBER OF CONTACT U IDIOT OR GET OUT OF THE WEBSITEEEEEE")),5
    phonebook=[]
    print(phonebook)
    for i in range(rows):
        print("ENTER CONTACT AND GET SCAMMED %d"%(i+1))
        temp=[]
        for j in range(cols):
            if j ==0:
                temp.append(str(input("ENTER NAME AND GET HACKED")))
                if temp[j]=="":
                    sys.exit("NAME IS MUST AND GET OUT")
            if j==1:
                temp.append(int(input("ENTER NUMBER U DUMB ")))
            if j==2:
                temp.append(str(input("ENTER UR EMAIL ADDRESS IAM GONNA HACK U ")))
                if temp[j]=="":
                    temp[j]==None
            if j==3:
                temp.append (str(input("ENTER SOMETHING DOB")))
                if temp[j]=="":
                    temp[j]==None
            if j==4:
                temp.append(str(input("ENTER CATEGORRRRRRY")))
                if temp[j]=="":
                    temp[j]==None
        phonebook.append(temp)
        print(phonebook)
        return phonebook

