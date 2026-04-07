node {
    stage('Checkout') {
        git 'https://github.com/YOUR_USERNAME/jenkins-multibranch-demo.git'
    }

    stage('Build') {
        bat 'python app.py'
    }

    stage('Test') {
        bat 'echo Testing successful'
    }

    stage('Deploy') {
        bat 'if not exist C:\\DeployFolder mkdir C:\\DeployFolder'
        bat 'copy app.py C:\\DeployFolder\\'
        bat 'python C:\\DeployFolder\\app.py'
    }
}
 
