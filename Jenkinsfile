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
    }
}
