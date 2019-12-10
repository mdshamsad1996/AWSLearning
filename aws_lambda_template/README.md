#### Create cloudformation template and try to deploy the lambda via CLI launching the                       cloudformation stack and Test the lambda

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

