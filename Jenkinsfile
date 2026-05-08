pipeline {
	agent any
	stages {
		stage('Install dependencies') {
			steps {
				sh 'pip3 install -r requirement.txt --break-system-packages'
			}
		}
		stage('Run tests') {
			steps {
				sh 'export PYTHONPATH=$PYTHONPATH:. && python3 -m unittest discover -s app/test'
			}
		}
	}
}

