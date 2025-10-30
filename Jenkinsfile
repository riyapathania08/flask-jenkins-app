pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t flask-jenkins-app:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                bat 'docker rm -f flask-jenkins-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name flask-jenkins-container flask-jenkins-app:latest'
            }
        }
    }

    post {
        success {
            echo '✅ Build and Deployment successful!'
        }
        failure {
            echo '❌ Build or Deployment failed!'
        }
    }
}
