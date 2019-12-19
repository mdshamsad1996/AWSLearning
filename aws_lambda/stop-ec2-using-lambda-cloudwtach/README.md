#### Automate to stop ec2 to across all region using cloud formation for lambda deploy using sam cli

Make sure python (preferred python3.7) is added to path.

      python --version
       or		
     python3.7 --version
     
 Install virtualenv using pip.

     pip install virtualenv 
   
 First create a virtual environment for the project.
 
    virtualenv -p python3.7 venv or virtualenv venv
       . venv/bin/activate (Linux)
       . venv/Scripts/activate (windows)
       
  install dependencies for AWS Lambda
 
    pip install -r requirements.txt -t ./

Note: Use of inline parameters in stop-ec2-cloudwatch-rule.YAMl
```
 Arn: !Sub 
            - arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:${lambdaFunctionName}
            - lambdaFunctionName: !ImportValue AWSLambdaHandlerARNForCloudWatchRules
 Id: "StopEc2InstancesRule"
```

Install sam cli using below command
```
pip install aws-sam-cli
```
After having Cloudformation template yaml validate using below command
```
sam validate -t template.yaml
```
Sam Build
```
sam build -m requirement.txt
        or
sam build (If it is requirements.txt file)
```
sam package
```
sam package --template-file template.yaml  --s3-bucket my-bucket --output-template-file out.yaml
```

sam deploy
```
sam deploy --template-file out.yaml --stack-name StackForAWSLambda --s3-bucket my-bucket  --capabilities  CAPABILITY_IAM
```

deploy stop-ec2-cloudwatch-rule.YAML template
```
aws cloudformation deploy --template-file stop-ec2-cloudwatch-rule.YAML --stack-name stackForCloudWatchRule

```



