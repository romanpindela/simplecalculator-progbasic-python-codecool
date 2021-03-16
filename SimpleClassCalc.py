class SimpleCalculator:
	def __init__(self):
		self.operand1 = None;
		self.operator = None;
		self.operand2 = None;
	def calculate(self):
		if self.operand1 == None or self.operator == None or self.operand2 == None:
			return None;
		if self.operator == "+":
			return self.operand1 + self.operand2;
		elif self.operator == "-":
			return self.operand1 - self.operand2;
		elif self.operator == "*":
			return self.operand1 * self.operand2;
		elif self.operator == "/":
			if self.operand2 == 0:
				print("Error divison by zero");
				return None;
			else:
				return self.operand1 / self.operand2;
		else:
			return None;
def simple_calculator():
	calc1 = SimpleCalculator()
	calc1.operand1 = 4;
	calc1.operand2 = 5;
	calc1.operator = "+";
	calc2 = SimpleCalculator()
	
	print(calc1.calculate());
	print(calc2.calculate());
if __name__ == "__main__":
	simple_calculator();