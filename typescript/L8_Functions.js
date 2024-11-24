// Basic Functions

function sayHello() {
    console.log("Hello, Cloud Engineer!");
}

// Calling Function
sayHello();

// Function Parameters

function deployToRegion(region) {
    console.log("Deploying to region: " + region);

}

// ----- Calling Function with Prameters -----
deployToRegion("us-east-1");

// Exercise 

function configureService(serviceName, tier){
    console.log("Confoguring " + serviceName + " service with tier: " + tier);

}

configureService("EC2", "t2.micro")
configureService("S3", "standard")