/* Jenkins */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    pwd
                    ls -l
                    python3 --version
                '''
            }
        }

        stage('Create virtual environment') {
            steps {
                echo 'Creare mediu virtual...'
                sh '''
                    rm -rf .venv
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirement.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                echo 'Verificare calitate cod cu pylint...'
                sh '''
                    echo "\\n\\nVerificare app/lib/*.py cu pylint"
                    .venv/bin/pylint --exit-zero app/lib/*.py

                    echo "\\n\\nVerificare app/routes/*.py cu pylint"
                    .venv/bin/pylint --exit-zero app/routes/*.py

                    echo "\\n\\nVerificare tests/*.py cu pylint"
                    .venv/bin/pylint --exit-zero tests/*.py

                    echo "\\n\\nVerificare masini.py cu pylint"
                    .venv/bin/pylint --exit-zero masini.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    .venv/bin/python -m pytest
                '''
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t mazda-imagine .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f masini-container || true'
                sh "docker run -d -p 5000:5000 --name masini-container mazda-imagine"
            }
        }
    }
}
