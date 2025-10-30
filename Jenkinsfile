pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/riyapathania08/flask-jenkins-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-jenkins-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 flask-jenkins-app'
            }
        }
    }
}
