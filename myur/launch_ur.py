# myur/launch_ur.py

import subprocess

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Launch UR control")
    parser.add_argument('--ur_type', type=str, default='ur3e', help='Type of UR robot')
    parser.add_argument('--robot_ip', type=str, required=True, help='IP address of the robot')
    parser.add_argument('--launch_rviz', type=bool, default=False, help='Launch RViz')
    
    args = parser.parse_args()
    
    # Build the command with arguments
    command = [
        "ros2", "launch", "ur_robot_driver", "ur_control.launch.py",
        f"ur_type:={args.ur_type}", f"robot_ip:={args.robot_ip}", f"launch_rviz:={str(args.launch_rviz).lower()}"
    ]
    
    # Execute the command
    subprocess.run(command)

if __name__ == "__main__":
    main()
