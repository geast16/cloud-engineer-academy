// Variables, Let and Const

function deployResources(isProduction) {
    let region = "us-east-1"; // Default region for development

    if (isProduction) {
        let region = "us-east-2"; // Region for production
        console.log(`Deploying production resources in ${region}`);
        // Deploy production-specific resources here
    }

    console.log(`Setting up monitoring in ${region}`);
    // Set up monitoring here
}

deployResources(true); // Deploy for Prod
deployResources(false); // Deploy for Dev