import csv
def write_into_csv():
    with open('student_info.csv','a',newline='') as csv_files:
        writer = csv.writer(csv_file)
        if csv_file_tell()==0:
            
             writer = csv.writer("firstname","lastname","age","contact_number","e-mail") 
if __name__ == "__main__" :
         
    condition =True
    
    while(condition):
        student_info=input("enter student information in the following format(firstname lastname age contact_number e-mail):")
        print("entered information:"+student_info)
        student_info_list=student_info.split(' ')
        print("entered split up info:"+str(student_info_list))
        print("\nthe entered information is-\nfirstage : {} \nlastname : {} \nage : {} \ncontact_number : {} \ne-mail : {} ".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        choice_check =input("is the value correct(yes/no):")
        if choice_check =="yes":
            
            write_into_csv(student_info_list)
            condition_check=input("enter(yes/no)yes for next entry:")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False
        elif choice_check =="no":
            print("\nplease re-enter the values!")
