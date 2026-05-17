pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirement.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'PYTHONPATH=. python3 -m unittest discover -s app/test'
            }
        }
    }
}
