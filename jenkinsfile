pipeline {
    agent any

    parameters {
        string(name: 'FILENAME', defaultValue: 'app.py')
    }

    stages {
        stage('Run') {
            steps {
                bat "python ${params.FILENAME}"
            }
        }
    }
}