pipeline {
    agent any

    parameters {
        string(name: 'FILENAME', defaultValue: 'app.py')
    }

    stages {
        stage('Run') {
            steps {
                bat "C:\\Users\\VENKY\\AppData\\Local\\Programs\\Python\\Python312\\python.exe ${params.FILENAME}"
            }
        }
    }
}
