pipeline {
    agent any

    parameters {
        string(name: 'FILENAME', defaultValue: 'Bank_Account.py')
        string(name: 'ACCOUNT_NAME', defaultValue: 'Venky')  // user input substitute
    }

    stages {
        stage('Run') {
            steps {
                bat "C:\\Users\\VENKY\\AppData\\Local\\Programs\\Python\\Python312\\python.exe ${params.FILENAME} ${params.ACCOUNT_NAME}"
            }
        }
    }
}
