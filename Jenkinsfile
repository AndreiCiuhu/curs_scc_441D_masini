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
                sh 'docker build -t ferrari-imagine .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop masini-container || true'
                sh 'docker rm masini-container || true'
                sh "docker run -d -p 5000:5000 --name masini-container ferrari-imagine"
            }
        }
    }
}
