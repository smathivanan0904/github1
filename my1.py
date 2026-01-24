pipeline {
    agent any // Runs on any available agent
    stages {
        stage('Check Python Version') {
            steps {
                echo 'Checking Python version...'
                // Executes the 'python3 --version' command in the shell
                sh 'python3 --version'
            }
        }
    }
}

