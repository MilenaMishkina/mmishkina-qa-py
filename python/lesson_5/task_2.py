is_raining = True
is_sunny = True

if is_raining and is_sunny:
    print('дождь при солнце')
elif is_sunny and not is_raining:
    print('Сегодня солнечная погода, отличный день для прогулки!')
elif is_raining and not is_sunny:
    print('Сегодня идет дождь, возьмите зонт!')
else:
    print('Сегодня облачно, но без осадков')