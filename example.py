response = { 
  "Reservations": [
    {
      "ReservationId": "r-1234567890abcdef0",
      "OwnerId": "123456789012",
      "Groups": [],
      "Instances": [
        {
          "InstanceId": "i-1234567890abcdef0",
          "ImageId": "ami-bff32ccc",
          "InstanceType": "t2.micro",
          "State": {
            "Code": 16,
            "Name": "running"
          },
          "PrivateIpAddress": "192.168.1.88",
          "PublicIpAddress": "54.194.252.215",
          "Architecture": "x86_64",
          "RootDeviceType": "ebs",
          "RootDeviceName": "/dev/xvda",
          "LaunchTime": "2018-05-08T16:46:19+00:00",
          "Placement": {
            "AvailabilityZone": "eu-west-1c",
            "Tenancy": "default"
          },
          "Monitoring": {
            "State": "disabled"
          },
          "VpcId": "vpc-11112222",
          "SubnetId": "subnet-56f5f633",
          "KeyName": "my_keypair"
        }
      ]
    },
    ],
    'ResponseMetadata': {
        '...': '...',
    },
}

print(response["Reservations"][0]["Instances"][0]["PublicIpAddress"])
print(response["Reservations"][0]["Instances"][0].keys())

state = response["Reservations"][0]["Instances"][0]["State"]["Name"]

if state == "running":
    print("Stop the mechine")
else:
    print("Start mechine")