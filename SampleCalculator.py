def is_number(input):
	try:
		return int(input);
	except:
		return None;
		
def is_valid_operator(operator):
	return operator in ["+", "-", "/", "*"];
	
def ask_for_a_number(forceValidInput = True):
	user_input = input("Podaj liczbe: ");
	casted_value = is_number(user_input);
	if forceValidInput:
		while casted_value == None:
			user_input = input("Podaj liczbe: ");
			casted_value = is_number(user_input);
	return casted_value;
	
def ask_for_an_operator(forceValidInput = True):
	user_input = input("Podaj operator: ");
	if forceValidInput:
		while not is_valid_operator(user_input):
			user_input = input("Podaj operator: ");
		return user_input;
	else:
		if not is_valid_operator(user_input):
			return None;
		else:
			return user_input;
		
def calculate(operand1, operator, operand2):
	if operand1 == None or operator == None or operand2 == None:
		return None;
	if operator == "+":
		return operand1 + operand2;
	elif operator == "-":
		return operand1 - operand2;
	elif operator == "*":
		return operand1 * operand2;
	elif operator == "/":
		if operand2 == 0:
			print("Error divison by zero");
			return None;
		else:
			return operand1 / operand2;
	else:
		return None;
def simple_calculator():
	end_cond = True;
	while end_cond:
		print("Podaj operand1");
		operand1 = ask_for_a_number(False);
		if operand1 == None:
			end_cond = False;
		else:
			operator = ask_for_an_operator(True);
			print("Podaj operand2");
			operand2 = ask_for_a_number(True);
			result = calculate(operand1, operator, operand2);
			print(f"Result of calculation is: {result}");
		
if __name__ == "__main__":
	simple_calculator();