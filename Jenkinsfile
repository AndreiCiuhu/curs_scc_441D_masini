pipeline {
  agent any

  stages {
    stage('Install dependencies') {
      steps {
        sh 'python3 -m venv venv'
        sh './venv/bin/pip install -r quickrequirements.txt'
      }
    }

    stage('Run tests') {
      steps {
        sh 'pytest -q'
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
        sh 'docker run -d -p 5000:5000 --name masini masini'
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
