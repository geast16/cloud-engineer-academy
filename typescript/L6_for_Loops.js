// For Loops

let regions = ["us-east-1", "us-west-1", 'ap-souteast-1', "eu-west-1"]

for (let i = 0; i < regions.length; i++) {
    console.log("Deploying to region: " + regions[i]);

}

// ----- Exercise ------

// Array of Cloud Services

let cloudServices = ["EC2", "S3", "Lambda", "DynamoDB"];

for (let i = 0; i < cloudServices.length; i++) {
console.log("Configuring AWS " + cloudServices[i] + "Services")

}