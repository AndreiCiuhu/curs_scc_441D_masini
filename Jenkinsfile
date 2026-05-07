pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checkout repository'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirement.txt'
            }
        }

        stage('Run unit tests') {
            steps {
                sh './venv/bin/python3 -m unittest app/test/test_rollsroyce.py'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t masini-rollsroyce-neacsu-roxana .'
            }
        }

        stage('Run Docker container') {
            steps {
                sh 'docker stop masini-rollsroyce-container || true'
                sh 'docker rm masini-rollsroyce-container || true'
                sh 'docker run -d -p 5000:5000 --name masini-rollsroyce-container masini-rollsroyce-neacsu-roxana'
            }
        }
    }
}
