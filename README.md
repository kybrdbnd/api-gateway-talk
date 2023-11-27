# api-gateway-dependencies
AWS lambda for API Gateway talk in Pydelhi Meetup

# Pre-requsite
1. Configure AWS credentials in your system.
2. Install AWSume for easy access to your profile
3. Install nodeJS 20.X
4. Install Python 3.10.X

## How to run the setup

1. Assume role in your AWS account using awsume.
```bash
awsume <name_of_your_aws_profile>
```
2. Create virtualenv using the following command
```bash
python -m venv venv
```
3. Activate the virtualenv
```bash
source venv/bin/activate
```
4. Install the dependencies
```bash
pip install -r requirements.txt
```
5. Run the scripts.
```bash
cd scripts
python create_table.py
python create_table_entries.py
```
6. Install the package dependencies
```bash
cd ..
npm install
```
7. Deploy the serverless app from the root directory
```bash
serverless deploy
```