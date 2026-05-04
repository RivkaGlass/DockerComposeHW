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
                sh '''
                    docker compose down --remove-orphans || true
                '''
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                    docker compose build
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker compose run --rm tests
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down
        
                    docker compose build
        
                    docker compose up -d --remove-orphans
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker compose logs --tail=50
            '''
        }
    }
}
   