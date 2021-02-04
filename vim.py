import boto3 region = str(input("Enter the Region_Name: ")) access_key 
= str(input("Enter the access_key: ")) secret_key = str(input("Enter 
the secret_key: ")) VPCcidr = str(input("Enter the VPCcidr: ")) 
SubnetCidr = str(input("Enter the SubnetCidr: ")) SubnetAZ = 
str(input("Enter the SubnetAZ: ")) VPCname = str(input("Enter the 
VPCname: ")) Subnetname = str(input("Enter the Subnetname: ")) 
destcidr = str(input("Enter the destcidr: ")) client = 
boto3.client('ec2',
		region_name = region, aws_access_key_id = access_key, 
		aws_secret_access_key = secret_key)
#Creating VPC
myvpc = client.create_vpc( CidrBlock=VPCcidr, 
    InstanceTenancy='default', 
    TagSpecifications=[{'ResourceType':'vpc','Tags':[{'Key':'Name','Value':VPCname}]}])
print("Created VPC") print(myvpc['Vpc']['VpcId'])
#Creating Subnet
mysubnet = client.create_subnet( CidrBlock=SubnetCidr, 
	AvailabilityZone='ap-south-1a',
    VpcId=myvpc['Vpc']['VpcId'], 
    TagSpecifications=[{'ResourceType':'subnet','Tags':[{'Key':'Name','Value':Subnetname}]}])
print("Created Subnet") print(mysubnet['Subnet']['SubnetId'])
#CreatingRouteTable
myroutetable = client.create_route_table( VpcId=myvpc['Vpc']['VpcId'], 
    TagSpecifications=[{'ResourceType':'route-table','Tags':[{'Key':'Name','Value':'Boto3RT'}]}])
print("Created RouteTable") 
print(myroutetable['RouteTable']['RouteTableId'])
#CreatingInternetGateway
myigw = client.create_internet_gateway( 
    TagSpecifications=[{'ResourceType':'internet-gateway','Tags':[{'Key':'Name','Value':'Boto3IGW'}]}])
print("Created InternetGateway") 
print(myigw['InternetGateway']['InternetGatewayId']) routetableassoc = 
client.associate_route_table(
    RouteTableId=myroutetable['RouteTable']['RouteTableId'], 
	SubnetId=mysubnet['Subnet']['SubnetId'])
print("Associated Subnets") attachigw = 
client.attach_internet_gateway(
    VpcId=myvpc['Vpc']['VpcId'], 
	InternetGatewayId=myigw['InternetGateway']['InternetGatewayId'])
print("Attached IGW") routeentry = client.create_route( 
    RouteTableId=myroutetable['RouteTable']['RouteTableId'],
	DestinationCidrBlock=destcidr, 
	GatewayId=myigw['InternetGateway']['InternetGatewayId'])
print("Added RouteEntry")
