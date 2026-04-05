pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // Clone GitHub repo main branch
                git branch: 'main', url: 'https://github.com/venkeyroyal/leaarning.git'
            }
        }

        stage('Check files') {
            steps {
                echo 'Checking workspace files...'
                bat 'dir'
            }
        }

        stage('Run Python') {
            steps {
                echo 'Running Python project...'
                // Run existing Python file Hello_world.py
                bat 'C:\\Users\\VENKY\\AppData\\Local\\Programs\\Python\\Python312\\python.exe Hello_world.py'
            }
        }
    }
}
