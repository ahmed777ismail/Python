print('--- Welcome to the Professional BMI Analyzer ---')

tips = {
  'Underweight': 'Try to include more energy-dense foods and healthy fats in your diet',
  'Normal weight': 'Great job! Maintain your balanced diet and regular physical activity',
  'Overweight': 'Consider increasing your daily activity and focusing on a portion-controlled diet',
  'Obesity': '''It's recommended to consult a nutritionist for a personalized health plan'''
}
history = []

while True:
  weight = float(input('Please enter your weight in kilograms: (or 0 to exit): '))
  if weight == 0:
    for record in history:
      print(record)
    break
  height = float(input('Please enter your height in centimeters:'))
  height = height / 100
  bmi_calculation = weight / (height ** 2)
  bmi_calculation = round(bmi_calculation,2)
  # category = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']

  
  if weight <= 0 or height <= 0:
    print('Invalid Input: Your input should be in positive numbers')
  else:
    if bmi_calculation < 18.5:
      category = 'Underweight'
    elif bmi_calculation >= 18.5 and bmi_calculation <= 24.9:
      category = 'Normal weight'
    elif bmi_calculation >= 25 and bmi_calculation <= 29.9:
      category = 'Overweight'
    elif bmi_calculation >= 30:
      category = 'Obesity'
    print(f'You are {category}')
    print(f"Health Tip: {tips[category]}")
    history.append(f'{bmi_calculation} ({category})')