pipeline {
    agent any

    parameters {
        string(name: 'FILENAME', defaultValue: 'app.py')
    }

    stages {
        stage('Run') {
            steps {
                bat "C:\\Python312\\python.exe ${params.FILENAME}"
            }
        }
    }
}
