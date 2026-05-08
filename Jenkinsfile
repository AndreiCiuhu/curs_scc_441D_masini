pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'rm -rf venv'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirement.txt'
            }
        }

        stage('Run unit tests') {
            steps {
                sh 'PYTHONPATH=app ./venv/bin/python3 -m unittest discover -s app/test'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t masini-porsche-fierea .'
            }
        }
    }
}
