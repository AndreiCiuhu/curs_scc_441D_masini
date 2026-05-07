pipeline {
    agent any

    environment {
        API_NINJAS_KEY = credentials('API_NINJAS_KEY')
    } 

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                
                sh './venv/bin/pip install -r requirements.txt'
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
                sh "docker run -d -p 5000:5000 --env API_NINJAS_KEY=${env.API_NINJAS_KEY} --name masini-container masini-app"
            }
        }
    }
}
