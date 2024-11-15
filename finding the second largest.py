#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    score=list(map(int,input().split()))
    score=list(set(score))
    score.sort()
    runner_up=score[-2]
    print(runner_up)
