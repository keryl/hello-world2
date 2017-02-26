class BankAccount():
	def deposit(self):
		pass

	def withdraw(self):
		pass

class SavingsAccount(BankAccount):
	def __init__(self):
		self.balance = 500
	def deposit(self, deposit):
		if type(deposit) =! int:
			return 'Invalid deposit amount'
		elif deposit < 0:
			return 'Invalid deposit amount'
		else:
			self.balance += deposit
			return self.balance
	def withdraw(self, withdrawal):
		if type(withdrawal) =! int:
			return 'Invalid withdrawal amount'
		elif withdrawal < 0:
			return 'Invalid withdarwal amount'
		elif (self.balance - withdrawal) < 500:
			return 'Cannot withdraw beyond the minimum account balance'
		elif withdrawal > self.balance:
			return 'Cannot withdraw beyond the current account balance'
		else:
			self.balance -= withdrawal
			return self.balance
class CurrentAccount(BankAccount):
	def __init__(self):
		self.balance = 0
	def deposit(self,deposit):
		if type(deposit) =! int:
			return 'Invalid deposit amount'
		elif deposit < 0:
			return 'Invalid deposit amount'
		else:
			self.balance += deposit
			return self.balance
	def withdraw(self, withdrawal):
		if type(withdrawal) =! int:
			return 'Invalid withdrawal amount'
		elif withdrwal < 0:
			'Invalid withdrawal amount'
		elif withdrawal > self.balance:
			return 'Cannot withdraw beyond the current account balance'
		else:
			self.balance -= withdrawal
			return self.balance



