pipeline {

    agent any

    stages {

        stage('Build') {

            steps {

                dir('sample-java-app/sampleapp') {

                    script {

                        def status = sh(
                            script: 'mvn clean install > ../../build.log 2>&1',
                            returnStatus: true
                        )

                        if (status != 0) {

                            echo "Build failed. Starting self-healing..."

                            sh 'cd ../.. && python3 healer/analyze_logs.py'

                            echo "Retrying build after healing..."

                            sh 'mvn clean install'
                        }
                    }
                }
            }
        }
    }
}