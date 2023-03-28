# Create a Development Environment with LaunchDarkly, Okteto, and Python

The LaunchDarkly Okteto integration enables you to automatically create a LaunchDarkly environment everytime your team creates a development or preview environment. With this, your team will be able to use feature flags as part of the development lifecycle. 

Okteto will autoamtically manage the lifecycle of the LaunchDarkly environment for you. When an environment is created in Okteto, the LaunchDarkly enviroment will be created automatically, and when the environment is destroyed, the LaunchDarkly environment will be destroyed as well. 

## Prerequisites

To use the LaunchDarkly Okteto integration, you must meet the following prerequisites:
1. A LaunchDarkly account
1. A LaunchDarkly project 
1. An Okteto account


## Instructions


1. Add the following environment variables to your Okteto secrets. This could be at the user level (if it's only for you) or at the Admin level (if you want to enable your entire team):

        LAUNCHDARKLY_ACCESS_TOKEN: A token with read/write access to your LaunchDarkly project.
        LAUNCHDARKLY_PROJECT_KEY: The key of your LaunchDarkly project.
        LAUNCHDARKLY_SOURCE: The key of the environment you want to use as the source for new environments. If empty, Okteto will create a new project for every environment.

2. Update your Okteto manifest to include LaunchDarkly as a dependency:
    
        ...
        dependencies:
            launchdarkly:
                - https://github.com/okteto/launchdarkly
        ...

3. Deploy your environment, and start using feature flags as part of your development lifecycle 🚀.