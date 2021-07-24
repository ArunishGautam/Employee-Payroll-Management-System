from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System Developed by Arunish Gautam")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employee's",command=self.employee_frame,font=("times new roman",12,"bold"),bg="orange",fg="white").place(x=1100,y=10,width=120,height=30)
        #====================Frame 1===========================
        #===========Variables=============
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()
        self.var_txt_address=StringVar()
        Frame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=870,height=720)
        title1=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman",20),bg="white",fg="black").place(x=10,y=40)
        self.txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow",fg="black")
        self.txt_code.place(x=200,y=50,width=300)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="grey").place(x=620,y=50,width=200,height=30)
        #===Row1===
        lbl_degi=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black").place(x=10,y=100)
        txt_degi=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black").place(x=180,y=110,width=200)
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black").place(x=470,y=110)
        txt_doj=Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=600,y=120,width=200)
        #===Row2===
        lbl_name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black").place(x=10,y=190)
        txt_degi=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=180,y=200,width=200)
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black").place(x=470,y=190)
        txt_dob=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=600,y=200)
        #===Row3===
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black").place(x=10,y=280)
        txt_age=Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=180,y=290,width=200)
        lbl_exp=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black").place(x=470,y=280)
        txt_exp=Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=600,y=290,width=200)
        #===Row4===
        lbl_gen=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black").place(x=10,y=370)
        txt_gen=Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=180,y=380,width=200)
        lbl_proof=Label(Frame1,text="Proof Id",font=("times new roman",20),bg="white",fg="black").place(x=470,y=370)
        txt_proof=Entry(Frame1,font=("times new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=600,y=380,width=200)
        #===Row5===
        lbl_email=Label(Frame1,text="Email",font=("times new roman",20),bg="white",fg="black").place(x=10,y=460)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=180,y=470,width=200)
        lbl_contactno=Label(Frame1,text="Contact No",font=("times new roman",20),bg="white",fg="black").place(x=470,y=460)
        txt_contactno=Entry(Frame1,font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=600,y=470)
        #===Row6===
        lbl_hired=Label(Frame1,text="Hired Location",font=("times new roman",18),bg="white",fg="black").place(x=10,y=550)
        txt_hired=Entry(Frame1,font=("times new roman",15),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=180,y=560,width=200)
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black").place(x=470,y=550)
        txt_status=Entry(Frame1,font=("times new roman",15),textvariable=self.var_status,bg="lightyellow",fg="black").place(x=600,y=560,width=200)
        #===Row7===
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18),bg="white",fg="black").place(x=10,y=640)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=180,y=600,width=600,height=100)


        
        
        
        
        
        #====================Frame 2===========================
         #===========Variables=============
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salery=StringVar()
        self.var_t_day=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=890,y=70,width=640,height=360)
        title2=Label(Frame2,text="Employee Sallery Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        #===Row1===
        lbl_mnth=Label(Frame2,text="Month:",font=("times new roman",15),bg="white",fg="black").place(x=10,y=50)
        txt_mnth=Entry(Frame2,font=("times new roman",20),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=80,y=50,width=100)
        lbl_yr=Label(Frame2,text="Year:",font=("times new roman",15),bg="white",fg="black").place(x=190,y=50)
        txt_yr=Entry(Frame2,font=("times new roman",20),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=250,y=50,width=100)
        lbl_slry=Label(Frame2,text="Basic Sallery:",font=("times new roman",15),bg="white",fg="black").place(x=380,y=50)
        txt_slry=Entry(Frame2,font=("times new roman",20),textvariable=self.var_salery,bg="lightyellow",fg="black").place(x=520,y=50,width=100)
        #===Row2===
        lbl_tdays=Label(Frame2,text="Total Days:",font=("times new roman",15),bg="white",fg="black").place(x=10,y=100)
        txt_tdays=Entry(Frame2,font=("times new roman",20),textvariable=self.var_t_day,bg="lightyellow",fg="black").place(x=110,y=100,width=100)
        lbl_absent=Label(Frame2,text="Absents:",font=("times new roman",15),bg="white",fg="black").place(x=220,y=100)
        txt_absent=Entry(Frame2,font=("times new roman",20),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=300,y=100,width=100)
        #===Row3===
        lbl_medi=Label(Frame2,text="Medical:",font=("times new roman",15),bg="white",fg="black").place(x=10,y=180)
        txt_medi=Entry(Frame2,font=("times new roman",20),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=100,y=180,width=100)
        lbl_pfund=Label(Frame2,text="Provident Fund:",font=("times new roman",15),bg="white",fg="black").place(x=220,y=180)
        txt_pfund=Entry(Frame2,font=("times new roman",20),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=360,y=180,width=100)
        #===Row4===
        lbl_Convse=Label(Frame2,text="Convence:",font=("times new roman",15),bg="white",fg="black").place(x=10,y=250)
        txt_convse=Entry(Frame2,font=("times new roman",20),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=100,y=250,width=100)
        lbl_nsalry=Label(Frame2,text="Net Sallery:",font=("times new roman",15),bg="white",fg="black").place(x=220,y=250)
        txt_nslry=Entry(Frame2,font=("times new roman",20),textvariable=self.var_net_salary,bg="lightyellow",fg="black").place(x=340,y=250,width=200)
        #===ButtonRow===
        btn_cal=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",20),bg="Yellow").place(x=20,y=290,width=120,height=30)
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",20),bg="green")
        self.btn_save.place(x=150,y=290,width=100,height=30)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",20),bg="grey").place(x=270,y=290,width=100,height=30)
        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",20),bg="Yellow")
        self.btn_update.place(x=400,y=290,width=120,height=30)
        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",20),bg="red")
        self.btn_delete.place(x=530,y=290,width=100,height=30)
        
        #====================Frame 3===========================
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=890,y=430,width=640,height=360)
        #========Calculator Frame==================
        self.var_txt=StringVar()
        self.var_operator=""
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=""
        def clear_cal():
          self.var_txt.set("")
          self.var_operator=""





        cal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        cal_frame.place(x=2,y=2,width=247,height=345)
        title3=Label(cal_frame,text="Calculator",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        txt_result=Entry(cal_frame,bg="lightyellow",textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=40,relwidth=1,height=50)
        #======Row1============
        btn_7=Button(cal_frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=92,width=60,height=60)
        btn_8=Button(cal_frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=92,width=60,height=60)
        btn_9=Button(cal_frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=92,width=60,height=60)
        btn_div=Button(cal_frame,text="/",command=lambda:btn_click("/"),font=("times new roman",15,"bold")).place(x=183,y=92,width=60,height=60)
          #======Row2============
        btn_4=Button(cal_frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=152,width=60,height=60)
        btn_5=Button(cal_frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=152,width=60,height=60)
        btn_6=Button(cal_frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=152,width=60,height=60)
        btn_mul=Button(cal_frame,text="*",command=lambda:btn_click("*"),font=("times new roman",15,"bold")).place(x=183,y=152,width=60,height=60)
          #======Row3============
        btn_1=Button(cal_frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=212,width=60,height=60)
        btn_2=Button(cal_frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=212,width=60,height=60)
        btn_3=Button(cal_frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=212,width=60,height=60)
        btn_min=Button(cal_frame,text="-",command=lambda:btn_click("-"),font=("times new roman",15,"bold")).place(x=183,y=212,width=60,height=60)
         #======Row4============
        btn_zero=Button(cal_frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=272,width=60,height=60)
        btn_dot=Button(cal_frame,text="C",command=clear_cal,font=("times new roman",15,"bold")).place(x=61,y=272,width=60,height=60)
        btn_plus=Button(cal_frame,text="+",command=lambda:btn_click("+"),font=("times new roman",15,"bold")).place(x=122,y=272,width=60,height=60)
        btn_equal=Button(cal_frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=183,y=272,width=60,height=60)
        #=========Sallery Frame=========
        sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=250,y=2,width=380,height=345)
        title4=Label(Frame3,text="Sallery Recipt",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=250,y=0,relwidth=1)
        sal_frame2=Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=270)
        self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  1024
