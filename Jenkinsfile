pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker compose -p jenkins-notes build'
            }
        }

        stage('DB') {
            steps {
                sh 'docker compose -p jenkins-notes up -d db'
            }
        }

        stage('Run App') {
            steps {
                sh 'docker compose -p jenkins-notes run --rm app || true'
            }
        }
    }
}