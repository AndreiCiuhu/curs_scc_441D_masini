pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirement.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh '. venv/bin/activate && python3 -m pytest'
            }
        }
    }
}
