pipeline {
    agent any  // Use any available agent, or specify one if needed
    
    environment {
        AWS_REGION = "us-east-1"
        AWS_TOPIC = "test/topic"
    }

     stages {
        
        stage('Connect to AWS') {
            steps {
                // Use AWS credentials in this block
                withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                 sh 'aws sts get-caller-identity'
                    }
                }
            }
            stage('Publish to AWS IoT') {
            steps {
                script {
                    def message = "Hello from Jenkins"
                    def encodedMessage = sh(script: "echo '${message}' | base64", returnStdout: true).trim()

                    sh """
                        aws iot-data publish --topic "$AWS_TOPIC" --payload "$(echo '$encodedMessage' | base64 --decode)" --region "$AWS_REGION"
                    """
                }
            }
        }
      
    }
}
