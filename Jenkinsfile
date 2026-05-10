pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/dev_gavra_dragos']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/AndreiCiuhu/curs_scc_441D_masini.git',
                        credentialsId: 'github-pat'
                    ]]
                ])
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t masini:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm masini:${BUILD_NUMBER} pytest app/test/ -v'
            }
        }
    }

    post {
        always {
            sh 'docker rmi masini:${BUILD_NUMBER} || true'
        }
    }
}
