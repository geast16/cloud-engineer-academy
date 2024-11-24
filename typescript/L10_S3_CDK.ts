import * as cdk from '@aws-cdk/core';
import * as s3 from '@aws-cdk/aws-s3';

export class MyStack extends cdk.Stack {
    constructor(scope: cdk.Constrict, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Define resources for this stack
        new s3.Bucket(this, 'MyBucket', {
            versioned: true,
            encryption: s3.BuceketEncryption.S3_MANAGED,

        });   
   
    }
}