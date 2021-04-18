if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() 


    """
	format to 2 dec places without truncating 
	a = 2.2234234

	print('%.2f' %a)

    """
    print('%.2f' %(sum(student_marks[query_name])/(len(student_marks[query_name]))))