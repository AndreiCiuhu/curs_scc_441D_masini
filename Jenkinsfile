pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install -r requirement.txt
                '''
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
                sh 'docker run -d -p 5000:5000 --name masini-container masini-app'
            }
        }
    }
}
