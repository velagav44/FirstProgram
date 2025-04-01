pipeline {
    agent any  
    
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
                  
                   def encodedMessage = sh(script: "echo 'Hello from Jenkins' | base64", returnStdout: true).trim()
                 
                   withAWS(credentials: 'aws-credentials', region: 'us-east-1'){
                   // sh 'aws iot-data publish --topic "\$AWS_TOPIC" --payload "$(echo '${encodedMessage}' | base64 --decode)" --region "\$AWS_REGION"'
                    sh 'aws iot-data publish --topic "$AWS_TOPIC" --payload "${encodedMessage}" --region "$AWS_REGION"'
                   }
                }
            }
        }
      
    }
}
