def countResponseTimeRegressions(responseTimes):
    avg=()
    count=0
    for i in range(1,len(responseTimes)):
        pre_avg=sum(avg)/len(avg)
        if responseTimes[i]>pre_avg:
            count+=1
            avg.append(responseTimes[i])# Write your code here
        else:
            count=1
            avg.append(responseTimes[i])
    return count
if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
