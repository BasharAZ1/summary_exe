
# Flask Application with AWS Deployment

This Flask application allows users to enter their name and email and store them locall db(sqlite), and it greets them with a personalized message and a picture stored in an S3 bucket. The application is deployed on AWS EC2 with a load balancer and an auto-scaling group.

## Features

- User registration with name and email
- Personalized greeting page
- Picture retrieved from an S3 bucket
- Deployed on AWS EC2 with load balancing and auto-scaling

## Prerequisites

- AWS Account
- AWS CLI configured
- An S3 bucket with your picture

## Setup

### 1. Configure AWS S3 Bucket

Ensure you have a bucket in AWS S3 (private) with the picture you want to display. Update the Flask application to use your bucket and picture.


### 2. Deploy to AWS EC2

1. **Launch an EC2 Instance:**

    - Go to the AWS Management Console.
    - Navigate to the EC2 Dashboard.
    - Click "Launch Instance."
    - Follow the prompts to configure and launch your instance.
    - add role thats allow ec2 access S3 bucket

2. **Connect to Your EC2 Instance:**

    - Once your instance is running, connect to it via SSH:
    
    ```bash
    ssh -i /path/to/your-key-pair.pem ec2-user@your-ec2-public-dns
    ```

3. **Install Docker and Git:**

    - Update the package list:

    ```bash
    sudo yum update -y
    ```

    - Install Docker:

    ```bash
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    ```

    - Install Git:

    ```bash
    sudo yum install git -y
    ```

4. **Clone Your Repository:**

    ```bash
    git clone https://github.com/BasharAZ1/summary_exe.git
    cd summary_exe
    nano .env
    ```
    - enter:
        - S3_BUCKET= your bucket name
        - OBJECT_Name = your_image_name
        - S3_KEY_ID=your S3 key
        - S3_ACCESS_KEY=your s3 access
        - FLASK_APP=app.py





5. **Build and Run Your Docker Image:**

    - Build your Docker image:

    ```bash
    docker build -t your-docker-image-name .
    ```

    - Run your Docker container on port 5001:

    ```bash
    docker run -d -p 5001:5000 your-docker-image-name
    ```

### 3. Set Up Load Balancer and Auto-Scaling

1. **Create a Load Balancer:**

    - Navigate to the EC2 Dashboard.
    - Create target group and choose and choose your ec2 
    - Under "Load Balancing," choose "Load Balancers."
    - Click "Create Load Balancer" and follow the prompts to set up a load balancer.
    - choose Application Load Balancer 
    - enter port 5001


2. **Set Up Auto-Scaling Group:**
    - Create launch template
    - in  Advanced details userdata copy the script.sh
    - Under "Auto Scaling," choose "Auto Scaling Groups."
    - Click "Create Auto Scaling group" and follow the prompts.
    - in step3 choose your load balncer
    - in step 4 Scaling choose Max desired capacity 3
    - Attach the load balancer to the auto-scaling group.

## Usage

Once the setup is complete, navigate to the load balancer's DNS name to access the application. Enter your name and email, and you will be greeted with a personalized message and the picture from your S3 bucket.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [BasharAz1](https://github.com/BasharAZ1) for developing the application.



## Documentation:
https://docs.google.com/document/d/1ZBt_B0_Fetpr06OfBV6Lq49a9PwLcULIEvWYePjnPMM/edit
