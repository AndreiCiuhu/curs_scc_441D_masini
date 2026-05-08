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
        sh '. .venv/bin/activate && pytest -q'
      }
    }

    stage('Build image') {
      steps {
        sh 'docker build -t masini .'
      }
    }

    stage('Deploy') {
      steps {
        sh 'docker run -d -p 5011:5011 --name masini masini'
      }
    }
  }

}
