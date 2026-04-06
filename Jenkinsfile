pipeline {
    agent any

    parameters {
        string(name: 'FILENAME', defaultValue: 'data_types.py')
    }

    stages {
        stage('Run') {
            steps {
                bat "C:\\Users\\VENKY\\AppData\\Local\\Programs\\Python\\Python312\\python.exe ${params.FILENAME}"
            }
        }
    }
}
