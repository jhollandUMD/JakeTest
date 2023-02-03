score = float(input('What is your score? '))

if score < 0:
    print('Negative')
elif score > 0:
    print('Positive')
else:
    print('Neutral')