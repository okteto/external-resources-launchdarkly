# Create a Development Environment with LaunchDarkly, Okteto, and Python

The LaunchDarkly Okteto integration enables you to automatically create a LaunchDarkly environment every time your team creates a development or preview environment. With this, your team will be able to use feature flags as part of the development lifecycle. 

Okteto will automatically manage the lifecycle of the LaunchDarkly environment for you. When an environment is created in Okteto, the LaunchDarkly environment will be created automatically, and when the environment is destroyed, the LaunchDarkly environment will be destroyed as well. 

## Prerequisites

To use the LaunchDarkly Okteto integration, you must meet the following prerequisites:
1. A LaunchDarkly account
1. A LaunchDarkly project 
1. An Okteto account (([Sign-up](https://www.okteto.com/try-free/) for 30 day, self-hosted free trial))


## Instructions

1. Add the following environment variables to your Okteto secrets. This could be at the user level (if it's only for you) or at the Admin level (if you want to enable your entire team):

- `LAUNCHDARKLY_ACCESS_TOKEN`: A token with read/write access to your LaunchDarkly project. To create one, check out the official docs on [Creating API access tokens](https://docs.launchdarkly.com/home/account-security/api-access-tokens#creating-api-access-tokens).
- `LAUNCHDARKLY_PROJECT_KEY`: The key of your LaunchDarkly project. You can find this in your *Account settings* -> *Projects*, underneath the project name.
- `LAUNCHDARKLY_SOURCE`: The key of the environment you want to use as the source for new environments. If empty, Okteto will create a new project for every environment.

2. Update your Okteto manifest to include LaunchDarkly as a dependency:
    
        ...
        dependencies:
            launchdarkly:
                - https://github.com/okteto/launchdarkly
        ...

3. Go to the LaunchDarkly dashboard, in your source environment, create a new boolean feature flag called `use-new-emojis`

4. Deploy your Okteto environment

5. Using the Okteto dashboard open the newly deployed endpoint for the *external-resources-launchdarkly* environment and notice the output being "Hello World! 🌐" 

6. Go to the LaunchDarkly dashboard, you should find a new environment named after your Okteto namespace, find the `use-new-emojis` feature flag

7. Toggle the value to **ON** and reload the *external-resources-launchdarkly* endpoint, notice the new output being "Hello New World! 🌎"

8. You're now up and running to start using feature flags as part of your development lifecycle 🚀
