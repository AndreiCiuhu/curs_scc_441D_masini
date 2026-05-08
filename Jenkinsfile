pipeline {
	agent any
	stages {
		stage('Install dependencies') {
			steps {
				sh 'pip3 install -r requirement.txt'
			}
		}
		stage('Run tests') {
			steps {
				sh 'PYTHONPATH=. python3 -m unittest discover -s app/test'
			}
		}
	}
}

