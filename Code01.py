def countResponseTimeRegressions(responseTimes):
    avg_list = []
    count = 0

    for i in range(1, len(responseTimes)):
        prev_avg = sum(avg_list) / len(avg_list) if avg_list else responseTimes[0]

        if responseTimes[i] > prev_avg:
            count += 1
        else:
            count = 1

        avg_list.append(responseTimes[i])

    return count


if __name__ == '__main__':
    responseTimes_count = int(input().strip())
    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)
    print(result)
