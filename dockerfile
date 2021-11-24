FROM lambci/lambda:build-python3.8

ENV AWS_DEFAULT_REGION us-west-2

# RUN pipenv --python 3.8
RUN pipenv install --system
# RUN pipenv install zappa

COPY . .

# CMD aws lambda update-function-code --function-name mylambda --zip-file fileb://lambda.zip
CMD pipenv run zappa deploy