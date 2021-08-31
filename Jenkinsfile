pipeline {
  environment {
    imagename = "bogotolec/devops_web_app"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Build image') {
      steps {
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Test') {
      steps {
        script {
          dockerImage.inside {
            sh 'python3 test.py'
          }
        }
      }
    }
    stage('Push') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
            dockerImage.push('latest')
          }
        }
      }
    }
  }
}