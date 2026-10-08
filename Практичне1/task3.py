x=int(input())
y=int(input())
if x>0 and y>0:
    print("перша чверть")
elif x<0 and y<0:
    print("третя чверть")
elif x>0 and y<0:
    print("четверта чверть")
elif x<0 and y>0:
    print("друга чверть")
elif x==0 and y==0:
    print("початок координат")
elif x==0:
    print("на осі ОУ")
else:
    print("на осі ОХ")


