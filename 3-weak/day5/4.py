def find_combi_per(combi):
    while len(combi) > 2:
        combi_per = ''

        for i in range(1, len(combi)):
            sum = int(combi[i - 1]) + int(combi[i])
            combi_per += str(sum % 10)

        combi = combi_per
    return combi

a_phone = input()
b_phone = input()

combi = ''
for i in range(len(a_phone)):
    combi += a_phone[i]
    combi += b_phone[i]

print(find_combi_per(combi))