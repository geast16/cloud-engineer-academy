import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

interface MyBucketProps {
  bucketName: string;
  versioned: boolean;
  encryption: s3.BuceketEncryption;
}

export class Week10CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucketProps: MyBucketProps = {
      bucketName: 'My-S3-Bucekt-GE-CDK- ' + this.account,
      versioned: true,
      encryption: S3.BuceketEncryption.S3_MANAGED,
    }

    new s3.Bucket(this, "is MyFirstBucket", bucketProps)
  }
}
