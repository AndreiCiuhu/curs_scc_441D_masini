pipeline {
  agent any

  stages {
    stage('Install dependencies') {
      steps {
        sh 'chmod +x ./activeaza_venv_jenkins'
        sh './activeaza_venv_jenkins'
      }
    }

    stage('Run tests') {
      steps {
        sh '. .venv/bin/activate && pytest app/tests/teste.py'
      }
    }

    stage('Build image') {
      steps {
        sh 'docker build -t masini .'
      }
    }

    stage('Deploy') {
        steps {
            sh 'docker stop masini || true'
            sh 'docker rm masini || true'
            sh 'docker run -d -p 5011:5011 --name masini masini'
        }
    }
  }

}
