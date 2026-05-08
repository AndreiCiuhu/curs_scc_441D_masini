pipeline {
	agent any
	stages {
		stage('Install dependencies') {
			steps {
				sh 'pip3 install flask --break-system-packages'
			}
		}
		stage('Run tests') {
			steps {
				sh 'cd app && python3 -m unittest discover -s test'
			}
		}
	}
}

