# https://www.codewars.com/kata/54e6533c92449cc251001667/solutions/python

        def unique_in_order(iterable):
            solution=[]
            # to compare elements with the next one better use enumerate
            for i in range(len(iterable)):
                if i == 0 or iterable[i] != iterable[i-1]:
                    solution.append(iterable[i])
            return solution