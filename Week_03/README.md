代码模板：

1. 递归求解问题



2. 分治代码模板


        def divide_conquer(problem,param1,param2,param2,...):
            #recursion terminator
            if problem is None:
                print_result
                return

            #prepare data
            data=prepare_data(problem)

            #conquer subproblems
            subresult1=self.divide_conquer(subproblems[0],p1,...)
            subresult2=self.divide_conquer(subproblems[1],p1,...)
            subresult3=self.divide_conquer(subproblems[2],p1,...)

            #process and generate the final result
            result=process_result(subresult1,subresult2,subresult3,...)

            #revert the current level state



3. 回溯求解问题

        result=[]
        def backtrack(路径，选择列表):
            if 满足结束条件：
                result.add(路径）
                return
            for 选择 in 选择列表：
                做选择
                backtrack(路径，选择列表）
                撤销选择