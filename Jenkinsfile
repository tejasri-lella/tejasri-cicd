pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'tejasri06'
        NAME = 'tejasri'
        ROLL_NUMBER = '2023bcs0166'

        IMAGE_FRONTEND = "${DOCKERHUB_USERNAME}/${NAME}_${ROLL_NUMBER}_frontend"
        IMAGE_BACKEND  = "${DOCKERHUB_USERNAME}/${NAME}_${ROLL_NUMBER}_backend"
    }

    stages {
      stage('Checkout Source Code') {
            steps {
                echo "Cloning repository..."
                // Using the explicit 'url' parameter helps avoid the 'null' error
                git url: 'https://github.com/tejasri-lella/tejasri-cicd.git', branch: 'main'
            }
        }
        stage('Build Docker Images') {
            steps {
                echo "Building frontend image..."
                sh "docker build -t ${IMAGE_FRONTEND} ./frontend"

                echo "Building backend image..."
                sh "docker build -t ${IMAGE_BACKEND} ./backend"
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                echo "Pushing frontend image..."
                sh "docker push ${IMAGE_FRONTEND}"

                echo "Pushing backend image..."
                sh "docker push ${IMAGE_BACKEND}"
            }
        }
    }

    post {
        success {
            echo """
            Pipeline completed successfully 🎉

            Frontend Image:
            https://hub.docker.com/r/${IMAGE_FRONTEND}

            Backend Image:
            https://hub.docker.com/r/${IMAGE_BACKEND}
            """
        }

        failure {
            echo "Pipeline failed ❌ Check logs."
        }

        always {
            echo "Cleaning up local images..."
            // Using || true to ensure the pipeline doesn't fail if the image was never built
            sh "docker rmi ${IMAGE_FRONTEND} || true"
            sh "docker rmi ${IMAGE_BACKEND} || true"
        }
    }
}
