from collections import deque

def vote(n, student):
    q = deque()
    cnt_dic = {}

    for i in student:
        if i in cnt_dic:
            cnt_dic[i] += 1
        else:
            if len(q) < n:
                q.append(i)
                cnt_dic[i] = 1
            else:
                min_vote = min(cnt_dic.values())
                candidates_to_remove = [k for k, v in cnt_dic.items() if v == min_vote]
                candidates_to_remove = candidates_to_remove[0]
                q.remove(candidates_to_remove)
                del cnt_dic[candidates_to_remove]

                q.append(i)
                cnt_dic[i] = 1

    return sorted(list(q))

n = int(input())
vote_cnt = int(input())
recommended_student = list(map(int, input().split()))

print(*vote(n, recommended_student))