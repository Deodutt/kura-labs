import boto3

# Let's use Amazon S3
s3 = boto3.resource("s3")
# print("hello world")


# s = boto3.resource("s3")
# print(dir(s))


def printBucketNames():
    for bucket in s3.buckets.all():
        # print(bucket.name)
        return print(bucket.name)


print(printBucketNames())


## Upload a new file3
# data = open("test.jpg", "rb")
# s3.Bucket("my-bucket").put_object(Key="test.jpg", Body=data)