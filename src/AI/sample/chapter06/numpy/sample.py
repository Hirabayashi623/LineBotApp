import numpy

# Verion確認
print(numpy.version.version)

# 乱数の生成　最小値,最大値,個数
rand_ary = numpy.random.randint(140, 190, 100)
print(rand_ary)

# 自力で平均を求める
sum = 0
cnt = 0
for i in rand_ary:
    sum += i
    cnt += 1
print("普通の平均",sum/cnt)

# 算術平均を求める
print("算術平均",rand_ary.mean())

# 加重平均 重みづけが可能
print("加重平均①",numpy.average(rand_ary))

ary = numpy.arange(1,13,1)
print("ary = ", ary)

ary_3_4 = ary.reshape(3,4)
print("ary_3_4 = ", ary_3_4)

print("加重平均①", numpy.average(ary_3_4))
print("加重平均②", numpy.average(ary_3_4, axis=0), "行方向の平均")
print("加重平均③", numpy.average(ary_3_4, axis=1), "列方向の平均")

rand_ary = numpy.random.randint(1, 10, 12)
# print("rand_ary = ", rand_ary)
print("加重平均④", numpy.average(ary, weights=rand_ary))
