pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t masini-renault-app .'
            }
        }

        stage('Run tests in Docker') {
            steps {
                sh 'docker run --rm masini-renault-app python -m unittest discover -s app/test'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker rm -f masini-renault-jenkins-container || true'
                sh 'docker run -d -p 5000:5000 --name masini-renault-jenkins-container masini-renault-app'
            }
        }
    }
}
