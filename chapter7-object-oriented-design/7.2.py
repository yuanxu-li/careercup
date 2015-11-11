# 7.2 Call Center: Imagine you have a call center with three levels of employees: respondent, manager, and director.
# An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle
# the call, he or she must escalate the call to a manager. If the manager is not free or not able to handle it,
# then the call should be escalated to a director. Design the classes and data structures for this problem.
# Implement a method dispatchCall() which assigns a call to the first available employee.

from collections import deque
import pdb


class CallCenter:
	def __init__(self):
		self.respondents = deque()
		self.managers = deque()
		self.directors = deque()
		self.calls = []
		self.calling = {}

	def register_employee(self, employee_type="Respondent"):
		if employee_type == "Respondent":
			self.respondents.appendleft(Respondent())
		elif employee_type == "Manager":
			self.managers.appendleft(Manager())
		elif employee_type == "Director":
			self.directors.appendleft(Director())
		else:
			print("Choose type from Respondent(default), Manager, or Director")

	def dispatch_call(self, level):
		call = Call(len(self.calls), level)
		call_id = call.id
		if call.level == 1:
			if len(self.respondents) > 0:
				r = self.respondents.pop()
				self.calling[call_id] = r
				r.assign()
			elif len(self.managers) > 0:
				m = self.managers.pop()
				self.calling[call_id] = m
				m.assign()
			elif len(self.directors) > 0:
				d = self.directors.pop()
				self.calling[call_id] = d
				d.assign()
			else:
				print("All respondents busy now. Please try later!")
				return
		elif call.level == 2:
			if len(self.managers) > 0:
				m = self.managers.pop()
				self.calling[call_id] = m
				m.assign()
			elif len(self.directors) > 0:
				d = self.directors.pop()
				self.calling[call_id] = d
				d.assign()
			else:
				print("All respondents busy now. Please try later!")
				return 
		elif call.level == 3:
			if len(self.directors) > 0:
				d = self.directors.pop()
				self.calling[call_id] = d
				d.assign()
			else:
				print("All respondents busy now. Please try later!")
				return 
		else:
			print("Call level unrecognized!")
			return
		self.calls.append(call)
		return call_id


	def release_call(self, call_id):
		e = self.calling[call_id]
		e.release()
		if isinstance(e, Director):
			self.directors.appendleft(e)
		elif isinstance(e, Manager):
			self.managers.appendleft(e)
		elif isinstance(e, Respondent):
			self.respondents.appendleft(e)
		else:
			print("unrecognized employees!")
			
class Call:
	def __init__(self, id, level=1):
		self.id = id
		self.level = level

class Employee:
	def __init__(self):
		self.free = True

	def assign(self):
		self.free = False

	def release(self):
		self.free = True

class Respondent(Employee):
	def __init__(self):
		super().__init__()
		self.level = 1

class Manager(Employee):
	def __init__(self):
		super().__init__()
		self.level = 2

class Director(Employee):
	def __init__(self):
		super().__init__()
		self.level = 3

if __name__ == "__main__":
	center = CallCenter()
	center.register_employee("Respondent")
	center.register_employee()
	center.register_employee()
	center.register_employee()
	center.register_employee("Manager")
	center.register_employee("Manager")
	center.register_employee("Director")
	# call1 = center.dispatch_call(1)
	# call2 = center.dispatch_call(1)
	# call3 = center.dispatch_call(1)
	# call4 = center.dispatch_call(1)
	# call5 = center.dispatch_call(2)
	# call6 = center.dispatch_call(3)
	# center.release_call(call1)
	# center.release_call(call2)
	pdb.set_trace()


