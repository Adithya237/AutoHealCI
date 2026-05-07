pipeline {

    agent any

    stages {

        stage('Build') {

            steps {

                dir('sample-java-app/sampleapp') {

                    sh 'mvn clean install > ../../build.log'

                }
            }
        }
    }

    post {

        failure {

            sh 'python3 healer/analyze_logs.py'

        }
    }
}