pipeline {
    agent any

    environment {
        IMAGE_NAME = 'masini-mclaren'
        CONTAINER_NAME = 'masini-mclaren-container'
        APP_PORT = '5000'
    }

    stages {
        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'ls -la'
            }
        }

        stage('Create virtual environment') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/pip install -r requirement.txt'
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '.venv/bin/pylint app/lib/biblioteca_masini.py app/routes/mclaren.py masini.py --disable=C0114,C0116,W0611,R1705 || true'
            }
        }

        stage('Unit Testing cu unittest') {
            steps {
                sh 'PYTHONPATH=. .venv/bin/python -m unittest discover -s app/test'
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f ${CONTAINER_NAME} || true'
                sh 'docker run -d -p ${APP_PORT}:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest'
            }
        }

        stage('Verify container') {
            steps {
                sh 'docker ps'
                sh 'docker logs ${CONTAINER_NAME}'
            }
        }
    }
}
