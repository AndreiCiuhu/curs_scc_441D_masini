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
        sh 'docker stop masini|| true'
        sh 'docker rm masini || true'
        sh 'docker run -d -p 5011:5011 --name masini masini'
      }
    }
  }

   post {
    always {
      echo 'Pipeline finished.'
    }
    success {
      echo 'Build succeeded.'
    }
    failure {
      echo 'Build failed.'
    }
   }
}
