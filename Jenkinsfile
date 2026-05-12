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

        stage('Docker - containerizare si test HTTP') {
            agent any
            steps {
                echo 'Construire imagine Docker, pornire container si verificare ruta Skoda'

                sh '''
                    echo "Sterg containerul vechi, daca exista:"
                    docker rm -f container-skoda-pamfir-jenkins || true

                    echo "Construiesc imaginea Docker:"
                    docker build -t masini-skoda-pamfir .

                    echo "Pornesc containerul pe portul 5001:"
                    docker run -d --name container-skoda-pamfir-jenkins -p 5001:5000 masini-skoda-pamfir

                    echo "Astept cateva secunde sa porneasca aplicatia:"
                    sleep 5

                    echo "Verific ruta /masini/skoda:"
                    curl -f http://127.0.0.1:5001/masini/skoda

                    echo "\\n\\nVerific ruta /masini/skoda/descriere:"
                    curl -f http://127.0.0.1:5001/masini/skoda/descriere

                    echo "\\n\\nAfisez logurile containerului:"
                    docker logs container-skoda-pamfir-jenkins

                    echo "Opresc si sterg containerul:"
                    docker stop container-skoda-pamfir-jenkins
                    docker rm container-skoda-pamfir-jenkins
                '''
            }
        }
    }
}
