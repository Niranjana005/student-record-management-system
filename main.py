import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Niranjana@2005",
        database="student_db"
    )
    cursor = conn.cursor()
    print("✅ Database connected successfully!")
except mysql.connector.Error as err:
    print("❌ Something went wrong: {}".format(err))


def add_student():
    print("\n-----ADD STUDENT-----")
    REGISTER_NUMBER=int(input('ENTER REGISTER NUMBER:'))
    NAME=input("ENTER NAME:").strip()
    GENDER=input('ENTER GENDER:').strip()
    DOB=input('ENTER DATE OF BIRTH(YYYY-MM-DD):').strip()
    DEPARTMENT=input("ENTER DEPARTMENT:").strip()
    YEAR=int(input("ENTER YEAR:"))
    SECTION=input("ENTER SECTION:").strip()
    CGPA=float(input('ENTER CGPA:'))
    ADMISSION_DATE=input("ENTER ADMISSION DATE(YYYY-MM-DD):").strip()
    ADDRESS=input("ENTER ADDRESS").strip()
    CONTACT=input("ENTER CONTACT NUMBER:").strip()
    EMAIL=input("ENTER EMAIL:").strip()
    PARENT_CONTACT=input("ENTER PARENT CONTACT:").strip()
    query="""INSERT INTO STUDENTS
            (REGISTER_NUMBER,NAME,GENDER,DOB,DEPARTMENT,YEAR,SECTION,CGPA,ADMISSION_DATE,ADDRESS,CONTACT,EMAIL,PARENT_CONTACT)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values=(REGISTER_NUMBER,NAME,GENDER,DOB,DEPARTMENT,YEAR,SECTION,CGPA,ADMISSION_DATE,ADDRESS,CONTACT,EMAIL,PARENT_CONTACT)
    cursor.execute(query,values)
    conn.commit()
    print("Students added successflly!")
def search_student():
    print("\n----SEARCH STUDENT-----")
    choice=input('SEARCH BY (1) REGISTER NUMBER OR (2) NAME? ENTER 1 OR 2: ').strip()
    if choice=='1':
        reg_no=input("ENTER REGISTER NUMBER: ").strip()
        query="SELECT * FROM students WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(reg_no,))
    elif choice=="2":
        name=input("ENTER NAME: ").strip()
        query="SELECT * FROM students WHERE NAME LIKE %s"
        cursor.execute(query,('%'+name+'%',))
    else:
        print("INVALID CHOICE!")
        return
    result=cursor.fetchall()
    if result:
        for row in result:
            print("\n----STUDENT DETAILS-----")
            print(f'REGISTER NUMBER:{row[0]}')
            print(f'NAME:{row[1]}')
            print(f'GENDER:{row[2]}')
            print(f'DOB:{row[3]}')
            print(f'DEPARTMENT:{row[4]}')
            print(f'YEAR:{row[5]}')
            print(f'SECTION:{row[6]}')
            print(f'CGPA:{row[7]}')
            print(f'ADMISSION DATE:{row[8]}')
            print(f'ADDRESS:{row[9]}')
            print(f'CONTACT:{row[10]}')
            print(f'EMAIL:{row[11]}')
            print(f'PARENT CONTACT:{row[12]}')
    else:
        print("No Student found with this details")
def update_student():
    print("\n--------UPDATE STUDENT---------")
    reg_no=int(input("Enter Register Number of student to update: ").strip())
    query="select * from students where REGISTER_NUMBER=%s"
    cursor.execute(query,(reg_no,))
    result=cursor.fetchone()
    if not result:
        print("STUDENT NOT FOUND!")
        return
    print("STUDENT FOUND.WHAT DO YOU WANT TO UPDATE?")
    while True:
      print("1.NAME")
      print("2.GENDER")
      print("3.DOB")
      print("4.DEPARTMENT")
      print("5.YEAR")
      print("6.SECTION")
      print("7.CGPA")
      print("8.ADMISSION DATE")
      print("9.ADDRESS")
      print("10.CONTACT")
      print("11.EMAIL")
      print("12.PARENT CONTACT")
      print("13.EXIT")
      choice=input("ENTER YOUR CHOICE: ").strip()
      if choice=='1':
        new_name=input("ENTER NEW NAME: ").strip()
        query="update students set NAME=%s where REGISTER_NUMBER=%s "
        cursor.execute(query,(new_name,reg_no))
      elif choice=='7':
        new_cgpa=float(input("ENTER NEW CGPA:"))
        query="update students set CGPA=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_cgpa,reg_no))
      elif choice=='10':
        new_contact=input("ENTER NEW CONTACT: ").strip()
        query="update students set CONTACT=%s where REGISTER_NUMBER=%s"
        cursor.execute(query,(new_contact,reg_no))
      elif choice=='11':
        new_email=input("ENTER NEW E-MAIL:").strip()
        query="update students set EMAIL=%s where REGISTER_NUMBER=%s"
        cursor.execute(query,(new_email,reg_no))
      elif choice=='2':
        new_gender=input("ENTER NEW GENDER: ").strip()
        query="update students set GENDER=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_gender,reg_no))
      elif choice=="3":
        new_dob=input("ENTER NEW DOB (YYYY-MM-DD): ").strip()
        query="update students set DOB=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_dob,reg_no))
      elif choice=="4":
        new_department=input("ENTER NEW DEPARTMENT: ").strip()
        query="update students set DEPARTMENT=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_department,reg_no))
      elif choice=="5":
        new_year=int(input("ENTER NEW YEAR: "))
        query="update students set YEAR=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_year,reg_no))
      elif choice=="6":
        new_section=input("ENTER NEW SECTION: ").strip()
        query="update students set SECTION=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_section,reg_no))
      elif choice=="8":
        new_admission=input("ENTER NEW DATE (YYYY-MM-DD): ").strip()
        query="update students set ADMISSION_DATE=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_admission,reg_no))
      elif choice=="9":
        new_address=input("ENTER NEW ADDRESS: ").strip()
        query="update students set ADDRESS=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_address,reg_no))
      elif choice=="12":
        new_parent=input("ENTER NEW PARENT CONTACT: ").strip()
        query="update students set PARENT_CONTACT=%s WHERE REGISTER_NUMBER=%s"
        cursor.execute(query,(new_parent,reg_no))
      elif choice=="13":
        print("Returning to admin menu!!!")
        break
      else:
        print("INVALID CHOICE")
        continue
      conn.commit()
      print("STUDENT DETAILS UPDATED SUCCESSFULLY!!")

def delete_student():
   print("\n-----------DELETE STUDENT---------")
   reg_no=int(input("ENTER REGISTER NUMBER OF THE STUDENT NEED TO BE DELETED: ").strip())
   cursor.execute("select * from students where REGISTER_NUMBER=%s",(reg_no,))
   result=cursor.fetchall()
   if not result:
      print("STUDENT NOT FOUND!!")
      return
   confirm=input("ARE YOU SURE YOU WANT TO DELETE?(YES/NO):").strip().lower()
   if confirm=="yes":
      query="delete from students where REGISTER_NUMBER=%s"
      cursor.execute(query,(reg_no,))
      conn.commit()
      print("Student Deleted Successfully!!")
   else:
      print("DELETION CANCELED!!")

def view_all_students():
   print("\n---------STUDENTS LIST---------")
   query='select * from students'
   cursor.execute(query)
   result=cursor.fetchall()
   if not result:
      print("NO STUDENT RECORD FOUND!!!")
      return
   for row in result:
      print("\n---------------------------------")
      print(f'REGISTER NUMBER:{row[0]}')
      print(f'NAME:{row[1]}')
      print(f'GENDER:{row[2]}')
      print(f'DOB:{row[3]}')
      print(f'DEPARTMENT:{row[4]}')
      print(f'YEAR:{row[5]}')
      print(f'SECTION:{row[6]}')
      print(f'CGPA:{row[7]}')
      print(f'ADMISSION DATE:{row[8]}')
      print(f'ADDRESS:{row[9]}')
      print(f'CONTACT:{row[10]}')
      print(f'EMAIL:{row[11]}')
      print(f'PARENT CONTACT:{row[12]}')

def viewer_menu():
   print("-------------VIEWER MODE-----------")
   reg_no=int(input("ENTER YOUR REGISTER NUMBER:"))
   query="select * from students where REGISTER_NUMBER=%s"
   cursor.execute(query,(reg_no,))
   result=cursor.fetchall()
   if result:
      for row in result:
        print("\n---------------------------------")
        print(f'REGISTER NUMBER:{row[0]}')
        print(f'NAME:{row[1]}')
        print(f'GENDER:{row[2]}')
        print(f'DOB:{row[3]}')
        print(f'DEPARTMENT:{row[4]}')
        print(f'YEAR:{row[5]}')
        print(f'SECTION:{row[6]}')
        print(f'CGPA:{row[7]}')
        print(f'ADMISSION DATE:{row[8]}')
        print(f'ADDRESS:{row[9]}')
        print(f'CONTACT:{row[10]}')
        print(f'EMAIL:{row[11]}')
        print(f'PARENT CONTACT:{row[12]}')
   else:
      print("NO RECORD!!")
   
   
def admin_menu():
    print("\n-----ADMIN MENU------")
    print("1. ADD STUDENT")
    print("2. SEARCH STUDENT")
    print("3. UPDATE STUDENT")
    print("4. DELETE STUDENT")
    print("5. VIEW ALL STUDENTS")
    print("6. EXIT")

while True:
    user_type=input("Are you Admin or Viewer ? (admin/Viewer/exit):").lower()


    if user_type=='admin':
        username=input("Enter Username:")
        password=input("Enter password:")
        query='SELECT * FROM users WHERE USERNAME=%s AND PASSWORD=%s'
        cursor.execute(query,(username,password))
        result=cursor.fetchone()
        if result:
            print("Welcome Admin!!")
          

            while True:
                admin_menu()
                choice=input("ENTER YOUR CHOICE:").strip()
                if choice=='1':
                  add_student()
                elif choice=='2':
                  search_student()
                elif choice=='3':
                  update_student()
                elif choice=='4':
                  delete_student()
                elif choice=='5':
                  view_all_students()
                elif choice=="6":
                  print("EXCITING ADMIN MENU.....")
                  break
                else:
                   print("INVALID CHOICE")
        else:
              print("INVALID USERNAME OR PASSWORD!!")
    elif user_type=="viewer":
        viewer_menu()
    elif user_type=="exit":
        print("PROGRAM ENDED!!!")
        break
    else:
        print("INVALID OPTION SELECTION")


