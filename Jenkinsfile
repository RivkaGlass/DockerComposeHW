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
                bat 'docker compose up --abort-on-container-exit --exit-code-from tests'
            }
        }
    }

    post {
        always {
            bat 'docker compose down'
        }
    }
}