SalaryOf\t\t:  MM-YYYY
Generated On\t\t:  DD-MM-YYYY
-------------------------------------------------
Total Days\t\t: DD
Total Present\t\t: DD
Total Absent\t\t: DD
Convence\t\t: Rs.------
Medical\t\t: Rs.-------
PF\t\t: Rs.------
Gross Payment\t\t: Rs.--------
Net Salary\t\t: Rs.---------
--------------------------------------------------
This is Computer Generated Slip, not
required any Signature
'''
        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        self.txt_salery_recipt=Text(sal_frame2,font=("times new roman",15),bg="lightyellow",yscrollcommand=scroll_y.set,fg="black")
        self.txt_salery_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salery_recipt.yview)
        self.txt_salery_recipt.insert(END,self.sample)
        btn_print=Button(sal_frame,text="Print",font=("times new roman",20),bg="Yellow").place(x=180,y=310,width=120,height=30)
        self.check_connection()
  #============================================ All Functions Start here =================================
    def search(self):
      try:
        con=pymysql.connect(host='localhost',user='root',password='',db='emss')
        cur=con.cursor()
        cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
        row=cur.fetchone()
          #print(rows)
          #print("conncection")
        if row==None:
          messagebox.showerror("Error","Invalid Employee Id try another Employee Id",parent=self.root)
        else:
          self.var_emp_code.set(row[0])
          self.var_designation.set(row[1])
          self.var_name.set(row[2])     
          self.var_age.set(row[3])   
          self.var_gender.set(row[4])
          self.var_email.set(row[5])
          self.var_hr_location.set(row[6])
          self.var_doj.set(row[7])
          self.var_dob.set(row[8])
          self.var_experience.set(row[9])
          self.var_proof_id.set(row[10])
          self.var_contact.set(row[11])
          self.var_status.set(row[12])
          self.txt_address.delete("1.0",END)
          self.txt_address.insert(END,row[13])
          self.var_month.set(row[14])
          self.var_year.set(row[15])
          self.var_salery.set(row[16])
          self.var_t_day.set(row[17])
          self.var_absent.set(row[18])
          self.var_medical.set(row[19])
          self.var_pf.set(row[20])
          self.var_convence.set(row[21])
          self.var_net_salary.set(row[22])   
          file_=open('Salary_reciept/'+str(row[23]),'r')
          self.txt_salery_recipt.delete('1.0',END)
          for i in file_:
            self.txt_salery_recipt.insert(END,i)
          file_.close()     
          self.btn_save.config(state=DISABLED)
          self.btn_update.config(state=NORMAL)
          self.btn_delete.config(state=NORMAL)
          self.txt_code.config(state='readonly')
      except Exception as ex:
        messagebox.showerror("Error",f'Error due to: {str(ex)}')
    def clear(self):
      self.btn_save.config(state=NORMAL)
      self.btn_update.config(state=DISABLED)
      self.btn_delete.config(state=DISABLED)
      self.txt_code.config(state=NORMAL)
      self.var_emp_code.set('')
      self.var_designation.set('')
      self.var_name.set('')     
      self.var_age.set('')   
      self.var_gender.set('')
      self.var_email.set('')
      self.var_hr_location.set('')
      self.var_doj.set('')
      self.var_dob.set('')
      self.var_experience.set('')
      self.var_proof_id.set('')
      self.var_contact.set('')
      self.var_status.set('')
      self.txt_address.delete("1.0",END)
      self.var_month.set('')
      self.var_year.set('')
      self.var_salery.set('')
      self.var_t_day.set('')
      self.var_absent.set('')
      self.var_medical.set('')
      self.var_pf.set('')
      self.var_convence.set('')
      self.var_net_salary.set('')   
      self.txt_salery_recipt.delete('1.0',END)
      self.txt_salery_recipt.insert(END,self.sample)
      
    def delete(self):
      if self.var_emp_code.get()=="":
        messagebox.showerror("Error","Invalid Employee Id")
      else:
        try:
          con=pymysql.connect(host='localhost',user='root',password='',db='emss')
          cur=con.cursor()
          cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
          row=cur.fetchone()
          #print(rows)
          #print("conncection")
          if row==None:
            messagebox.showerror("Error","Invalid Employee Id try another Employee Id",parent=self.root)
          else:
            op=messagebox.askyesno("Confirm","Are you really want to delete")
            if op>=1:
              cur.execute("delete from emp_salary where e_id=%s",(self.var_emp_code.get()))
              con.commit()
              con.close()
              messagebox.showinfo("Success","Employee record deleted Successfully",parent=self.root)
              self.clear()
        except Exception as ex:
           messagebox.showerror("Error",f'Error due to: {str(ex)}')
      
   
    def add(self):
      if self.var_emp_code.get()=="" or self.var_designation.get()=="" or self.var_name.get()=="":
        messagebox.showerror("Error","Employee Details are Required")
      else:
        try:
          con=pymysql.connect(host='localhost',user='root',password='',db='emss')
          cur=con.cursor()
          cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
          row=cur.fetchone()
          #print(rows)
          #print("conncection")
          if row!=None:
            messagebox.showerror("Error","This Employee Id available in record,try again with another Id",parent=self.root)
          else:
            cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
              self.var_emp_code.get(),
              self.var_designation.get(),
              self.var_name.get(),
              self.var_age.get(),
              self.var_gender.get(),
              self.var_email.get(),
              self.var_hr_location.get(),
              self.var_doj.get(),
              self.var_dob.get(),
              self.var_experience.get(),
              self.var_proof_id.get(),
              self.var_contact.get(),
              self.var_status.get(),
              self.txt_address.get("1.0",END),
              self.var_month.get(),
              self.var_year.get(),
              self.var_salery.get(),
              self.var_t_day.get(),
              self.var_absent.get(),
              self.var_medical.get(),
              self.var_pf.get(),
              self.var_convence.get(),
              self.var_net_salary.get(),    
              self.var_emp_code.get()+".txt"                                                                                            
            )
            )
            con.commit()
            con.close()
            file_=open('Salary_reciept/'+str(self.var_emp_code.get())+".txt",W)
            file_.write(self.txt_salery_recipt.get("1.0",END))
            file_.close()
            messagebox.showinfo("Success","Record added Succesfully ")
            self.clear()
        except Exception as ex:
           messagebox.showerror("Error",f'Error due to: {str(ex)}')
    def update(self):
      if self.var_emp_code.get()=="" or self.var_designation.get()=="" or self.var_name.get()=="":
        messagebox.showerror("Error","Employee Details are Required")
      else:
        try:
          con=pymysql.connect(host='localhost',user='root',password='',db='ems')
          cur=con.cursor()
          cur.execute("select * from emp_salary where e_id=%s",(self.var_emp_code.get()))
          row=cur.fetchone()
          #print(rows)
          #print("conncection")
          if row==None:
            messagebox.showerror("Error","This Employee Id is Invalid,try again with valid Employee Id",parent=self.root)
          else:
            cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
            (
              self.var_designation.get(),
              self.var_name.get(),
              self.var_age.get(),
              self.var_gender.get(),
              self.var_email.get(),
              self.var_hr_location.get(),
              self.var_doj.get(),
              self.var_dob.get(),
              self.var_experience.get(),
              self.var_proof_id.get(),
              self.var_contact.get(),
              self.var_status.get(),
              self.txt_address.get("1.0",END),
              self.var_month.get(),
              self.var_year.get(),
              self.var_salery.get(),
              self.var_t_day.get(),
              self.var_absent.get(),
              self.var_medical.get(),
              self.var_pf.get(),
              self.var_convence.get(),
              self.var_net_salary.get(),    
              self.var_emp_code.get()+".txt"  ,
              self.var_emp_code.get()                                                                                         
            )
            )
            con.commit()
            con.close()
            file_=open('Salary_reciept/'+str(self.var_emp_code.get())+".txt",W)
            file_.write(self.txt_salery_recipt.get("1.0",END))
            file_.close()
            messagebox.showinfo("Success","Record Updated Succesfully ")
        except Exception as ex:
           messagebox.showerror("Error",f'Error due to: {str(ex)}')
    def calculate(self):
      if self.var_designation.get()=="" or self.var_name.get()=="" or self.var_age.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_hr_location.get()=="" or self.var_doj.get()=="" or self.var_dob.get()=="" or self.var_experience.get()=="":
        messagebox.showerror("Error","All Fields are Required")
      else:
        per_day=int(self.var_salery.get())/int(self.var_t_day.get())
        work_day=int(self.var_t_day.get())-int(self.var_absent.get())
        sal_=per_day*work_day
        deduct=int(self.var_medical.get())+int(self.var_pf.get())
        addition=int(self.var_convence.get())
        net_sal=sal_-deduct+addition
        self.var_net_salary.set(str(round(net_sal,2)))
        #=========Update the Recipt============
        new_sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t: {self.var_emp_code.get()}
SalaryOf\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
-------------------------------------------------
Total Days\t\t: {self.var_t_day.get()}
Total Present\t\t: {str(int(self.var_t_day.get())-int(self.var_absent.get()))}
Total Absent\t\t: {self.var_absent.get()}
Convence\t\t: Rs.{self.var_convence.get()}
Medical\t\t: Rs.{self.var_medical.get()}
PF\t\t: Rs.{self.var_pf.get()}
Gross Payment\t\t: Rs.{self.var_salery.get()}
Net Salary\t\t: Rs.{self.var_net_salary.get()}
--------------------------------------------------
This is Computer Generated Slip, not
required any Signature
'''
        self.txt_salery_recipt.delete("1.0",END)
        self.txt_salery_recipt.insert(END,new_sample)

    def check_connection(self):
      try:
        con=pymysql.connect(host='localhost',user='root',password='',db='emss')
        cur=con.cursor()
        cur.execute("select * from emp_salary")
        rows=cur.fetchall()
        print(rows)
        print("conncection")
      except Exception as ex:
        messagebox.showerror("Error",f'Error due to: {str(ex)}')
    def employee_frame(self):
      self.root2=Toplevel(self.root)      
      self.root2.title("Employee Payroll Management System Developed by Arunish Gautam")
      self.root2.geometry("1280x700+100+60")
      self.root2.config(bg="white")
      #title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
      self.root2.focus_force()
      self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'))
      self.employee_tree.heading('e_id',text='EID')
      self.employee_tree.heading('designation',text='Designation')
      self.employee_tree.heading('name',text='Name')
      self.employee_tree.heading('age',text='Age')
      self.employee_tree.heading('gender',text='Gender')
      self.employee_tree.heading('email',text='Email')
      self.employee_tree.heading('hr_location',text='HR LOC')
      self.employee_tree.heading('doj',text='DOJ')
      self.employee_tree.heading('dob',text='DOB')
      self.employee_tree.heading('experience',text='Experience')
      self.employee_tree.heading('proof_id',text='Proof')
      self.employee_tree.heading('contact',text='Contact')
      self.employee_tree.heading('status',text='Status')
      self.employee_tree.heading('address',text='Address')
      self.employee_tree.heading('month',text='Month')
      self.employee_tree.heading('year',text='Year')
      self.employee_tree.heading('basic_salary',text='Basic Salary')
      self.employee_tree.heading('t_days',text='T Days')
      self.employee_tree.heading('absent_days',text='Absent Days')
      self.employee_tree.heading('medical',text='Medical')
      self.employee_tree.heading('pf',text='PF')
      self.employee_tree.heading('convence',text='Convence')
      self.employee_tree.heading('net_salary',text='Net Salary')
      self.employee_tree.heading('salary_receipt',text='Salary Receipt')
      self.employee_tree['show']='headings'
      self.employee_tree.column('e_id',width=10)
      self.employee_tree.column('designation',width=100)
      self.employee_tree.column('name',width=100)
      self.employee_tree.column('age',width=100)
      self.employee_tree.column('gender',width=100)
      self.employee_tree.column('email',width=100)
      self.employee_tree.column('hr_location',width=100)
      self.employee_tree.column('doj',width=10)
      self.employee_tree.column('dob',width=10)
      self.employee_tree.column('experience',width=100)
      self.employee_tree.column('proof_id',width=100)
      self.employee_tree.column('contact',width=100)
      self.employee_tree.column('status',width=100)
      self.employee_tree.column('address',width=200)
      self.employee_tree.column('month',width=10)
      self.employee_tree.column('year',width=10)
      self.employee_tree.column('basic_salary',width=100)
      self.employee_tree.column('t_days',width=100)
      self.employee_tree.column('absent_days',width=100)
      self.employee_tree.column('medical',width=100)
      self.employee_tree.column('pf',width=100)
      self.employee_tree.column('convence',width=500)
      self.employee_tree.column('net_salary',width=100)
      self.employee_tree.heading('salary_receipt',width=100)
      self.employee_tree.pack(fill=BOTH,expand=1)
      self.root2.mainloop()
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()