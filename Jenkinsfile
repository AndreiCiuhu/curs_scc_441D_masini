pipeline {

    agent any

    stages {

        stage('Check files') {
            steps {
                sh 'pwd'
                sh 'ls -R'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirement.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'PYTHONPATH=. python3 -m unittest discover -s app/test -v'
            }
        }

    }
}