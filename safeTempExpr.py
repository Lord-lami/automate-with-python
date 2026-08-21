print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = float(input())
if scale == "C" and degrees >= 16 and degrees <= 38 or scale == "F" and degrees >= 60.8 and degrees <= 100.4:
    print('Safe')
else:
    print('Dangerous')