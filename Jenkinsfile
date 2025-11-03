pipeline {
    agent any
    environment {
    DOCKERHUB_CREDENTIALS = 'dockerhub-creds'  // set this in Jenkins credentials
    DOCKER_IMAGE = "yourdockerhubusername/lab-flask"
    }
    stages {
    stage('Checkout') {
        steps { checkout scm }
    }
    stage('Build Docker Image') {
        steps {
        sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
        }
    }
    stage('Push to Docker Hub') {
        steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
            sh 'echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin'
            sh "docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
            sh "docker tag ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ${DOCKER_IMAGE}:latest"
            sh "docker push ${DOCKER_IMAGE}:latest"
        }
        }
    }
    }
    post {
    always { archiveArtifacts artifacts: '**/*', fingerprint: true }
    }
}
