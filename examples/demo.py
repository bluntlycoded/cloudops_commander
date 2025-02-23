from cloudops_commander.deploy import deploy
from cloudops_commander.monitor import watch
from cloudops_commander.iac import generate_terraform_config, generate_cloudformation_config

@deploy(target="aws", region="us-east-1")
def launch_my_app():
    print("Launching my app into the cloud with swagger!")

def main():
    launch_my_app()
    watch(service="test_service", alert_callback=lambda msg: print(f"Alert received: {msg}"))
    print("\nTerraform Config:\n", generate_terraform_config())
    print("\nCloudFormation Config:\n", generate_cloudformation_config())

if __name__ == "__main__":
    main()
