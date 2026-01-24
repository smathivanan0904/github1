pipeline {
    agent any
    options {
        // Skips subsequent stages if a test fails and marks the build as unstable
        skipStagesAfterUnstable()
    }
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies in a virtual environment...'
                sh '''
                    # Set up a virtual environment
                    python3 -m venv venv
                    source venv/bin/activate
                    # Install dependencies
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                    # Activate virtual environment
                    source venv/bin/activate
                    # Run tests and generate a JUnit XML report
                    pytest --junit-xml test-reports/results.xml sources/test_calc.py
                '''
            }
            post {
                always {
                    // Archive the test results for display in the Jenkins UI
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Build/Package') {
            steps {
                echo 'Building the application using PyInstaller...'
                sh '''
                    source venv/bin/activate
                    pyinstaller --onefile sources/add2vals.py
                '''
            }
            post {
                success {
                    // Archive the generated executable artifact
                    archiveArtifacts artifacts: 'dist/add2vals', fingerprint: true
                }
            }
        }
    }
}
