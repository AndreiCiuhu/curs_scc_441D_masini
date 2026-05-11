pipeline {
    agent any

    environment {
        IMAGE_NAME = 'masini-mercedes'
        CONTAINER_NAME = 'masini-mercedes-container'
        APP_PORT = '5000'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run unit tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest app/test
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Deploy container') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 ${IMAGE_NAME}:latest
                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes. Aplicatia Mercedes-Benz ruleaza in container.'
        }

        failure {
            echo 'Pipeline esuat. Verifica stage-ul la care a aparut eroarea.'
        }
    }
}
