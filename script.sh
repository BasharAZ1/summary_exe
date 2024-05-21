#!/bin/bash

# Update package lists
sudo apt-get update

# Install Git
sudo apt-get install -y git

# Install Docker
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce

# Clone the GitHub repository
git clone https://github.com/BasharAZ1/summary_exe.git

# Navigate into the repository directory
cd summary_exe

# Create the .env file with specific environment variables
cat <<EOF > .env
S3_BUCKET=value1
OBJECT_Name=value2
FLASK_APP=value3
EOF
# Build the Docker image
sudo docker build -t lab .



# Run the Docker container with the .env file
sudo docker run -p 5001:5000 --env-file .env lab
