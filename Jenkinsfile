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
                script {
                    docker.build("flask-jenkins-app")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 flask-jenkins-app'
                }
            }
        }
    }
}

