secrate = 'giraff'
count_num = 0
count_limit = 3
gusses = ''
out_of_gusses = False
print('HINT ::::: ==== TAll ANIMAL(write your answer simple letters)')
while gusses != secrate and not (out_of_gusses):
    if count_num < count_limit:
        gusses = input('enter gusses :')
        count_num += 1
    else:
        out_of_gusses = True


if out_of_gusses:
    print('you lost')
else:
    print('you won')
