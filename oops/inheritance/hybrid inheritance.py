# # it is a combination of different type of inheritance
#
# class parent:
#     def fun(self):
#         print("parent")
# class childA(parent):
#     def fun1(self):
#         print("A")
# class childB(parent):
#     def fun2(self):
#         print("b")
# class childC(childA,childB,parent):
#     def fun3(self):
#
#         print("C")
# obj=childC()
# obj.fun()
# obj.fun1()
# obj.fun2()
# obj.fun3()

# university (univ_name,location)
# colg(clgname)
# course(crs_name)
# student(rollno,name)
#
#
# class university:
#     def setval(self,univ_name,location):
#         self.univ_name=univ_name
#         self.location=location
#         print("university_name:",self.univ_name)
#         print("location:",self.location)
#
# class college(university):
#     def setval1(self,college_name):
#         self.college_name=college_name
#         print("colleage_name:",self.college_name)
#
#
# class course(university):
#     def setval2(self,course_name):
# #         self.course_name=course_name
# #         print("course name:",self.course_name)
# # class student(college,course):
# #     def setval3(self,roll_no,name):
# #         self.roll_no=roll_no
# #         self.name=name
# #         print("roll no:",self,roll_no)
# #         print("name",self.name)
# #
# # obj=student()
# # obj.setval('Kannur University','Kannur')
# # # obj.setval1('CAS COLLEGE MADAYI')
# # # obj.setval2('Mcom')
# # # obj.setval3(8,'SHIGIN M')
# #
# #
# #
#
# class university:
#     def __init__ (self,univ_name,location):
#         self.univ_name=univ_name
#         self.location=location
#
# class college(university):
#     def __init__ (self,college_name,univ_name,location):
#         university.__init__ (self,univ_name,location)
#         self.college_name=college_name
#
#
#
# class course(university):
#     def __init__ (self,course_name,college_name,univ_name,location):
#         university.__init__(self,univ_name,location)
#         self.course_name=course_name
#
# class student(college,course):
#     def __init__ (self,roll_no,name,course_name,college_name,univ_name,location,):
#         college. __init__(self,college_name,univ_name,location)
#         course.__init__(self,course_name,college_name,univ_name,location)
#
#         self.roll_no=roll_no
#         self.name=name
#         print("roll no:",self.roll_no)
#         print("name",self.name)
#
#         print("university_name:",self.univ_name)
#         print("location:",self.location)
#         self.college_name = college_name
#         print("colleage_name:", self.college_name)
#         print("course name:", self.course_name)
#
#
# obj=student(12,"ayshu","mbbs","gmc","kerala","palakkad")