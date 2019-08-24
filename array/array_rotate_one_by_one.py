class job:
    def rotate(self,arr):
        temp = arr[0]
        for i in range(0,len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = temp

        return arr
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    job = job()
    arr = job.rotate(arr)
    arr = job.rotate(arr)
    arr = job.rotate(arr)

    for item in arr:
        print(item)
