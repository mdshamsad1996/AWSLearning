##### AWSLearning
### FileZilla : I have used to transffered my local cpuload.py file to ec2 instance

### Steps to check auto scaling policy

1. Connect to ec2 instance using ssh 
2. Transferred cpuload.py to ec2 instance using FileZilla Software
3. Install Python3 in ec2 Instance
```
    sudo yum install python3
```
4. Run python script to exhaust CPU ( python3 cpuload.py)

Now AutoScalingOut Policy will be trigerred by cloudWatch Alarm
 And Now we can stopped execution of python file by CTRL+C
 AutoScalingIn Policy will be triggered by CloudWatch Alarm
