/* Jenkinsfile - Pamfir Cosmin Alexandru - Skoda */

pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Build proiect Flask - Masini / Skoda'
                sh '''
                    echo "Director curent:"
                    pwd

                    echo "Fisiere proiect:"
                    ls -l

                    echo "Creare mediu virtual pentru Jenkins:"
                    python3 -m venv .venv_jenkins

                    echo "Activare mediu virtual si instalare dependinte:"
                    . .venv_jenkins/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirement.txt
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
                echo 'Verificare calitate cod cu pylint'
                sh '''
                    . .venv_jenkins/bin/activate

                    echo "\\n\\nVerificare app/lib/*.py cu pylint"
                    pylint --exit-zero app/lib/*.py

                    echo "\\n\\nVerificare app/routes/*.py cu pylint"
                    pylint --exit-zero app/routes/*.py

                    echo "\\n\\nVerificare app/test/*.py cu pylint"
                    pylint --exit-zero app/test/*.py

                    echo "\\n\\nVerificare masini.py cu pylint"
                    pylint --exit-zero masini.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Rulare teste unitare pentru functionalitatea Skoda'
                sh '''
                    . .venv_jenkins/bin/activate

                    echo "Rulare teste cu pytest:"
                    PYTHONPATH=. pytest app/test
                '''
            }
        }

        stage('Unit Testing cu unittest') {
            agent any
            steps {
                echo 'Rulare teste unitare si cu unittest'
                sh '''
                    . .venv_jenkins/bin/activate

                    echo "Rulare teste cu unittest:"
                    PYTHONPATH=. python3 -m unittest discover -s app/test
                '''
            }
        }

        stage('Docker') {
            agent any
            steps {
                echo 'Test simplu Docker'

                sh '''
                    IMAGE_NAME="skoda-test:${BUILD_NUMBER}"
                    CONTAINER_NAME="skoda-test-container"

                    echo "Sterg containerul vechi daca exista:"
                    docker rm -f $CONTAINER_NAME || true

                    echo "Construiesc imaginea Docker:"
                    docker build -t $IMAGE_NAME .

                    echo "Pornesc containerul:"
                    docker run -d --name $CONTAINER_NAME $IMAGE_NAME

                    echo "Astept 3 secunde:"
                    sleep 3

                    echo "Verific daca ruleaza containerul:"
                    docker ps | grep $CONTAINER_NAME

                    echo "Sterg containerul:"
                    docker rm -f $CONTAINER_NAME

                    echo "Sterg imaginea temporara:"
                    docker rmi -f $IMAGE_NAME || true

                    echo "Test Docker finalizat cu succes."
                '''
            }
        }
    }
}
