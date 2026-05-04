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
        stage('Deploy') {
            steps {
                // withCredentials([usernamePassword(
                //     credentialsId: 'dockerhub-creds',
                //     usernameVariable: 'DOCKER_USER',
                //     passwordVariable: 'DOCKER_PASS'
                // )]) {
                //     bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                //     bat 'docker build -t app-ci:latest ./app'
                //     bat 'docker tag app-ci:latest estergottliwb/app-ci:latest'
                //     bat 'docker push estergottliwb/app-ci:latest'
                // }
                bat 'docker login -u estergottliwb -p ETti65055!'
                bat 'docker build -t app-ci-cd:latest ./app'
                bat 'docker tag app-ci-cd:latest estergottliwb/app-ci-cd:latest'
                bat 'docker push estergottliwb/app-ci-cd:latest'
            }
        }
    }

    post {
        always {
            bat 'docker compose down'
        }
    }
}
