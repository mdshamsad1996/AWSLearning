### Secure API GW with JWT Authentication.
    
For more information check below : https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html

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
         
Install sam cli using below command

    pip install aws-sam-cli
Setting up AWS Credentials using below command
        
        aws configure
        
#### Install dependencies
    pip install -r requirements.txt

#### Deploy application using below steps
    #step1: Validate template using below command
         sam validate -t template.yml
         
    #step2:  Build your application
         sam build -t template.yml
         
    #step3: Deploy  application
            sam deploy --guided

            
##### Once application will deploy check the response by APIendpoint url and by providing the authorization value 


        APIendpoint_url :https://<restapiid>.execute-api.us-east-1.amazonaws.com/Stage/
        Update this url in src/http_response.py file

   
            
##### Run unittest case using below command
      
       python -m unittest

##### Set up linter

  1. Generate pylintrc file using below command (for pylint tool)
   
             pylint --generate-rcfile > .pylintrc
  2. create setup.config for pycodestyle
        
            touch setup.config
  3. create linter script in scripts folder

##### Run lint using below command

        sh script/lint.sh

#### Reference: I have taken help from below link

 https://auth0.com/blog/securing-aws-http-apis-with-jwt-authorizers/#Add-a-JWT-Authorizer-to-Your-API

        
    
    
       
        
            


