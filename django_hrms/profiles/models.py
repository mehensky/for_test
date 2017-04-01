#-*-coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

sex_choices = (
		('F','Female'),
		('M','Male'),
	)

status_choices = (
		('Z','在职'),
		('L','离职'),
		('O','停职'),
		('T','退休'),

	)

assignment_status_choices = (
		('A','已外派'),
		('B','未外派'),

	)

condition_choices = (
		('attend','正常上班'),
		('sentout','出差'),
		('late','迟到'),
		('earlyout','早退'),
		('absent','旷工'),

	)



#人员基本信息表
class person(models.Model):
	employee_id = models.ForeignKey(User,primary_key = True,unique=True)
	name = models.CharField('name',max_length = 30,)
	sex = models.CharField(max_length = 1,choices = sex_choices )
	birth = models.DateField('birth',help_text = '输入格式为 YYYY-MM-DD',null = True)
	birth_place = models.CharField('birth_place',max_length = 50)
	nation = models.CharField('nation',max_length=20)
	identification_num = models.CharField('identification_num',max_length = 18)
	political = models.CharField(null = True,max_length = 50)
	duty = models.ForeignKey('duties')
	department = models.ForeignKey('department')
	graduation_school = models.CharField(null = True,max_length = 30)
	graduation_date = models.DateField(null = True,help_text = '输入格式为 YYYY-MM-DD')
	education = models.CharField(max_length = 10)
	address = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 11)
	email = models.EmailField(null = True)
	status = models.CharField(choices = status_choices,max_length = 1)

	def __unicode__(self):
		return self.name



#部门信息表
class department(models.Model):
	department_name = models.CharField(max_length = 30)
	department_comment = models.CharField(max_length = 500)

	def __unicode__(self):
		return self.department_name


#职务信息表 
class duties(models.Model):
	duty_id = models.CharField(max_length = 4 ,primary_key=True)
	duty_name = models.CharField(max_length = 30 )
	department = models.ForeignKey('department')
	salary_lev_id = models.ForeignKey('salary_standard')

	def __unicode__(self):
		return self.duty_name




#外派单位信息表
class company(models.Model):
	company_name = models.CharField(max_length = 30,unique=True)
	company_loca = models.CharField(max_length = 50)

	def __unicode__(self):
		return  self.company_name






#考勤数据表   通过日期区间跟ID确定一个员工的考勤情况      员工只能通过 now 按钮输入，并且可以输入多次，不过选最早的当签到，最晚的当签退
class attendance_data(models.Model):                 
	employee_id = models.ForeignKey('person')       #employee_id作为一个对象，拥有对应person的所有属性且能对其进行访问
	attendance_day = models.DateField()
	sign_in = models.TimeField()
	sign_out = models.TimeField()
	class Meta:
		unique_together = ("employee_id","attendance_day")
	def __unicode__(self):
		return u'%s %s %s %s '  % (self.employee_id.name,self.attendance_day,sign_in,'sign_out')     #可以进行多个参数的显示设置

  
#各公司考勤时间标准表       
class attendance_standard(models.Model):
	company = models.ForeignKey('company')
	regular_sign_in = models.TimeField()
	regular_sign_out = models.TimeField()

	def __unicode__(self):
		return u'%s' % self.company

#考勤表       这个表建立了考勤原数据跟考勤标准的联系与对比，同时能够将结果存在condition_status中，condition_status也就是我们要进行考核的内容
class attendance(models.Model):
	attendance_data = models.ForeignKey('attendance_data')      
	attendance_standard =  models.ForeignKey('attendance_standard')
	condition_status = models.BooleanField(choices = condition_choices)	

	def __unicode__(self):
		return u'%s' % self.attendance_data

#工资标准信息表
class salary_standard(models.Model):
	salary_lev_id = models.CharField(max_length = 4, primary_key=True)
	salary_lev_name = models.CharField(max_length = 10)
	basic_salary = models.DecimalField(max_digits = 11 , decimal_places = 2 )
	subsidy = models.DecimalField(max_digits = 11 , decimal_places = 2 )
	housing_fund = models.DecimalField(max_digits = 11 , decimal_places = 2 )
	social_security = models.DecimalField(max_digits = 11 , decimal_places = 2 )
	bonus = models.DecimalField(max_digits = 11 , decimal_places = 2 )
    
    	def __unicode__(self):
    		return self.salary_lev_name

#工资记发信息表
class salary_cs(models.Model):
	attendance = models.ForeignKey('attendance')
	person = models.ForeignKey('person')
	salary_should_sent_time = models.CharField(max_length=30)
	salary_standard = models.ForeignKey('salary_standard')
	salary_total = models.DecimalField(max_digits = 11 , decimal_places = 2 )
	salary_actual = models.DecimalField(max_digits = 11 , decimal_places = 2 )
	sent_salary_status = models.BooleanField("工资是否已发放？", default=False)