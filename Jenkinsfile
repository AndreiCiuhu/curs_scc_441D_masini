pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirement.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'PYTHONPATH=app ./venv/bin/python3 -m unittest discover -s app/test'
            }
        }
        stage('Build image') {
            steps {
                sh 'docker build -t masini-app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop masini-container || true'
                sh 'docker rm masini-container || true'
                sh "docker run -d -p 5055:5055 --name masini-container masini-app"
            }
        }
    }
}