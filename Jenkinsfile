pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Cleanup Old Containers') {
            steps {
                bat 'docker compose down --remove-orphans'
            }
        }

        stage('Build Images') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker compose up --abort-on-container-exit'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker build -t app-ci:latest ./app'
                bat 'docker tag app-ci:latest estergottliwb/app-ci:latest'
                bat 'docker push estergottliwb/app-ci:latest'
            }
        }
    }

    post {
        always {
            bat 'docker compose down'
        }
    }
}