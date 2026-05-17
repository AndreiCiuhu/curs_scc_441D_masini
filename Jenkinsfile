pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirement.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                . venv/bin/activate
                PYTHONPATH=. python -m unittest discover -s app/test
                '''
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t masini-alpine .'
            }
        }

        stage('Deploy') {
          steps {
             sh 'docker stop masini-alpine-container || true'
             sh 'docker rm masini-alpine-container || true'
             sh 'docker run -d -p 5000:5000 --name masini-alpine-container masini-alpine'
          }
        }
    }
}