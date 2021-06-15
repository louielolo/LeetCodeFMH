import sys

class Solution:
    def __init__(self):
        pass
    def add(self,task_array:list,last_batch:list)->list:
        if len(task_array)>1:
            batch_time = task_array[0]
            for i in range(1,len(task_array)):
                batch_time = list(map(lambda x,y:x+y,batch_time,task_array[i]))
            output = list(map(lambda x,y:x+y,batch_time,last_batch))
        else:
            output = list(map(lambda x,y:x+y,task_array[0],last_batch))
        return output

    def period(self,mission:list,task:list) -> int:
        pipeline = mission[0]
        num_task = mission[1]
        t_pipeline = []
        t_batch = []
        batch = int(num_task/pipeline)
        num_last_batch = int(num_task%pipeline)
        for i in range(batch):
            task_array = sorted(task)
            #每个批次的任务时间存为一个list，最后将list元素对应相加，最大的就是作业总时长
            t_batch.append([task_array[j] for j in range(pipeline)])
            for j in range(pipeline):
                task_array.remove(task_array[0])
        last_batch = task_array
        for j in range(pipeline-num_last_batch):
            last_batch.append(0)
        total_task_period = sorted(self.add(t_batch,last_batch),reverse=True)

        return total_task_period[0]
if __name__ == '__main__':
    getline = lambda :sys.stdin.readline().strip()
    mission_raw = getline()
    mission = [int(elem) for elem in mission_raw.split()]
    task_raw = getline()
    task = [int(elem) for elem in task_raw.split()]
    s = Solution()
    print(s.period(mission,task))