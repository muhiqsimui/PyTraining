n = int(input())
mark_sheet = [[input(), float(input())] for _ in range(n)]
second = sorted(list(set([marks for name, marks in mark_sheet])))[1]  
print('\n'.join([a for a,b in sorted(mark_sheet) if b == second]))
