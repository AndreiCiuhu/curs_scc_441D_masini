pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create virtual environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'venv/bin/pip install --upgrade pip'
                sh 'venv/bin/pip install flask'
            }
        }

        stage('Run tests') {
            steps {
                sh 'venv/bin/python -m unittest discover -s app/test -p "test_*.py"'
            }
        }
	
	stage('Build Docker image') {
            steps {
                sh 'docker build -t masini-honda-anton-darius .'
            }
        }

        stage('Run Docker container') {
            steps {
                sh 'docker rm -f masini-honda-container || true'
                sh 'docker run -d --name masini-honda-container -p 5000:5000 masini-honda-anton-darius'
            }
        }	
    }
}
