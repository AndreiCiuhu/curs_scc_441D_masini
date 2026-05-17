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
                sh 'PYTHONPATH=. ./venv/bin/python3 -m unittest discover -s app/test'
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t imagine-lamborghini .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop container-lamborghini || true'
                sh 'docker rm container-lamborghini || true'
                sh 'docker run -d -p 5001:5000 --name container-lamborghini imagine-lamborghini'
            }
        }
    }
}
