pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirement.txt'
                sh './venv/bin/python3 -m unittest discover -s app/test'
            }
        }
        stage('Run tests') {
            steps {
                sh 'PYTHONPATH=app python -m unittest discover -s app/test'
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
                sh 'docker run -d -p 5000:5000 --env-file .env --name masini-container masini-app'
            }
        }
    }
}